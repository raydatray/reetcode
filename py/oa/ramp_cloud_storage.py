from typing import Dict, Set


class User:
    def __init__(self, max_capacity: float, is_admin: bool):
        self.files: Set[str] = set()
        self.is_admin = is_admin
        self.max_capacity = max_capacity
        self.in_use = 0.0

    def try_reserve_capacity(self, file_size: float) -> bool:
        if self.is_admin:
            self.in_use += file_size
            return True

        if self.in_use + file_size > self.max_capacity:
            return False

        self.in_use += file_size
        return True


class CloudStorage:
    def __init__(self):
        self.users: Dict[str, "User"] = {"admin": User(float("inf"), True)}
        self.files: Dict[str, float] = {}

    def add_user(self, user_id: str, max_capacity: float) -> bool:
        if user_id in self.users:
            return False

        self.users[user_id] = User(max_capacity, False)
        return True

    def add_file(self, file_name: str, file_size: float) -> bool:
        return self._add_file("admin", file_name, file_size)

    def add_file_by(self, user_id: str, file_name: str, file_size: float) -> bool:
        return self._add_file(user_id, file_name, file_size)

    def copy_file(self, name_from: str, name_to: str) -> bool:
        if name_to in self.files:
            return False

        file_size = self.files.get(name_from)
        if file_size is None:
            return False

        owner = next(
            (
                user_id
                for user_id, user in self.users.items()
                if name_from in user.files
            ),
            None,
        )
        if owner is None:
            return False

        return self._add_file(owner, name_to, file_size)

    def update_user_max_capacity(
        self, user_id: str, new_max_capacity: float
    ) -> int | None:
        user = self.users.get(user_id)
        if user is None or user_id == "admin":
            return None

        user.max_capacity = new_max_capacity

        if user.in_use <= new_max_capacity:
            return 0

        user_file_list = [
            (file_name, self.files[file_name]) for file_name in user.files
        ]

        user_file_list.sort(key=lambda x: (-x[1], x[0]))

        removed_count = 0
        for file_name, _ in user_file_list:
            if user.in_use <= new_max_capacity:
                break

            if self._remove_file(user_id, file_name):
                removed_count += 1

        return removed_count

    def compress_file(self, user_id: str, file_name: str) -> float | None:
        if file_name not in self.files:
            return None

        user = self.users.get(user_id)
        if user is None:
            return None

        original_file_size = self.files.get(file_name)
        if original_file_size is None:
            return None

        compressed_name = f"{file_name}.COMPRESSED"
        compressed_size = original_file_size / 2

        if compressed_name in self.files:
            return None

        self._remove_file(user_id, file_name)
        self._add_file(user_id, compressed_name, compressed_size)

        return user.max_capacity - user.in_use

    def decompress_file(self, user_id: str, file_name: str) -> float | None:
        if not file_name.endswith(".COMPRESSED"):
            return None

        if file_name not in self.files:
            return None

        user = self.users.get(user_id)
        if user is None:
            return None

        original_file_size = self.files.get(file_name)
        if original_file_size is None:
            return None

        decompressed_name = file_name[: -len(".COMPRESSED")]
        decompressed_size = original_file_size * 2

        if decompressed_name in self.files:
            return None

        size_difference = decompressed_size - original_file_size
        if user.in_use + size_difference > user.max_capacity:
            return None

        self._remove_file(user_id, file_name)
        self._add_file(user_id, decompressed_name, decompressed_size)

        return user.max_capacity - user.in_use

    def _add_file(self, user_id: str, file_name: str, file_size: float) -> bool:
        if file_name in self.files:
            return False

        user = self.users.get(user_id)
        if user is None:
            return False

        if not user.try_reserve_capacity(file_size):
            return False

        self.files[file_name] = file_size
        user.files.add(file_name)
        return True

    def _remove_file(self, user_id: str, file_name: str) -> bool:
        if file_name not in self.files:
            return False

        file_size = self.files.get(file_name)
        if file_size is None:
            return False

        user = self.users.get(user_id)
        if user is None:
            return False

        user.files.remove(file_name)
        user.in_use -= file_size

        self.files.pop(file_name)
        return True
