"""
https://leetcode.com/problems/largest-rectangle-in-histogram/description/?envType=company&envId=roblox&favoriteSlug=roblox-all

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4

Constraints:
1 <= heights.length <= 10^5
0 <= heights[i] <= 10^4
"""

from typing import List
from itertools import chain


class Solution:
    def largest_rectangle_area(self, heights: List[int]) -> int:
        stack: List[List[int]] = []
        result = 0

        for i, height in enumerate(chain([0], heights, [0])):
            while stack and stack[-1][1] > height:
                curr_height = stack.pop()[1]
                curr_width = i - stack[-1][0] - 1
                result = max(result, curr_height * curr_width)

            stack.append([i, height])

        return result


def test_one():
    solution = Solution()
    result = solution.largest_rectangle_area([2, 1, 5, 6, 2, 3])

    assert result == 10


def test_two():
    solution = Solution()
    result = solution.largest_rectangle_area([2, 4])

    assert result == 4
