"""
https://leetcode.com/problems/regular-expression-matching/description/?envType=company&envId=citadel&favoriteSlug=citadel-all

Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Constraints:

1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
"""

from typing import Dict, Tuple


class Solution:
    def is_match(self, s: str, p: str) -> bool:
        memo: Dict[Tuple, bool] = {}

        def match(i: int, j: int) -> bool:
            if (i, j) in memo:
                return memo[(i, j)]

            if j == len(p):
                return i == len(s)

            first_match = i < len(s) and p[j] in {s[i], "."}

            if j + 1 < len(p) and p[j + 1] == "*":
                result = match(i, j + 2) or (first_match and match(i + 1, j))
            else:
                result = first_match and match(i + 1, j + 1)

            memo[(i, j)] = result
            return result

        return match(0, 0)


def test_is_match_fail_simple():
    solution = Solution()
    assert not solution.is_match("aa", "a")


def test_is_match_repeating():
    solution = Solution()
    assert solution.is_match("aa", "a*")


def test_is_match_wild_repeating():
    solution = Solution()
    assert solution.is_match("ab", ".*")
