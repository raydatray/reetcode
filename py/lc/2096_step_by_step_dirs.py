"""
https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/description/?envType=company&envId=databricks&favoriteSlug=databricks-all

You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.

Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:

'L' means to go from a node to its left child node.
'R' means to go from a node to its right child node.
'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t.

Example 1:
Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
Output: "UURL"
Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.

Example 2:
Input: root = [2,1], startValue = 2, destValue = 1
Output: "L"
Explanation: The shortest path is: 2 → 1.

Constraints:
The number of nodes in the tree is n.
2 <= n <= 10^5
1 <= Node.val <= n
All the values in the tree are unique.
1 <= startValue, destValue <= n
startValue != destValue
"""

from __future__ import annotations
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


class Solution:
    def get_directions(
        self, root: Optional[TreeNode], start_val: int, dest_val: int
    ) -> str:
        def dfs(curr: Optional[TreeNode], target_val: int, path: List[str]) -> bool:
            if curr is None:
                return False

            if curr.val == target_val:
                return True

            path.append("L")
            if dfs(curr.left, target_val, path):
                return True
            path.pop()

            path.append("R")
            if dfs(curr.right, target_val, path):
                return True
            path.pop()

            return False

        start_path = []
        dfs(root, start_val, start_path)
        dest_path = []
        dfs(root, dest_val, dest_path)

        lca = 0
        while (
            lca < len(start_path)
            and lca < len(dest_path)
            and start_path[lca] == dest_path[lca]
        ):
            lca += 1

        result = "U" * (len(start_path) - lca) + "".join(dest_path[lca:])
        return result


def test_one():
    solution = Solution()
    root = TreeNode(5, TreeNode(1, TreeNode(3)), TreeNode(2, TreeNode(6), TreeNode(4)))

    result = solution.get_directions(root, 3, 6)

    assert result == "UURL"


def test_two():
    solution = Solution()
    root = TreeNode(2, TreeNode(1))

    result = solution.get_directions(root, 2, 1)

    assert result == "L"
