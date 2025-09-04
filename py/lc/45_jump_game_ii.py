"""
https://leetcode.com/problems/jump-game-ii/description/?envType=company&envId=roblox&favoriteSlug=roblox-all

You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.
Each element nums[i] represents the maximum length of a forward jump from index i.
In other words, if you are at index i, you can jump to any index (i + j) where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2

Constraints:
1 <= nums.length <= 10^4
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        curr_end, curr_farthest = 0, 0
        result = 0

        for i in range(len(nums) - 1):
            curr_farthest = max(curr_farthest, i + nums[i])  # type: ignore

            if i == curr_end:
                result += 1
                curr_end = curr_farthest

        return result


def test_one():
    solution = Solution()
    result = solution.jump([2, 3, 1, 1, 4])

    assert result == 2


def test_two():
    solution = Solution()
    result = solution.jump([2, 3, 0, 1, 4])

    assert result == 2
