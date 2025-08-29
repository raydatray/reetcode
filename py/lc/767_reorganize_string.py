"""
https://leetcode.com/problems/reorganize-string/?envType=company&envId=roblox&favoriteSlug=roblox-all

Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

Example 1:
Input: s = "aab"
Output: "aba"

Example 2:
Input: s = "aaab"
Output: ""

Constraints:
1 <= s.length <= 500
s consists of lowercase English letters.
"""

from collections import Counter


class Solution:
    def reorganize_string(self, s: str) -> str:
        char_count = Counter(s)
        max_count, letter = 0, ""

        for char, count in char_count.items():
            if count >= max_count:
                max_count = count
                letter = char

        if max_count > (len(s) + 1) // 2:
            return ""

        result = [" "] * len(s)
        idx = 0

        while char_count[letter] != 0:
            result[idx] = letter
            idx += 2
            char_count[letter] -= 1

        for char, count in char_count.items():
            while count > 0:
                if idx >= len(s):
                    idx = 1

                result[idx] = char
                idx += 2
                count -= 1

        return "".join(result)


def test_one():
    solution = Solution()
    assert solution.reorganize_string("aab") == "aba"


def test_two():
    solution = Solution()
    assert solution.reorganize_string("aaab") == ""
