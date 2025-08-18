"""
https://leetcode.com/problems/first-missing-positive/description/?envType=company&envId=databricks&favoriteSlug=databricks-all

Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Example 2:
Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.

Constraints:
1 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1
"""

from typing import List


class Solution:
    def first_missing_positive(self, nums: List[int]) -> int:
        n = len(nums)
        seen: List[bool] = [False for _ in range(n + 1)]

        for num in nums:
            if 0 <= num <= n:
                seen[num] = True

        for i in range(1, n + 1):
            if not seen[i]:
                return i

        return n + 1


def test_one():
    solution = Solution()
    result = solution.first_missing_positive([1, 2, 0])

    assert result == 3


def test_two():
    solution = Solution()
    result = solution.first_missing_positive([3, 4, -1, 1])

    assert result == 2


def test_three():
    solution = Solution()
    result = solution.first_missing_positive([7, 8, 9, 11, 12])

    assert result == 1
