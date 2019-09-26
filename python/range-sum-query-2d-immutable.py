#  https://leetcode.com/problems/range-sum-query-2d-immutable/
#  Related Topics: Dynamic Programming
#  Difficulty: Medium


# Initial thoughts:
# The naive approach is to look at each and every element every time
# and sum them. This would have a Time Complexity of O(n) and a Space Complexity of O(1)

# Optimization:
# Using a Dynamic Programming approach, we can create a suplemental matrix where each element
# contains the sum of all the values before it in that specific row plus itself.
# Now to find the sum of the elements in a box in the matrix we need to add the sums for each
# row in that box.
# This is very similar to range-sum-query-immutable.py and its solution and will only add another
# dimension to the whole problem.
# Preprocessing will take up O(n) where n === matrix.width * matrix.heigth
# Lookup time for a box inside the matrix is O(matrix.height) since the sum of a row can be calculated
# in constant time.

# Time complexity: O(n) where n === matrix.width * matrix.heigth
# Space complexity: O(n) where n === matrix.width * matrix.heigth

from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self._matrix = matrix
        self._dp = self.preprocess()

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for i in range(row1, row2+1):
            sum += self._dp[i][col2+1] - self._dp[i][col1]
        return sum

    def preprocess(self) -> List[List[int]]:
        dp = [[0 for i in range(len(self._matrix[0])+1)]
              for j in range(len(self._matrix))]
        for i in range(len(self._matrix)):
            for j in range(len(self._matrix[0])):
                dp[i][j+1] = dp[i][j] + self._matrix[i][j]
        return dp

    def sumRegionNaive(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                sum += self._matrix[i][j]
        return sum


# Optimization:
# We could render the lookup time constant by storing the sum of the whole box before an element
# in the dp array. Then with some basic arithmetic we can calculate any box in the matrix.

# Time Complexity: O(n) where n === matrix.width * matrix.heigth
# Space Complexity: O(n) where n === matrix.width * matrix.heigth
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self._matrix = matrix
        self._dp = self.preprocess()

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self._dp[row2+1][col2+1] - self._dp[row1][col2+1] - self._dp[row2+1][col1] + self._dp[row1][col1]

    def preprocess(self):
        if len(self._matrix) == 0 or len(self._matrix[0]) == 0:
            return None
        dp = [[0 for i in range(len(self._matrix[0])+1)]
              for j in range(len(self._matrix)+1)]

        for i in range(len(self._matrix)):
            for j in range(len(self._matrix[0])):
                dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1] - \
                    dp[i][j] + self._matrix[i][j]
        return dp

        # Your NumMatrix object will be instantiated and called as such:
        # obj = NumMatrix(matrix)
        # param_1 = obj.sumRegion(row1,col1,row2,col2)
