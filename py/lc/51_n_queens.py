"""
https://leetcode.com/problems/n-queens/description/?envType=company&envId=citadel&favoriteSlug=citadel-all

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:
Input: n = 1
Output: [["Q"]]

Constraints:
1 <= n <= 9
"""

from typing import List, Set


class Solution:
    def solve_n_queens(self, n: int) -> List[List[str]]:
        def create_board(state: List[List[str]]) -> List[str]:
            board: List[str] = []

            for row in state:
                board.append("".join(row))

            return board

        def backtrack(
            state: List[List[str]],
            row: int,
            cols: Set[int],
            l_diags: Set[int],
            r_diags: Set[int],
        ):
            if row == n:
                ans.append(create_board(state))
                return

            for col in range(n):
                curr_l_diag = row - col
                curr_r_diag = row + col

                if col in cols or curr_l_diag in l_diags or curr_r_diag in r_diags:
                    continue

                cols.add(col)
                l_diags.add(curr_l_diag)
                r_diags.add(curr_r_diag)
                state[row][col] = "Q"

                backtrack(state, row + 1, cols, l_diags, r_diags)

                cols.remove(col)
                l_diags.remove(curr_l_diag)
                r_diags.remove(curr_r_diag)
                state[row][col] = "."

        ans: List[List[str]] = []
        empty_board = [["."] * n for _ in range(n)]
        backtrack(empty_board, 0, set(), set(), set())

        return ans


def test_one():
    solution = Solution()
    result = solution.solve_n_queens(4)

    assert result == [
        [".Q..", "...Q", "Q...", "..Q."],
        ["..Q.", "Q...", "...Q", ".Q.."],
    ]


def test_two():
    solution = Solution()
    result = solution.solve_n_queens(1)

    assert result == [["Q"]]
