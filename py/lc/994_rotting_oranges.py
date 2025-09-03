"""
https://leetcode.com/problems/rotting-oranges/description/?envType=company&envId=roblox&favoriteSlug=roblox-all

You are given an m x n grid where each cell can have one of three values:
0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""

from collections import deque
from typing import Deque, List, Tuple


class Solution:
    def oranges_rotting(self, grid: List[List[int]]) -> int:
        q: Deque[Tuple] = deque()

        fresh = 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        q.append((-1, -1))
        elapsed = -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        while q:
            r, c = q.popleft()
            if r == -1:
                elapsed += 1

                if q:
                    q.append((-1, -1))
            else:
                for dr, dc in directions:
                    temp_r = r + dr
                    temp_c = c + dc

                    if rows > temp_r >= 0 and cols > temp_c >= 0:
                        if grid[temp_r][temp_c] == 1:
                            grid[temp_r][temp_c] = 2
                            fresh -= 1
                            q.append((temp_r, temp_c))

        return elapsed if fresh == 0 else -1


def test_one():
    solution = Solution()
    result = solution.oranges_rotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])

    assert result == 4


def test_two():
    solution = Solution()
    result = solution.oranges_rotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]])

    assert result == -1


def test_three():
    solution = Solution()
    result = solution.oranges_rotting([[0, 2]])

    assert result == 0
