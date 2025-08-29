"""
https://leetcode.com/problems/count-number-of-nice-subarrays/description/?envType=company&envId=roblox&favoriteSlug=roblox-all

Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
Return the number of nice sub-arrays.

Example 1:
Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

Example 2:
Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.

Example 3:
Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16

Constraints:
1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length
"""

from typing import List


class Solution:
    def number_of_subarrays(self, nums: List[int], k: int) -> int:
        lp = 0
        even, odd = 0, 0
        result = 0

        for rp in range(len(nums)):
            if nums[rp] % 2 == 1:
                odd += 1
                even = 0

            while odd == k:
                if nums[lp] % 2 == 1:
                    odd -= 1
                lp += 1
                even += 1

            result += even

        return result


def test_one():
    solution = Solution()

    assert solution.number_of_subarrays([1, 1, 2, 1, 1], 3) == 2


def test_two():
    solution = Solution()

    assert solution.number_of_subarrays([2, 4, 6], 1) == 0


def test_three():
    solution = Solution()

    assert solution.number_of_subarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2) == 16
