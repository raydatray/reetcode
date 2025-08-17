from sortedcontainers import SortedDict
from dataclasses import dataclass
from typing import Callable, Dict, List


@dataclass
class FieldValue:
    value: str
    expiry: int | None

    def is_expired(self, curr_time: int) -> bool:
        return self.expiry is not None and self.expiry <= curr_time


@dataclass
class BackupSnapshot:
    db: Dict[str, Dict[str, "FieldValue"]]
    timestamp: int


class InMemoryDB:
    def __init__(self):
        self.db: Dict[str, Dict[str, "FieldValue"]] = {}
        self.backups = SortedDict()
        self.curr_time = 0

    def set(self, key: str, field: str, value: str):
        self.db.setdefault(key, {})[field] = FieldValue(value, None)

    def set_at(self, key: str, field: str, value: str, timestamp: int):
        self.curr_time = timestamp
        self.set(key, field, value)

    def set_at_with_ttl(
        self, key: str, field: str, value: str, timestamp: int, ttl: int
    ):
        self.curr_time = timestamp
        self.db.setdefault(key, {})[field] = FieldValue(value, ttl)

    def get(self, key: str, field: str) -> str | None:
        fields = self.db.get(key)
        if fields is None:
            return None

        value = fields.get(field)
        if value is None or value.is_expired(self.curr_time):
            return None

        return value.value

    def get_at(self, key: str, field: str, timestamp: int) -> str | None:
        self.curr_time = timestamp
        return self.get(key, field)

    def delete(self, key: str, field: str) -> bool:
        fields = self.db.get(key)
        if fields is None:
            return False

        value = fields.get(field)
        if value is None:
            return False

        if value.is_expired(self.curr_time):
            fields.pop(field)
            if not fields:
                self.db.pop(field)
            return True

        return False

    def delete_at(self, key: str, field: str, timestamp: int) -> bool:
        self.curr_time = timestamp
        return self.delete(key, field)

    def scan_with_filter(self, key: str, op: Callable[[str], bool]) -> List[str]:
        fields = self.db.get(key)
        if fields is None:
            return []

        result = [
            f"{field_name}({field_value.value})"
            for field_name, field_value in fields.items()
            if op(field_name) and not field_value.is_expired(self.curr_time)
        ]
        result.sort()

        return result

    def scan(self, key: str) -> List[str]:
        return self.scan_with_filter(key, lambda _: True)

    def scan_by_prefix(self, key: str, prefix: str) -> List[str]:
        return self.scan_with_filter(key, lambda x_: x_.startswith(prefix))

    def scan_at(self, key: str, timestamp: int) -> List[str]:
        self.curr_time = timestamp
        return self.scan(key)

    def scan_by_prefix_at(self, key: str, prefix: str, timestamp: int) -> List[str]:
        self.curr_time = timestamp
        return self.scan_by_prefix(key, prefix)

    def backup(self, timestamp: int) -> int:
        self.curr_time = timestamp
        self._purge_expired()

        snapshot = BackupSnapshot(self.db, timestamp)
        self.backups[timestamp] = snapshot

        count = 0
        for key, fields in self.db.items():
            if fields:
                count += 1

        return count

    def restore(self, timestamp: int, timestamp_to_restore: int):
        self.curr_time = timestamp

        backup = self.backups.peekitem(-1)[1]
        restored_db = self._recalculate_expiry_times(
            backup, backup.backup_time, timestamp
        )

        self.db = restored_db
        self._purge_expired()

    def _purge_expired(self):
        for key, fields in self.db.items():
            for field, value in fields.items():
                if value.is_expired(self.curr_time):
                    fields.pop(field)

            if not fields:
                self.db.pop(key)

    def _recalculate_expiry_times(
        self,
        db: Dict[str, Dict[str, "FieldValue"]],
        backup_time: int,
        restore_time: int,
    ) -> Dict[str, Dict[str, "FieldValue"]]:
        result: Dict[str, Dict[str, "FieldValue"]] = {}

        for key, fields in db.items():
            new_fields: Dict[str, "FieldValue"] = {}
            for field, value in fields.items():
                ttl = self._calculate_remaining_ttl(value.expiry, backup_time)

                if ttl is not None:
                    expiry = restore_time + ttl
                elif value.expiry is not None:
                    expiry = restore_time - 1
                else:
                    expiry = None

                new_fields[field] = FieldValue(value.value, expiry)

            result[key] = new_fields

        return result

    def _calculate_remaining_ttl(
        self, expiry: int | None, from_time: int
    ) -> int | None:
        if expiry is None:
            return None

        ttl = expiry - from_time
        return ttl if ttl > 0 else None
