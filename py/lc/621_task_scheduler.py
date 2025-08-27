"""
https://leetcode.com/problems/task-scheduler/description/?envType=company&envId=roblox&favoriteSlug=roblox-all

You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.
Return the minimum number of CPU intervals required to complete all tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

Example 2:
Input: tasks = ["A","C","A","B","D","B"], n = 1
Output: 6
Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:
Input: tasks = ["A","A","A", "B","B","B"], n = 3
Output: 10
Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.
There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

Constraints:
1 <= tasks.length <= 10^4
tasks[i] is an uppercase English letter.
0 <= n <= 100
"""

from typing import List


class Solution:
    def least_interval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        max_freq = 0
        num_of_max = 0

        for task in tasks:
            idx = ord(task) - ord("A")
            freq[idx] += 1

            if max_freq == freq[idx]:
                num_of_max += 1
            elif max_freq < freq[idx]:
                max_freq = freq[idx]
                num_of_max = 1

        cycle_count = max_freq - 1
        cycle_len = n - (num_of_max - 1)
        empty_slots = cycle_count * cycle_len
        available_tasks = len(tasks) - max_freq * num_of_max
        idles = max(0, empty_slots - available_tasks)

        return len(tasks) + idles


def test_one():
    solution = Solution()
    assert solution.least_interval(["A", "A", "A", "B", "B", "B"], 2) == 8


def test_two():
    solution = Solution()
    assert solution.least_interval(["A", "C", "A", "B", "D", "B"], 1) == 6


def test_three():
    solution = Solution()
    assert solution.least_interval(["A", "A", "A", "B", "B", "B"], 3) == 10
