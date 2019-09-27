#  https://leetcode.com/problems/pascals-triangle-ii/
#  Related Topics: Array
#  Difficulty: Easy


# Initial thoughts:
# The naive solution is to handle this problem like with did Pascal's Triangle where we create a two dimensional array
# with the values of Pascal's triangle up to the row that we need to return and then return the last row.

# Optimization:
# Since we only need the last row, we can have a one dimensional array that initially holds the first row of
# Pascal's triangle and build uppon it by changing the values in place. This way we will decrease the space complexity
# by a factor of n.

# Time complexity: O(n^2) where n === index of the required row
# Space complexity: O(n) where n === index of the required row
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]
        for i in range(1, rowIndex+1):
            prev = result[0]
            for j in range(1, len(result)):
                curr = result[j]
                result[j] = curr+prev
                prev = curr
            result.append(1)
        return result
