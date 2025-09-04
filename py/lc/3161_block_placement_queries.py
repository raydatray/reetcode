"""
https://leetcode.com/problems/block-placement-queries/?envType=company&envId=roblox&favoriteSlug=roblox-all

There exists an infinite number line, with its origin at 0 and extending towards the positive x-axis.
You are given a 2D array queries, which contains two types of queries:
For a query of type 1, queries[i] = [1, x]. Build an obstacle at distance x from the origin. It is guaranteed that there is no obstacle at distance x when the query is asked.
For a query of type 2, queries[i] = [2, x, sz]. Check if it is possible to place a block of size sz anywhere in the range [0, x] on the line, such that the block entirely lies in the range [0, x]. A block cannot be placed if it intersects with any obstacle, but it may touch it. Note that you do not actually place the block. Queries are separate.
Return a boolean array results, where results[i] is true if you can place the block specified in the ith query of type 2, and false otherwise.

Example 1:
Input: queries = [[1,2],[2,3,3],[2,3,1],[2,2,2]]
Output: [false,true,true]
Explanation:
For query 0, place an obstacle at x = 2. A block of size at most 2 can be placed before x = 3.

Example 2:
Input: queries = [[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]
Output: [true,true,false]
Explanation:
Place an obstacle at x = 7 for query 0. A block of size at most 7 can be placed before x = 7.
Place an obstacle at x = 2 for query 2. Now, a block of size at most 5 can be placed before x = 7, and a block of size at most 2 before x = 2.

Constraints:
1 <= queries.length <= 15 * 10^4
2 <= queries[i].length <= 3
1 <= queries[i][0] <= 2
1 <= x, sz <= min(5 * 10^4, 3 * queries.length)
The input is generated such that for queries of type 1, no obstacle exists at distance x when the query is asked.
The input is generated such that there is at least one query of type 2.
"""

from itertools import pairwise
import math
from sortedcontainers import SortedList
from typing import List


class Solution:
    def get_results(self, queries: List[List[int]]) -> List[bool]:
        line = SortedList()
        end = min(5 * (10**4), len(queries) * 3)
        line.add(0)
        line.add(end)

        for query in queries:
            if query[0] == 1:
                x = query[1]
                line.add(x)

        gaps = SortedList()
        gaps.add((0, 0))
        curr = 0

        for start, end in pairwise(line):
            if (gap := end - start) > curr:
                gaps.add((end, gap))
                curr = gap

        result = []
        for query in reversed(queries):
            if query[0] == 1:
                x = query[1]
                idx = line.index(x)
                after = line[idx + 1]
                before = line[idx - 1]

                line.remove(x)

                gap = after - before  # type: ignore
                idx = gaps.bisect_left((x, 0))

                while idx < len(gaps) and gaps[idx][1] <= gap:
                    gaps.pop(idx)

                if gaps[idx - 1][1] < gap:
                    gaps.add((after, gap))
            elif query[0] == 2:
                _, x, sz = query
                idx = line.bisect_right(x)
                before = line[idx - 1]
                idx = gaps.bisect_right((before, math.inf)) - 1

                result.append((x - before) >= sz or gaps[idx][1] >= sz)  # type: ignore

        result.reverse()

        return result


def test_one():
    solution = Solution()
    result = solution.get_results([[1, 2], [2, 3, 3], [2, 3, 1], [2, 2, 2]])

    assert result == [False, True, True]


def test_two():
    solution = Solution()
    result = solution.get_results([[1, 7], [2, 7, 6], [1, 2], [2, 7, 5], [2, 7, 6]])

    assert result == [True, True, False]
