#  https://leetcode.com/problems/spiral-matrix/
#  Related Topics: Array
#  Difficulty: Medium


# Initial thoughts:
# We are going to read each border of a imaginary outline clockwise
# and move inward until there are no more outlines left.
# To keep track of the bounderies of our borders, we will have a variable
# for each boundary that we increment or decrement accordingly.
# To keep track of when we have reached the end of the spiral, we will
# simply track the number of elements that we have already read. When that
# number equls the number of the elements in the matrix, we are done.

# Time complexity: O(n) where n === number of elements in matrix
# Space complexity: O(n) where n === number of elements in matrix (that's
# for the results array. In some interpretations, this does not count as
# auxilliary space.)
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        top, bottom = 0, len(matrix)-1
        left, right = 0, len(matrix[0])-1

        n = 0
        result = []
        lenMatrix = len(matrix)*len(matrix[0])

        while True:
            # Top
            for i in range(left, right+1):
                result.append(matrix[top][i])
                n += 1
            top += 1
            if n >= lenMatrix:
                break

            # Right
            for i in range(top, bottom+1):
                result.append(matrix[i][right])
                n += 1
            right -= 1
            if n >= lenMatrix:
                break

            # Bottom
            for i in range(right, left-1, -1):
                result.append(matrix[bottom][i])
                n += 1
            bottom -= 1
            if n >= lenMatrix:
                break

            # Left
            for i in range(bottom, top-1, -1):
                result.append(matrix[i][left])
                n += 1
            left += 1
            if n >= lenMatrix:
                break

        return result
