"""
https://leetcode.com/problems/design-a-leaderboard/description/?envType=company&envId=databricks&favoriteSlug=databricks-all

Design a Leaderboard class, which has 3 functions:

addScore(playerId, score): Update the leaderboard by adding score to the given player's score. If there is no player with such id in the leaderboard, add him to the leaderboard with the given score.
top(K): Return the score sum of the top K players.
reset(playerId): Reset the score of the player with the given id to 0 (in other words erase it from the leaderboard). It is guaranteed that the player was added to the leaderboard before calling this function.
Initially, the leaderboard is empty.

Example 1:
Input:
["Leaderboard","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","top"]
[[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]]
Output:
[null,null,null,null,null,null,73,null,null,null,141]

Explanation:
Leaderboard leaderboard = new Leaderboard ();
leaderboard.addScore(1,73);   // leaderboard = [[1,73]];
leaderboard.addScore(2,56);   // leaderboard = [[1,73],[2,56]];
leaderboard.addScore(3,39);   // leaderboard = [[1,73],[2,56],[3,39]];
leaderboard.addScore(4,51);   // leaderboard = [[1,73],[2,56],[3,39],[4,51]];
leaderboard.addScore(5,4);    // leaderboard = [[1,73],[2,56],[3,39],[4,51],[5,4]];
leaderboard.top(1);           // returns 73;
leaderboard.reset(1);         // leaderboard = [[2,56],[3,39],[4,51],[5,4]];
leaderboard.reset(2);         // leaderboard = [[3,39],[4,51],[5,4]];
leaderboard.addScore(2,51);   // leaderboard = [[2,51],[3,39],[4,51],[5,4]];
leaderboard.top(3);           // returns 141 = 51 + 51 + 39;


Constraints:
1 <= playerId, K <= 10000
It's guaranteed that K is less than or equal to the current number of players.
1 <= score <= 100
There will be at most 1000 function calls.
"""

import heapq
from collections import defaultdict
from typing import Dict


class Leaderboard:
    def __init__(self):
        self.players_to_scores: Dict[int, int] = defaultdict(int)

    def add_score(self, player_id: int, score: int):
        self.players_to_scores[player_id] += score

    def top(self, k: int) -> int:
        scores = [-value for value in self.players_to_scores.values()]

        heapq.heapify(scores)

        res = 0

        for _ in range(k):
            res += -heapq.heappop(scores)

        return res

    def reset(self, player_id: int):
        self.players_to_scores.pop(player_id)


def test_one():
    leaderboard = Leaderboard()

    leaderboard.add_score(1, 73)
    leaderboard.add_score(2, 56)
    leaderboard.add_score(3, 39)
    leaderboard.add_score(4, 51)
    leaderboard.add_score(5, 4)

    assert leaderboard.top(1) == 73

    leaderboard.reset(1)

    leaderboard.reset(2)

    leaderboard.add_score(2, 51)

    assert leaderboard.top(3) == 141
