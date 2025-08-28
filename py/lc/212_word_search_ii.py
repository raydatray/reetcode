"""
https://leetcode.com/problems/word-search-ii/description/?envType=company&envId=roblox&favoriteSlug=roblox-all

Given an m x n board of characters and a list of strings words, return all words on the board.
Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once in a word.

Example 1:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []

Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 10^4
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
"""

from typing import Dict, List


class Solution:
    def find_words(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        trie = {}  # recursive type Trie: Dict[str, Union[Trie, str]]
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node["$"] = word

        result = []

        def _backtrack(r: int, c: int, node: Dict):
            letter = board[r][c]
            parent = node

            if letter in node:
                board[r][c] = "#"
                node = node[letter]
                if "$" in node:
                    result.append(node["$"])
                    del node["$"]

                directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                for dr, dc in directions:
                    if 0 <= r + dr < rows and 0 <= c + dc < cols:
                        _backtrack(r + dr, c + dc, node)

                board[r][c] = letter
                if not node:
                    parent.pop(letter)

        for r in range(rows):
            for c in range(cols):
                _backtrack(r, c, trie)

        return result


def test_one():
    solution = Solution()
    result = solution.find_words(
        [
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"],
        ],
        ["oath", "pea", "eat", "rain"],
    )

    assert sorted(result) == ["eat", "oath"]


def test_two():
    solution = Solution()
    result = solution.find_words([["a", "b"], ["c", "d"]], ["abcb"])

    assert result == []
