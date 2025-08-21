"""
There are n memory blocks, and the size of the iᵗʰ block is given by the array element memoryBlocks[i], where 0 ≤ i < n.

The following operation can be performed on memoryBlocks one time:
An index i can be selected. The size of memoryBlocks[i] can be increased by 1 unit, but only if memoryBlocks[i] is less than n. The smallest integer not present in memoryBlocks after any number of operations is called a Valid Size or the MEX (minimum excluded value).
The task is to return an array of all possible Valid Sizes that can be achieved using memoryBlocks, sorted in ascending order.

Note:
The MEX of memoryBlocks is the smallest non-negative integer not present in the array.

Example
Given n = 3,
memoryBlocks = [0, 3, 4]
If no operation on memoryBlocks is performed, then the Valid Size is 1.
If x = 0, increase the size of memoryBlocks[x] by 1, then the Valid Size is 0.
There are only two possible Valid Sizes. Hence, the answer is [0, 1], when sorted in ascending order.

Function Description
Complete the function findValidSizes in the editor below.

Function Parameters
int[] memoryBlocks: the memory block sizes
Returns
int[]: all possible Valid Sizes that can be allocated using memoryBlocks, sorted in ascending order

Constraints
1 ≤ n ≤ 10⁵
0 ≤ memoryBlocks[i] < n
"""

from typing import List


class Solution:
    def find_valid_sizes(self, memory_blocks: List[int]) -> List[int]:
        memory_blocks.sort()

        curr = 0
        result = []

        for block in memory_blocks:
            if block > curr:
                break

            result.append(curr)
            curr += 1

        result.append(curr)

        return result


def test_one():
    solution = Solution()
    result = solution.find_valid_sizes([0, 3, 4])

    assert result == [0, 1]


def test_two():
    solution = Solution()
    result = solution.find_valid_sizes([0, 1, 2, 2, 3, 3, 4, 4])

    assert result == [0, 1, 2, 3, 4, 5, 6, 7, 8]
