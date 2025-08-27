"""
https://leetcode.com/problems/valid-parentheses/description/?envType=company&envId=roblox&favoriteSlug=roblox-all

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
 - Open brackets must be closed by the same type of brackets.
 - Open brackets must be closed in the correct order.
 - Every close bracket has a corresponding open bracket of the same type.


Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Example 5:
Input: s = "([)]"
Output: false

Constraints:
1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def is_valid(self, s: str) -> bool:
        bracket_map = {"]": "[", "}": "{", ")": "("}
        stack = []

        for char in s:
            if char in bracket_map.keys():
                if not stack:
                    return False

                if stack[-1] != bracket_map[char]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)

        return not stack


def test_one():
    solution = Solution()
    assert solution.is_valid("()")


def test_two():
    solution = Solution()
    assert solution.is_valid("()[]{}")


def test_three():
    solution = Solution()
    assert not solution.is_valid("(]")


def test_four():
    solution = Solution()
    assert solution.is_valid("([])")


def test_five():
    solution = Solution()
    assert not solution.is_valid("([)]")
