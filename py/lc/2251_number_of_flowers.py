"""
https://leetcode.com/problems/number-of-flowers-in-full-bloom/description/?envType=company&envId=databricks&favoriteSlug=databricks-all

You are given a 0-indexed 2D integer array flowers, where flowers[i] = [starti, endi] means the ith flower will be in full bloom from starti to endi (inclusive). You are also given a 0-indexed integer array people of size n, where people[i] is the time that the ith person will arrive to see the flowers.

Return an integer array answer of size n, where answer[i] is the number of flowers that are in full bloom when the ith person arrives.

Example 1:
Input: flowers = [[1,6],[3,7],[9,12],[4,13]], people = [2,3,7,11]
Output: [1,2,2,2]
Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
For each person, we return the number of flowers in full bloom during their arrival.

Example 2:
Input: flowers = [[1,10],[3,3]], people = [3,3,2]
Output: [2,2,1]
Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
For each person, we return the number of flowers in full bloom during their arrival.

Constraints:
1 <= flowers.length <= 5 * 10^4
flowers[i].length == 2
1 <= starti <= endi <= 10^9
1 <= people.length <= 5 * 10^4
1 <= people[i] <= 10^9
"""

import bisect
from typing import List


class Solution:
    def full_bloom_flowers(
        self, flowers: List[List[int]], people: List[int]
    ) -> List[int]:
        starts: List[int] = []
        ends: List[int] = []

        for start, end in flowers:
            starts.append(start)
            ends.append(end + 1)

        starts.sort()
        ends.sort()

        result = []
        for person in people:
            bloomed = bisect.bisect_right(starts, person)
            dead = bisect.bisect_right(ends, person)
            result.append(bloomed - dead)

        return result


def test_one():
    solution = Solution()
    result = solution.full_bloom_flowers(
        [[1, 6], [3, 7], [9, 12], [4, 13]], [2, 3, 7, 11]
    )

    assert result == [1, 2, 2, 2]


def test_two():
    solution = Solution()
    result = solution.full_bloom_flowers([[1, 10], [3, 3]], [3, 3, 2])

    assert result == [2, 2, 1]
