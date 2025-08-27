"""
https://leetcode.com/problems/longest-common-prefix/description/?envType=company&envId=roblox&favoriteSlug=roblox-all

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""

from typing import List


class Solution:
    def longest_common_prefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        for char_index in range(len(strs[0])):
            char = strs[0][char_index]

            for str_index in range(1, len(strs)):
                if (
                    char_index == len(strs[str_index])
                    or char != strs[str_index][char_index]
                ):
                    return strs[0][0:char_index]

        return strs[0]


def test_one():
    solution = Solution()
    result = solution.longest_common_prefix(["flower", "flow", "flight"])

    assert result == "fl"


def test_two():
    solution = Solution()
    result = solution.longest_common_prefix(["dog", "racecar", "car"])

    assert result == ""
