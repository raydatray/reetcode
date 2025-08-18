"""
https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/description/?envType=company&envId=databricks&favoriteSlug=databricks-all

You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.

Example 1:
Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
Explanation:
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].

Example 2:
Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
Output: [1,1]

Constraints:
nums.length == k
1 <= k <= 3500
1 <= nums[i].length <= 50
-10^5 <= nums[i][j] <= 10^5
nums[i] is sorted in non-decreasing order.
"""

from collections import defaultdict
from typing import Dict, List, Tuple


class Solution:
    def smallest_range(self, nums: List[List[int]]) -> List[int]:
        all_lists: List[Tuple] = []

        for i in range(len(nums)):
            for num in nums[i]:
                all_lists.append((num, i))

        all_lists.sort()

        freq: Dict[int, int] = defaultdict(int)
        left, count = 0, 0
        start, end = 0, 10000000

        for right in range(len(all_lists)):
            freq[all_lists[right][1]] += 1
            if freq[all_lists[right][1]] == 1:
                count += 1

            while count == len(nums):
                curr_range = all_lists[right][0] - all_lists[left][0]
                if curr_range < end - start:
                    start = all_lists[left][0]
                    end = all_lists[right][0]

                freq[all_lists[left][1]] -= 1
                if freq[all_lists[left][1]] == 0:
                    count -= 1
                left += 1

        return [start, end]


def test_one():
    solution = Solution()
    result = solution.smallest_range(
        [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
    )

    assert result == [20, 24]


def test_two():
    solution = Solution()
    result = solution.smallest_range([[1, 2, 3], [1, 2, 3], [1, 2, 3]])

    assert result == [1, 1]
