"""
https://leetcode.com/problems/combination-sum/description/?envType=company&envId=citadel&favoriteSlug=citadel-all

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []


Constraints:
1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40
"""

from collections import defaultdict
from typing import Dict, List


class Solution:
    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        memo: Dict[int, List[List[int]]] = defaultdict(list)

        memo[0] = [[]]

        for candidate in candidates:
            for curr_target in range(candidate, target + 1):
                for combination in memo[curr_target - candidate]:
                    new_combination = combination + [candidate]
                    memo[curr_target].append(new_combination)

        return memo[target]


def test_one():
    solution = Solution()
    result = solution.combination_sum([2, 3, 6, 7], 7)

    assert result == [[2, 2, 3], [7]]


def test_two():
    solution = Solution()
    result = solution.combination_sum([2, 3, 5], 8)

    assert result == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]


def test_three():
    solution = Solution()
    result = solution.combination_sum([2], 1)

    assert result == []
