"""
https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/?envType=company&envId=roblox&favoriteSlug=roblox-all

Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.
Return the decimal value of the number in the linked list.
The most significant bit is at the head of the linked list.

Example 1:
Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10

Example 2:
Input: head = [0]
Output: 0

Constraints:
The Linked List is not empty.
Number of nodes will not exceed 30.
Each node's value is either 0 or 1.
"""

from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: Optional[ListNode] = next


class Solution:
    def get_decimal_value(self, head: Optional[ListNode]) -> int:
        result = 0
        head_ptr = head
        len = 0

        while head:
            len += 1
            head = head.next

        head = head_ptr
        len -= 1

        while head:
            result += head.val * (2**len)
            len -= 1
            head = head.next

        return result


def test_one():
    solution = Solution()
    result = solution.get_decimal_value(ListNode(1, ListNode(0, ListNode(1))))

    assert result == 5


def test_two():
    solution = Solution()
    result = solution.get_decimal_value(ListNode(0))

    assert result == 0
