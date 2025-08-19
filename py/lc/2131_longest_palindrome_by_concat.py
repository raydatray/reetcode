"""
https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/description/?envType=company&envId=databricks&favoriteSlug=databricks-all

You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.

Example 1:
Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.

Example 2:
Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.

Example 3:
Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".

Constraints:
1 <= words.length <= 10^5
words[i].length == 2
words[i] consists of lowercase English letters.
"""

from collections import Counter
from typing import List


class Solution:
    def longest_palindrome(self, words: List[str]) -> int:
        word_count = Counter(words)
        res = 0
        center_used = False

        for word in word_count:
            count = word_count[word]

            if word[0] == word[1]:
                pairs = count // 2
                res += pairs * 4

                if count % 2 == 1 and not center_used:
                    res += 2
                    center_used = True

            else:
                word_reversed = word[::-1]
                if word_reversed in word_count and word < word_reversed:
                    pairs = min(count, word_count[word_reversed])
                    res += pairs * 4

        return res


def test_one():
    solution = Solution()
    result = solution.longest_palindrome(["lc", "cl", "gg"])

    assert result == 6


def test_two():
    solution = Solution()
    result = solution.longest_palindrome(["ab", "ty", "yt", "lc", "cl", "ab"])

    assert result == 8


def test_three():
    solution = Solution()
    result = solution.longest_palindrome(["cc", "ll", "xx"])

    assert result == 2
