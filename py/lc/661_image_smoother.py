"""
https://leetcode.com/problems/image-smoother/description/?envType=company&envId=roblox&favoriteSlug=roblox-all

An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother).
If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).

Given an m x n integer matrix img representing the grayscale of an image, return the image after applying the smoother on each cell of it.

Example 1:
Input: img = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[0,0,0],[0,0,0],[0,0,0]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0

Example 2:
Input: img = [[100,200,100],[200,50,200],[100,200,100]]
Output: [[137,141,137],[141,138,141],[137,141,137]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137
For the points (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = floor(141.666667) = 141
For the point (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138

Constraints:
m == img.length
n == img[i].length
1 <= m, n <= 200
0 <= img[i][j] <= 255
"""

from typing import List


class Solution:
    def image_smoother(self, img: List[List[int]]) -> List[List[int]]:
        deltas = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]
        rows = len(img)
        cols = len(img[0])

        def helper(img: List[List[int]], r: int, c: int) -> int:
            total = img[r][c]
            count = 1

            for dr, dc in deltas:
                temp_r = r + dr
                temp_c = c + dc

                if rows > temp_r >= 0 and cols > temp_c >= 0:
                    total += img[temp_r][temp_c]
                    count += 1

            return total // count

        result = [[0 for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                result[r][c] = helper(img, r, c)

        return result


def test_one():
    solution = Solution()
    result = solution.image_smoother([[1, 1, 1], [1, 0, 1], [1, 1, 1]])

    assert result == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def test_two():
    solution = Solution()
    result = solution.image_smoother([[100, 200, 100], [200, 50, 200], [100, 200, 100]])

    assert result == [[137, 141, 137], [141, 138, 141], [137, 141, 137]]
