"""
https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=company&envId=roblox&favoriteSlug=roblox-all

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Example 3:
Input: nums = [1,0,1,2]
Output: 3

Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""

from typing import List


class Solution:
    def longest_consecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        result = 0

        for num in seen:
            if num - 1 not in seen:
                temp_num = num

                while temp_num in seen:
                    temp_num += 1

                result = max(result, temp_num - num)

        return result


def test_one():
    solution = Solution()
    result = solution.longest_consecutive([100, 4, 200, 1, 3, 2])

    assert result == 4


def test_two():
    solution = Solution()
    result = solution.longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])

    assert result == 9


def test_three():
    solution = Solution()
    result = solution.longest_consecutive([1, 0, 1, 2])

    assert result == 3
