"""
https://leetcode.com/problems/closest-leaf-in-a-binary-tree/description/?envType=company&envId=databricks&favoriteSlug=databricks-all

Given the root of a binary tree where every node has a unique value and a target integer k, return the value of the nearest leaf node to the target k in the tree.

Nearest to a leaf means the least number of edges traveled on the binary tree to reach any leaf of the tree. Also, a node is called a leaf if it has no children.

Example 1:
Input: root = [1,3,2], k = 1
Output: 2
Explanation: Either 2 or 3 is the nearest leaf node to the target of 1.

Example 2:
Input: root = [1], k = 1
Output: 1
Explanation: The nearest leaf node is the root node itself.

Example 3:
Input: root = [1,2,3,4,null,null,null,5,null,6], k = 2
Output: 3
Explanation: The leaf node with value 3 (and not the leaf node with value 6) is nearest to the node with value 2.

Constraints:
The number of nodes in the tree is in the range [1, 1000].
1 <= Node.val <= 1000
All the values of the tree are unique.
There exist some node in the tree where Node.val == k.
"""

from __future__ import annotations
from collections import deque, defaultdict
from typing import Deque, Dict, List, Optional, Set


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


class Solution:
    def find_closest_leaf(self, root: Optional[TreeNode], k: int) -> int:
        graph: Dict[Optional[TreeNode], List[Optional[TreeNode]]] = defaultdict(list)

        def dfs(node: Optional[TreeNode], parent: Optional[TreeNode]):
            if node:
                graph[node].append(parent)
                graph[parent].append(node)
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root, None)

        queue: Deque[Optional[TreeNode]] = deque(
            node for node in graph if node and node.val == k
        )
        seen: Set[Optional[TreeNode]] = set(queue)

        while queue:
            node = queue.popleft()
            if node:
                if len(graph[node]) <= 1:
                    return node.val
                for neighbor in graph[node]:
                    if neighbor and neighbor not in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)

        return 0


def test_one():
    solution = Solution()
    result = solution.find_closest_leaf(TreeNode(1, TreeNode(3), TreeNode(2)), 1)

    assert result == 2


def test_two():
    solution = Solution()
    result = solution.find_closest_leaf(TreeNode(1), 1)

    assert result == 1


def test_three():
    solution = Solution()
    result = solution.find_closest_leaf(
        TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(5, TreeNode(6)))), TreeNode(3)), 2
    )

    assert result == 3
