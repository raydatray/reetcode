"""
https://leetcode.com/problems/spiral-matrix/description/?envType=company&envId=roblox&favoriteSlug=roblox-all

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""

from typing import List


class Solution:
    def spiral_order(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        r, c = 0, -1
        direction = 1

        result = []
        while rows * cols > 0:
            for _ in range(cols):
                c += direction
                result.append(matrix[r][c])
            rows -= 1
            for _ in range(rows):
                r += direction
                result.append(matrix[r][c])
            cols -= 1
            direction *= -1

        return result


def test_one():
    solution = Solution()
    result = solution.spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    assert result == [1, 2, 3, 6, 9, 8, 7, 4, 5]


def test_two():
    solution = Solution()
    result = solution.spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

    assert result == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
