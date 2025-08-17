"""
https://leetcode.com/problems/merge-k-sorted-lists/description/?envType=company&envId=citadel&favoriteSlug=citadel-all

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 10^4.
"""

from __future__ import annotations
from dataclasses import dataclass
import heapq
from typing import Optional, List


@dataclass
class ListNode:
    val: int = 0
    next: Optional[ListNode] = None


@dataclass
class HeapListNode:
    node: ListNode

    def __lt__(self, other: HeapListNode) -> bool:
        return self.node.val < other.node.val


class Solution:
    def merge_k_lists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        heap: List[HeapListNode] = []

        for list in lists:
            if list:
                heapq.heappush(heap, HeapListNode(list))

        while heap:
            heap_node = heapq.heappop(heap)
            node = heap_node.node

            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(heap, HeapListNode(node.next))

        return dummy.next


def test_one():
    solution = Solution()
    result = solution.merge_k_lists(
        [
            ListNode(1, ListNode(4, ListNode(5))),
            ListNode(1, ListNode(3, ListNode(4))),
            ListNode(2, ListNode(6)),
        ]
    )

    assert result == ListNode(
        1,
        ListNode(
            1,
            ListNode(
                2, ListNode(3, ListNode(4, ListNode(4, ListNode(5, ListNode(6)))))
            ),
        ),
    )


def test_two():
    solution = Solution()
    result = solution.merge_k_lists([])

    assert result is None


def test_three():
    solution = Solution()
    result = solution.merge_k_lists([None])

    assert result is None
