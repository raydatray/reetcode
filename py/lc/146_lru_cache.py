"""
https://leetcode.com/problems/lru-cache/description/?envType=company&envId=optiver&favoriteSlug=optiver-more-than-six-months

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

Constraints:
1 <= capacity <= 3000
0 <= key <= 10^4
0 <= value <= 10^5
At most 2 * 10^5 calls will be made to get and put.
"""

from __future__ import annotations
from typing import Dict, Optional


class DLLNode:
    def __init__(
        self,
        key: int,
        value: int,
        prev: Optional[DLLNode] = None,
        next: Optional[DLLNode] = None,
    ):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRU:
    def __init__(self):
        self.dummy_head = DLLNode(-1, -1, None, None)  # dummy_head.next, least recent
        self.tail = self.dummy_head  # most recent

    def add(self, node: DLLNode):
        node.prev = self.tail
        node.next = None
        self.tail.next = node
        self.tail = node

    def remove(self, node: DLLNode):
        prev = node.prev
        next = node.next

        if prev:
            prev.next = next
        if next:
            next.prev = prev

        if self.tail is node:
            self.tail = prev if prev is not None else self.dummy_head

        node.prev = None
        node.next = None

    def refresh(self, node: DLLNode):
        if node is self.tail:
            return
        self.remove(node)
        self.add(node)

    def evict(self) -> Optional[DLLNode]:
        lru = self.dummy_head.next
        if not lru:
            return None
        self.remove(lru)
        return lru


class LRUCache:
    def __init__(self, capacity: int):
        self.cache: Dict[int, DLLNode] = {}
        self.lru = LRU()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]

        self.lru.refresh(node)

        return node.value

    def put(self, key: int, value: int):
        if key in self.cache:
            node = self.cache[key]

            node.value = value
            self.lru.refresh(node)

            return

        if len(self.cache) == self.capacity:
            evicted_node = self.lru.evict()
            if evicted_node:
                del self.cache[evicted_node.key]

        node = DLLNode(key, value)
        self.cache[key] = node
        self.lru.add(node)


def test_one():
    lRUCache = LRUCache(2)

    lRUCache.put(1, 1)  # cache is {1=1}
    lRUCache.put(2, 2)  # cache is {1=1, 2=2}

    assert lRUCache.get(1) == 1  # return 1

    lRUCache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}

    assert lRUCache.get(2) == -1  # returns -1 (not found)

    lRUCache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}

    assert lRUCache.get(1) == -1  # return -1 (not found)
    assert lRUCache.get(3) == 3  # return 3
    assert lRUCache.get(4) == 4  # return 4
