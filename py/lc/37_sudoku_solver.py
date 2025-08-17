"""
https://leetcode.com/problems/sudoku-solver/?envType=company&envId=citadel&favoriteSlug=citadel-all

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.


Example 1:
Input: board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
Output: [
    ["5","3","4","6","7","8","9","1","2"],
    ["6","7","2","1","9","5","3","4","8"],
    ["1","9","8","3","4","2","5","6","7"],
    ["8","5","9","7","6","1","4","2","3"],
    ["4","2","6","8","5","3","7","9","1"],
    ["7","1","3","9","2","4","8","5","6"],
    ["9","6","1","5","3","7","2","8","4"],
    ["2","8","7","4","1","9","6","3","5"],
    ["3","4","5","2","8","6","1","7","9"]
]
Explanation: The input board is shown above and the only valid solution is shown below:

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
"""

from collections import defaultdict
from typing import Dict, List


class Solution:
    def solve_sudoku(self, board: List[List[str]]):
        box_size = 3
        total_size = box_size * box_size

        rows: List[Dict[str, int]] = [defaultdict(int) for _ in range(total_size)]
        cols: List[Dict[str, int]] = [defaultdict(int) for _ in range(total_size)]
        boxes: List[Dict[str, int]] = [defaultdict(int) for _ in range(total_size)]

        def can_place(digit: str, row: int, col: int) -> bool:
            return not (
                digit in rows[row]
                or digit in cols[col]
                or digit in boxes[box_index(row, col)]
            )

        def place_digit(digit: str, row: int, col: int):
            rows[row][digit] += 1
            cols[col][digit] += 1
            boxes[box_index(row, col)][digit] += 1
            board[row][col] = digit

        def remove_digit(digit: str, row: int, col: int):
            rows[row][digit] -= 1
            cols[col][digit] -= 1
            boxes[box_index(row, col)][digit] -= 1

            if rows[row][digit] == 0:
                del rows[row][digit]

            if cols[col][digit] == 0:
                del cols[col][digit]

            if boxes[box_index(row, col)][digit] == 0:
                del boxes[box_index(row, col)][digit]

            board[row][col] = "."

        def backtrack(row: int, col: int) -> bool:
            if row == total_size:
                return True

            next_row, next_col = (
                (row, col + 1) if col < total_size - 1 else (row + 1, 0)
            )

            if board[row][col] != ".":
                return backtrack(next_row, next_col)

            for digit in range(1, 10):
                digit = str(digit)

                if can_place(digit, row, col):
                    place_digit(digit, row, col)

                    if backtrack(next_row, next_col):
                        return True

                    remove_digit(digit, row, col)

            return False

        def box_index(row: int, col: int) -> int:
            return (row // box_size) * box_size + col // box_size

        for i in range(total_size):
            for j in range(total_size):
                if board[i][j] != ".":
                    digit = board[i][j]
                    place_digit(digit, i, j)

        backtrack(0, 0)


def test_one():
    solution = Solution()
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    solution.solve_sudoku(board)

    assert board == [
        ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
        ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
        ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
        ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
        ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
        ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
        ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
        ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
        ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
    ]
