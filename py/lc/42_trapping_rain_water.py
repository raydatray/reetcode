"""
https://leetcode.com/problems/trapping-rain-water/description/?envType=company&envId=citadel&favoriteSlug=citadel-all

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        lp, rp = 0, len(height) - 1
        l_max, r_max = 0, 0
        res = 0

        while lp < rp:
            if height[lp] < height[rp]:
                l_max = max(l_max, height[lp])
                res += l_max - height[lp]
                lp += 1
            else:
                r_max = max(r_max, height[rp])
                res += r_max - height[rp]
                rp -= 1

        return res


def test_one():
    solution = Solution()
    result = solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])

    assert result == 6


def test_two():
    solution = Solution()
    result = solution.trap([4, 2, 0, 3, 2, 5])

    assert result == 9
