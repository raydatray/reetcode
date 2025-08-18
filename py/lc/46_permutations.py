"""
https://leetcode.com/problems/permutations/description/?envType=company&envId=citadel&favoriteSlug=citadel-all

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res: List[List[int]] = []
        stack: List[List[int]] = [[]]

        while stack:
            curr = stack.pop()

            if len(curr) == len(nums):
                res.append(curr)
                continue

            for num in nums:
                if num not in curr:
                    stack.append(curr + [num])

        return res


def test_one():
    solution = Solution()
    result = solution.permute([1, 2, 3])

    assert sorted(result) == [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ]


def test_two():
    solution = Solution()
    result = solution.permute([0, 1])

    assert sorted(result) == [[0, 1], [1, 0]]


def test_three():
    solution = Solution()
    result = solution.permute([1])

    assert result == [[1]]
