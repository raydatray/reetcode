"""
https://leetcode.com/problems/3sum/description/?envType=company&envId=citadel&favoriteSlug=citadel-all

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.


Constraints:
3 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5
"""

from typing import List


class Solution:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result: List[List[int]] = []

        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            lp, rp = i + 1, len(nums) - 1

            while lp < rp:
                sum = nums[lp] + nums[rp]

                if sum == target:
                    result.append([nums[i], nums[lp], nums[rp]])

                    if lp < len(nums) - 1:
                        lp += 1

                    while lp < len(nums) - 1 and nums[lp] == nums[lp - 1]:
                        lp += 1

                elif sum > target:
                    rp -= 1
                else:
                    lp += 1

        return result


def test_one():
    solution = Solution()
    result = solution.three_sum([-1, 0, 1, 2, -1, -4])

    assert result == [[-1, -1, 2], [-1, 0, 1]]


def test_two():
    solution = Solution()
    result = solution.three_sum([0, 1, 1])

    assert result == []


def test_three():
    solution = Solution()
    result = solution.three_sum([0, 0, 0])

    assert result == [[0, 0, 0]]
