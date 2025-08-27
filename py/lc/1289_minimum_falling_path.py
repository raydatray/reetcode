"""
https://leetcode.com/problems/minimum-falling-path-sum-ii/description/?envType=company&envId=roblox&favoriteSlug=roblox-all

Given an n x n integer matrix grid, return the minimum sum of a falling path with non-zero shifts.

A falling path with non-zero shifts is a choice of exactly one element from each row of grid such that no two elements chosen in adjacent rows are in the same column.

Example 1:
Input: grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
Output: 13
Explanation:
The possible falling paths are:
[1,5,9], [1,5,7], [1,6,7], [1,6,8],
[2,4,8], [2,4,9], [2,6,7], [2,6,8],
[3,4,8], [3,4,9], [3,5,7], [3,5,9]
The falling path with the smallest sum is [1,5,7], so the answer is 13.

Example 2:
Input: grid = [[7]]
Output: 7

Constraints:
n == grid.length == grid[i].length
1 <= n <= 200
-99 <= grid[i][j] <= 99
"""

from typing import Optional, List


class Solution:
    def min_falling_path_sum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        memo = [[float("inf")] * n for _ in range(n)]

        for col in range(n):
            memo[n - 1][col] = grid[n - 1][col]

        for row in range(n - 2, -1, -1):
            for col in range(n):
                next_minimum = float("inf")
                for next_row_col in range(n):
                    if next_row_col != col:
                        next_minimum = min(next_minimum, memo[row + 1][next_row_col])

                memo[row][col] = grid[row][col] + next_minimum

        result = float("inf")
        for col in range(n):
            result = min(result, memo[0][col])

        return int(result)

    def min_falling_path_sum_optimal(self, grid: List[List[int]]) -> int:
        n = len(grid)

        next_min_col: Optional[int] = None
        next_min_col_2: Optional[int] = None

        next_min_val: Optional[int] = None
        next_min_val_2: Optional[int] = None

        for col in range(n):
            if next_min_val is None or grid[n - 1][col] <= next_min_val:
                next_min_val_2 = next_min_val
                next_min_col_2 = next_min_col

                next_min_val = grid[n - 1][col]
                next_min_col = col
            elif next_min_val_2 is None or grid[n - 1][col] <= next_min_val_2:
                next_min_val_2 = grid[n - 1][col]
                next_min_col_2 = col

        for row in range(n - 2, -1, -1):
            min_col: Optional[int] = None
            min_col_2: Optional[int] = None

            min_val: Optional[int] = None
            min_val_2: Optional[int] = None

            for col in range(n):
                # this is spaghetti and u should fix it
                assert next_min_col is not None
                assert next_min_val is not None
                assert next_min_val_2 is not None
                assert col is not None

                if col != next_min_col:
                    value = grid[row][col] + next_min_val
                else:
                    value = grid[row][col] + next_min_val_2

                if min_val is None or value <= min_val:
                    min_val_2 = min_val
                    min_col_2 = min_col
                    min_val = value
                    min_col = col
                elif min_val_2 is None or value <= min_val_2:
                    min_val_2 = value
                    min_col_2 = col

            next_min_col = min_col
            next_min_col_2 = min_col_2
            next_min_val = min_val
            next_min_val_2 = min_val_2

        assert next_min_val is not None
        return next_min_val


def test_one():
    solution = Solution()

    assert solution.min_falling_path_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 13
    assert (
        solution.min_falling_path_sum_optimal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 13
    )


def test_two():
    solution = Solution()

    assert solution.min_falling_path_sum([[7]]) == 7
    assert solution.min_falling_path_sum_optimal([[7]]) == 7
