"""
https://leetcode.com/problems/median-of-two-sorted-arrays/description/?envType=company&envId=citadel&favoriteSlug=citadel-all

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10^6 <= nums1[i], nums2[i] <= 10^6
"""

from typing import List


class Solution:
    def find_median_of_two_sorted_arrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        m, n = len(nums1), len(nums2)
        total = m + n
        target = total // 2

        p1, p2 = 0, 0
        prev, curr = 0, 0

        for _ in range(target + 1):
            prev = curr
            if p1 < m and (p2 >= n or nums1[p1] <= nums2[p2]):
                curr = nums1[p1]
                p1 += 1
            else:
                curr = nums2[p2]
                p2 += 1

        return curr if total % 2 else (curr + prev) / 2


def test_one():
    solution = Solution()
    result = solution.find_median_of_two_sorted_arrays([1, 3], [2])

    assert result == 2.0


def test_two():
    solution = Solution()
    result = solution.find_median_of_two_sorted_arrays([1, 2], [3, 4])

    assert result == 2.5
