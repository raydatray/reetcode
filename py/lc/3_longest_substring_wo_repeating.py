"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=company&envId=roblox&favoriteSlug=roblox-all

Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.
"""

from typing import Set


class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        seen: Set[str] = set()
        left = 0

        result = 0

        for right, ch in enumerate(s):
            if ch in seen:
                while ch in seen:
                    seen.remove(s[left])
                    left += 1
            seen.add(ch)

            result = max(result, right - left + 1)

        return result


def test_one():
    solution = Solution()
    assert solution.length_of_longest_substring("abcabcbb") == 3


def test_two():
    solution = Solution()
    assert solution.length_of_longest_substring("bbbbb") == 1


def test_three():
    solution = Solution()
    assert solution.length_of_longest_substring("pwwkew") == 3
