"""
https://leetcode.com/problems/subarrays-with-k-different-integers/description/?envType=company&envId=roblox&favoriteSlug=roblox-all

Given an integer array nums and an integer k, return the number of good subarrays of nums.
A good array is an array where the number of different integers in that array is exactly k.
For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]

Example 2:
Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].

Constraints:
1 <= nums.length <= 2 * 10^4
1 <= nums[i], k <= nums.length
"""

from typing import List


class Solution:
    def subarrays_with_k_distinct(self, nums: List[int], k: int) -> int:
        distinct = [0 for _ in range(len(nums) + 1)]

        left, right = 0, 0
        curr_count = 0
        result = 0

        while right < len(nums):
            distinct[nums[right]] += 1

            if distinct[nums[right]] == 1:
                k -= 1

            if k < 0:
                distinct[nums[left]] -= 1
                if distinct[nums[left]] == 0:
                    k += 1
                left += 1
                curr_count = 0

            if k == 0:
                while distinct[nums[left]] > 1:
                    distinct[nums[left]] -= 1
                    left += 1
                    curr_count += 1

                result += curr_count + 1

            right += 1

        return result


def test_one():
    solution = Solution()
    result = solution.subarrays_with_k_distinct([1, 2, 1, 2, 3], 2)

    assert result == 7


def test_two():
    solution = Solution()
    result = solution.subarrays_with_k_distinct([1, 2, 1, 3, 4], 3)

    assert result == 3
