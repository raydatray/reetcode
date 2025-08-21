"""
https://leetcode.com/problems/count-submatrices-with-all-ones/description/?envType=daily-question&envId=2025-08-21

Given an m x n binary matrix mat, return the number of submatrices that have all ones.

Example 1:
Input: mat = [[1,0,1],[1,1,0],[1,1,0]]
Output: 13
Explanation:
There are 6 rectangles of side 1x1.
There are 2 rectangles of side 1x2.
There are 3 rectangles of side 2x1.
There is 1 rectangle of side 2x2.
There is 1 rectangle of side 3x1.
Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.

Example 2:
Input: mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
Output: 24
Explanation:
There are 8 rectangles of side 1x1.
There are 5 rectangles of side 1x2.
There are 2 rectangles of side 1x3.
There are 4 rectangles of side 2x1.
There are 2 rectangles of side 2x2.
There are 2 rectangles of side 3x1.
There is 1 rectangle of side 3x2.
Total number of rectangles = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24.

Constraints:
1 <= m, n <= 150
mat[i][j] is either 0 or 1.
"""

from typing import List


class Solution:
    def num_submat(self, mat: List[List[int]]) -> int:
        heights = [0 for _ in range(len(mat[0]))]
        result = 0

        for row in mat:
            for i, row_ele in enumerate(row):
                heights[i] = 0 if row_ele == 0 else heights[i] + 1

            stack = [[-1, 0, -1]]
            for i, height in enumerate(heights):
                while stack[-1][2] >= height:
                    stack.pop()

                j, prev, _ = stack[-1]
                curr = prev + (i - j) * height
                stack.append([i, curr, height])
                result += curr

        return result


def test_one():
    solution = Solution()
    result = solution.num_submat([[1, 0, 1], [1, 1, 0], [1, 1, 0]])

    assert result == 13


def test_two():
    solution = Solution()
    result = solution.num_submat([[0, 1, 1, 0], [0, 1, 1, 1], [1, 1, 1, 0]])

    assert result == 24
