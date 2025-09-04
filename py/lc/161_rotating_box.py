"""
https://leetcode.com/problems/rotating-the-box/description/?envType=company&envId=roblox&favoriteSlug=roblox-all

You are given an m x n matrix of characters boxGrid representing a side-view of a box. Each cell of the box is one of the following:
A stone '#'
A stationary obstacle '*'
Empty '.'
The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box.
Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.
It is guaranteed that each stone in boxGrid rests on an obstacle, another stone, or the bottom of the box
Return an n x m matrix representing the box after the rotation described above.

Example 1:
Input: boxGrid = [["#",".","#"]]
Output: [["."],
         ["#"],
         ["#"]]

Example 2:
Input: boxGrid = [["#",".","*","."],
              ["#","#","*","."]]
Output: [["#","."],
         ["#","#"],
         ["*","*"],
         [".","."]]

Example 3:
Input: boxGrid = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]
Output: [[".","#","#"],
         [".","#","#"],
         ["#","#","*"],
         ["#","*","."],
         ["#",".","*"],
         ["#",".","."]]

Constraints:
m == boxGrid.length
n == boxGrid[i].length
1 <= m, n <= 500
boxGrid[i][j] is either '#', '*', or '.'.
"""

from typing import List


class Solution:
    def rotate_the_box(self, box_grid: List[List[str]]) -> List[List[str]]:
        orig_rows, orig_cols = len(box_grid), len(box_grid[0])
        result = [[" " for _ in range(orig_rows)] for _ in range(orig_cols)]

        for r in range(orig_rows):
            for c in range(orig_cols):
                result[c][orig_rows - r - 1] = box_grid[r][c]

        new_rows, new_cols = orig_cols, orig_rows

        for c in range(new_cols):
            lowest_empty_cell = new_rows - 1
            for r in reversed(range(new_rows)):
                if result[r][c] == "#":
                    result[r][c] = "."
                    result[lowest_empty_cell][c] = "#"
                    lowest_empty_cell -= 1
                if result[r][c] == "*":
                    lowest_empty_cell = r - 1

        return result


def test_one():
    solution = Solution()
    result = solution.rotate_the_box([["#", ".", "#"]])

    assert result == [["."], ["#"], ["#"]]


def test_two():
    solution = Solution()
    result = solution.rotate_the_box([["#", ".", "*", "."], ["#", "#", "*", "."]])

    assert result == [["#", "."], ["#", "#"], ["*", "*"], [".", "."]]


def test_three():
    solution = Solution()
    result = solution.rotate_the_box(
        [
            ["#", "#", "*", ".", "*", "."],
            ["#", "#", "#", "*", ".", "."],
            ["#", "#", "#", ".", "#", "."],
        ]
    )

    assert result == [
        [".", "#", "#"],
        [".", "#", "#"],
        ["#", "#", "*"],
        ["#", "*", "."],
        ["#", ".", "*"],
        ["#", ".", "."],
    ]
