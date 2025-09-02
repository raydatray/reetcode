"""
https://leetcode.com/problems/minimum-number-of-frogs-croaking/description/?envType=company&envId=roblox&favoriteSlug=roblox-all

You are given the string croakOfFrogs, which represents a combination of the string "croak" from different frogs, that is, multiple frogs can croak at the same time, so multiple "croak" are mixed.
Return the minimum number of different frogs to finish all the croaks in the given string.
A valid "croak" means a frog is printing five letters 'c', 'r', 'o', 'a', and 'k' sequentially. The frogs have to print all five letters to finish a croak. If the given string is not a combination of a valid "croak" return -1.

Example 1:
Input: croakOfFrogs = "croakcroak"
Output: 1
Explanation: One frog yelling "croak" twice.

Example 2:
Input: croakOfFrogs = "crcoakroak"
Output: 2
Explanation: The minimum number of frogs is two.
The first frog could yell "crcoakroak".
The second frog could yell later "crcoakroak".

Example 3:
Input: croakOfFrogs = "croakcrook"
Output: -1
Explanation: The given string is an invalid combination of "croak" from different frogs.

Constraints:
1 <= croakOfFrogs.length <= 10^5
croakOfFrogs is either 'c', 'r', 'o', 'a', or 'k'.
"""


class Solution:
    def min_num_of_frogs(self, croak_of_frogs: str) -> int:
        result = 0
        frogs = 0
        croak = [0 for _ in range(5)]

        for ch in croak_of_frogs:
            idx = "croak".index(ch)
            if idx == -1:
                return -1

            croak[idx] += 1

            if idx == 0:
                frogs += 1
                result = max(result, frogs)
            else:
                croak[idx - 1] -= 1
                if croak[idx - 1] < 0:
                    return -1
                if idx == 4:
                    frogs -= 1

        return result if frogs == 0 else -1


def test_one():
    solution = Solution()
    result = solution.min_num_of_frogs("croakcroak")

    assert result == 1


def test_two():
    solution = Solution()
    result = solution.min_num_of_frogs("crcoakroak")

    assert result == 2


def test_three():
    solution = Solution()
    result = solution.min_num_of_frogs("croakcrook")

    assert result == -1
