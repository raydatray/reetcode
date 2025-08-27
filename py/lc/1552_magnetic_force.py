"""
https://leetcode.com/problems/magnetic-force-between-two-balls/description/?envType=company&envId=roblox&favoriteSlug=roblox-all

In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket.
Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.
Rick stated that magnetic force between two different balls at positions x and y is |x - y|.
Given the integer array position and the integer m. Return the required force.

Example 1:
Input: position = [1,2,3,4,7], m = 3
Output: 3
Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between ball pairs [3, 3, 6]. The minimum magnetic force is 3. We cannot achieve a larger minimum magnetic force than 3.

Example 2:
Input: position = [5,4,3,2,1,1000000000], m = 2
Output: 999999999
Explanation: We can use baskets 1 and 1000000000.

Constraints:
n == position.length
2 <= n <= 10^5
1 <= position[i] <= 10^9
All integers in position are distinct.
2 <= m <= position.length
"""

from typing import List


class Solution:
    def max_distance(self, position: List[int], m: int) -> int:
        position.sort()

        low = 1
        high = int(position[-1] / (m - 1.0)) + 1
        result = 0

        while low <= high:
            mid = low + (high - low) // 2
            if self._can_place(mid, position, m):
                result = mid
                low = mid + 1
            else:
                high = mid - 1

        return result

    def _can_place(self, gap: int, position: List[int], num_of_balls: int) -> bool:
        prev_pos = position[0]
        balls_placed = 1

        for i in range(1, len(position)):
            curr_pos = position[i]
            if curr_pos - prev_pos >= gap:
                balls_placed += 1
                prev_pos = curr_pos

            if balls_placed == num_of_balls:
                return True

        return False


def test_one():
    solution = Solution()
    assert solution.max_distance([1, 2, 3, 4, 7], 3) == 3


def test_two():
    solution = Solution()
    assert solution.max_distance([5, 4, 3, 2, 1, 1000000000], 2) == 999999999
