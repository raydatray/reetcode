"""
https://leetcode.com/problems/two-sum/description/?envType=company&envId=roblox&favoriteSlug=roblox-all

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 10^4
-109 <= nums[i] <= 10^9
-109 <= target <= 10^9
Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

from typing import Dict, List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        complements: Dict[int, int] = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in complements:
                return [complements[complement], i]
            else:
                complements[num] = i

        return []


def test_one():
    solution = Solution()
    result = solution.two_sum([2, 7, 11, 15], 9)

    assert sorted(result) == [0, 1]


def test_two():
    solution = Solution()
    result = solution.two_sum([3, 2, 4], 6)

    assert sorted(result) == [1, 2]


def test_three():
    solution = Solution()
    result = solution.two_sum([3, 3], 6)

    assert sorted(result) == [0, 1]
