"""
https://leetcode.com/problems/house-robber-ii/description/?envType=company&envId=databricks&favoriteSlug=databricks-all

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:
Input: nums = [1,2,3]
Output: 3

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 1000
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        prev1, prev2 = 0, 0

        for num in nums[1:]:
            temp = prev1
            prev1 = max(prev2 + num, prev1)
            prev2 = temp

        right_max = prev1

        prev1, prev2 = 0, 0

        for num in nums[:-1]:
            temp = prev1
            prev1 = max(prev2 + num, prev1)
            prev2 = temp

        left_max = prev1

        return max(left_max, right_max)


def test_one():
    solution = Solution()
    result = solution.rob([2, 3, 2])

    assert result == 3


def test_two():
    solution = Solution()
    result = solution.rob([1, 2, 3, 1])

    assert result == 4


def test_three():
    solution = Solution()
    result = solution.rob([1, 2, 3])

    assert result == 3
