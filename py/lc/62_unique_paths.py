"""
https://leetcode.com/problems/unique-paths/description/?envType=company&envId=roblox&favoriteSlug=roblox-all

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Constraints:
1 <= m, n <= 100
"""


class Solution:
    def unique_paths(self, m: int, n: int) -> int:
        moves_to_reach = [[1] * n for _ in range(m)]

        for r in range(1, m):
            for c in range(1, n):
                moves_to_reach[r][c] = (
                    moves_to_reach[r - 1][c] + moves_to_reach[r][c - 1]
                )

        return moves_to_reach[m - 1][n - 1]


def test_one():
    solution = Solution()
    assert solution.unique_paths(3, 7) == 28


def test_two():
    solution = Solution()
    assert solution.unique_paths(3, 2) == 3
