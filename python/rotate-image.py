#  https://leetcode.com/problems/rotate-image/
#  Related Topics: Array
#  Difficulty: Medium


# Initial thoughts:
# Looking at the matrix in liers, we are going to swap elements in
# clockwise order while moving inward into the middle of the matrix

# Time Complexity: O(n) where n == the number of cells in our matrix
# Space Complexity: O(1)

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)-1
        for i in range(len(matrix)//2):
            for j in range(i, n-i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-j][i]
                matrix[n-j][i] = matrix[n-i][n-j]
                matrix[n-i][n-j] = matrix[j][n-i]
                matrix[j][n-i] = temp
