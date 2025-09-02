"""
https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/description/?envType=company&envId=roblox&favoriteSlug=roblox-all

Given a string s, return the maximum number of occurrences of any substring under the following rules:
The number of unique characters in the substring must be less than or equal to maxLetters.
The substring size must be between minSize and maxSize inclusive.

Example 1:
Input: s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
Output: 2
Explanation: Substring "aab" has 2 occurrences in the original string.
It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).

Example 2:
Input: s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
Output: 2
Explanation: Substring "aaa" occur 2 times in the string. It can overlap.

Constraints:
1 <= s.length <= 10^5
1 <= maxLetters <= 26
1 <= minSize <= maxSize <= min(26, s.length)
s consists of only lowercase English letters.
"""

from collections import defaultdict
from typing import Dict


class Solution:
    def max_freq(self, s: str, max_letters: int, min_size: int, max_size: int) -> int:
        window_counts: Dict[str, int] = defaultdict(int)
        substr_freq: Dict[str, int] = defaultdict(int)
        result = 0

        for i, ch in enumerate(s):
            window_counts[ch] += 1

            if i >= min_size:
                left_ch = s[i - min_size]
                window_counts[left_ch] -= 1

                if window_counts[left_ch] == 0:
                    del window_counts[left_ch]

            if i + 1 >= min_size and len(window_counts) <= max_letters:
                substr = s[i - min_size + 1 : i + 1]
                substr_freq[substr] += 1
                result = max(result, substr_freq[substr])

        return result


def test_one():
    solution = Solution()
    result = solution.max_freq("aababcaab", 2, 3, 4)

    assert result == 2


def test_two():
    solution = Solution()
    result = solution.max_freq("aaaa", 1, 3, 3)

    assert result == 2
