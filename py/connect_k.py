"""
Connect k

Citadel R1, Jane Street R1

Let’s design a game, where the game board is infinite on the x axis in both the positive and negative directions and infinite on the positive y axis.
Each turn players place a piece at a given x coordinate and the piece is placed at (x,0) and all other pieces in that column are pushed up.

Follow up1: let’s implement a way to win, where we are initially given number k, and a player can win if they have k consecutive pieces vertically or horizontally
Follow up2: lets allow players to win id they have k consecutive pieces diagonally as well
"""

import pytest
from collections import deque
from enum import Enum
from typing import Dict, Deque


class Player(Enum):
    RED = 1
    BLUE = 2


class Game:
    def __init__(self, k: int):
        self.board: Dict[int, Deque[Player]] = {}
        self.k = k

    def make_move(self, player: Player, col: int) -> bool:
        self.board.setdefault(col, deque()).appendleft(player)

        return (
            self._check_vertical_win(player, col)
            or self._check_horizontal_win(player, col)
            or self._check_diagonal_win(player, col)
        )

    def check_win(self, player: Player, col: int) -> bool:
        if self._check_vertical_win(player, col):
            return True

        if self._check_horizontal_win(player, col):
            return True

        return False

    def _check_vertical_win(self, player: Player, col: int) -> bool:
        if col not in self.board:
            return False

        return all(self._get_piece_at(col, row) == player for row in range(self.k))

    def _check_horizontal_win(self, player: Player, col: int) -> bool:
        if col not in self.board or not self.board[col]:
            return False

        for row in range(len(self.board[col])):
            if self._check_row(player, col, row):
                return True

        return False

    def _check_row(self, player: Player, col: int, row: int) -> bool:
        consecutive = 0

        left_col = col - self.k + 1
        right_col = col + self.k - 1

        for check_col in range(left_col, right_col + 1):
            piece = self._get_piece_at(check_col, row)

            if piece == player:
                consecutive += 1
                if consecutive >= self.k:
                    return True
            else:
                consecutive = 0

        return False

    def _check_diagonal_win(self, player: Player, col: int) -> bool:
        if col not in self.board or not self.board[col]:
            return False

        for row in range(len(self.board[col])):
            if self._check_diag(player, col, row, 1, 1) or self._check_diag(
                player, col, row, 1, -1
            ):
                return True

        return False

    def _check_diag(
        self, player: Player, col: int, row: int, col_dir: int, row_dir: int
    ) -> bool:
        consecutive = 0

        for i in range(-(self.k - 1), self.k):
            check_col = col + i * col_dir
            check_row = row + i * row_dir

            piece = self._get_piece_at(check_col, check_row)

            if piece == player:
                consecutive += 1
                if consecutive >= self.k:
                    return True
            else:
                consecutive = 0

        return False

    def _get_piece_at(self, col: int, row: int) -> Player | None:
        if col not in self.board or row < 0:
            return None

        col_pieces = list(self.board[col])
        if row >= len(col_pieces):
            return None

        return col_pieces[row]


@pytest.fixture
def game_ready_for_vertical_win() -> Game:
    """Board where RED can win vertically by placing at column 0"""
    game = Game(3)
    game.board[0] = deque([Player.RED, Player.RED])
    game.board[1] = deque([Player.BLUE])
    game.board[2] = deque([Player.BLUE, Player.RED])
    return game


@pytest.fixture
def game_ready_for_horizontal_win() -> Game:
    """Board where RED can win horizontally by placing at column 2"""
    game = Game(3)
    game.board[0] = deque([Player.RED])
    game.board[1] = deque([Player.RED])
    game.board[2] = deque([Player.BLUE])
    return game


@pytest.fixture
def game_ready_for_horizontal_win_upper_row() -> Game:
    """Board where RED can win horizontally at row 1 by placing at column 1"""
    game = Game(3)
    game.board[0] = deque([Player.BLUE, Player.RED])
    game.board[1] = deque([Player.RED])
    game.board[2] = deque([Player.BLUE, Player.RED])
    return game


@pytest.fixture
def game_ready_for_diagonal_win_up_right() -> Game:
    """Board where RED can win diagonally (↗) by placing at column 2"""
    game = Game(3)
    game.board[0] = deque([Player.RED])
    game.board[1] = deque([Player.BLUE, Player.RED])
    game.board[2] = deque([Player.BLUE, Player.RED])

    return game


@pytest.fixture
def game_ready_for_diagonal_win_down_right() -> Game:
    """Board where BLUE can win diagonally (↘) by placing at column 0"""
    game = Game(3)
    game.board[0] = deque([Player.RED, Player.BLUE])
    game.board[1] = deque([Player.RED, Player.BLUE])
    game.board[2] = deque([Player.BLUE])

    return game


def test_make_move():
    game = Game(2)
    result = game.make_move(Player.RED, 0)

    assert not result
    assert 0 in game.board
    assert len(game.board[0]) == 1
    assert game.board[0][0] == Player.RED


def test_vertical_win(game_ready_for_vertical_win):
    assert game_ready_for_vertical_win.make_move(Player.RED, 0)


def test_horizontal_win(game_ready_for_horizontal_win):
    assert game_ready_for_horizontal_win.make_move(Player.RED, 2)


def test_horizontal_win_upper_row(game_ready_for_horizontal_win_upper_row):
    assert game_ready_for_horizontal_win_upper_row.make_move(Player.RED, 1)


def test_diagonal_win_up_right(game_ready_for_diagonal_win_up_right):
    assert game_ready_for_diagonal_win_up_right.make_move(Player.RED, 2)


def test_diagonal_win_down_right(game_ready_for_diagonal_win_down_right):
    assert game_ready_for_diagonal_win_down_right.make_move(Player.BLUE, 0)
