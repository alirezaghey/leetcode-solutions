#  https://leetcode.com/problems/spiral-matrix-ii/
#  Related Topics: Array
#  Difficulty: Medium


# Initial thoughts:
# We are going to write each border of an imaginary outline clockwise
# and move inward until there are no more outlines left.
# To keep track of the bounderies of our borders, we will have a variable
# for each boundary that we increment or decrement accordingly.
# To keep track of when we have reached the end of the spiral, we will
# simply track the number of elements that we have already read. When that
# number equals the number of the elements in the matrix, we are done.

# Time complexity: O(n^2) where n === length of a side of our square matrix
# Space complexity: O(n^2) where n === length of a side of our square matrix
# (that's for the results array. In some interpretations, this does not count as
# auxilliary space.)
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0:
            return []

        result = [[None]*n for _ in range(n)]
        count = 1
        left, right = 0, n-1
        top, bottom = 0, n-1
        lenMatrix = n**2

        while True:
            # Top
            for i in range(left, right+1):
                result[top][i] = count
                count += 1
            top += 1
            if count > lenMatrix:
                break

            # Left
            for i in range(top, bottom+1):
                result[i][right] = count
                count += 1
            right -= 1
            if count > lenMatrix:
                break

            # Bottom
            for i in range(right, left-1, -1):
                result[bottom][i] = count
                count += 1
            bottom -= 1
            if count > lenMatrix:
                break

            # Right
            for i in range(bottom, top-1, -1):
                result[i][left] = count
                count += 1
            left += 1
            if count > lenMatrix:
                break

        return result
