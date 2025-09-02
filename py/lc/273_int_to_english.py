"""
https://leetcode.com/problems/integer-to-english-words/description/?envType=company&envId=roblox&favoriteSlug=roblox-all

Convert a non-negative integer num to its English words representation.

Example 1:
Input: num = 123
Output: "One Hundred Twenty Three"

Example 2:
Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:
Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Constraints:
0 <= num <= 2^31 - 1
"""


class Solution:
    def number_to_words(self, num: int) -> str:
        if num == 0:
            return "Zero"

        sub_twenties = [
            "",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
            "Ten",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen",
        ]
        tens = [
            "",
            "",
            "Twenty",
            "Thirty",
            "Forty",
            "Fifty",
            "Sixty",
            "Seventy",
            "Eighty",
            "Ninety",
        ]
        thousands = ["", "Thousand", "Million", "Billion"]

        def helper(n: int) -> str:
            if n == 0:
                return ""
            elif n < 20:
                return sub_twenties[n] + " "
            elif n < 100:
                return tens[n // 10] + " " + helper(n % 10)
            else:
                return sub_twenties[n // 100] + " Hundred " + helper(n % 100)

        result = ""

        for i, unit in enumerate(thousands):
            if num % 1000 != 0:
                result = helper(num % 1000) + unit + " " + result
            num //= 1000

        return result.strip()


def test_one():
    solution = Solution()
    result = solution.number_to_words(123)

    assert result == "One Hundred Twenty Three"


def test_two():
    solution = Solution()
    result = solution.number_to_words(12345)

    assert result == "Twelve Thousand Three Hundred Forty Five"


def test_three():
    solution = Solution()
    result = solution.number_to_words(1234567)

    assert (
        result
        == "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
    )
