"""
KVStore with metrics

DBricks R1

Make a key value store, but you can mesaure the average QPS over X seconds
"""

import time
from typing import Dict


class KVStore:
    def __init__(self, window_seconds=300):
        self.store: Dict[str, int] = {}
        self.window_seconds = window_seconds
        self.put_buckets = [0 for _ in range(window_seconds)]
        self.get_buckets = [0 for _ in range(window_seconds)]
        self.last_update = int(time.time())

    def put(self, key: str, val: int):
        curr_time_int = int(time.time())
        self._update_buckets(curr_time_int)

        self.store[key] = val

        self.put_buckets[self._get_bucket_idx(curr_time_int)] += 1

    def get(self, key: str) -> int:
        curr_time_int = int(time.time())
        self._update_buckets(curr_time_int)
        self.get_buckets[self._get_bucket_idx(curr_time_int)] += 1

        return self.store[key]

    def put_qps(self) -> float:
        curr_time_int = int(time.time())
        self._update_buckets(curr_time_int)

        return sum(self.put_buckets) / self.window_seconds

    def get_qps(self) -> float:
        curr_time_int = int(time.time())
        self._update_buckets(curr_time_int)

        return sum(self.get_buckets) / self.window_seconds

    def _get_bucket_idx(self, curr_time_int: int) -> int:
        return curr_time_int & self.window_seconds

    def _update_buckets(self, curr_time_int: int):
        if curr_time_int - self.last_update >= self.window_seconds:
            self.put_buckets = [0 for _ in range(self.window_seconds)]
            self.get_buckets = [0 for _ in range(self.window_seconds)]
        else:
            time_diff = curr_time_int - self.last_update

            for i in range(min(time_diff, self.window_seconds)):
                bucket_to_clear = (self.last_update + i + 1) % self.window_seconds
                self.put_buckets[bucket_to_clear] = 0
                self.get_buckets[bucket_to_clear] = 0

        self.last_update = curr_time_int
