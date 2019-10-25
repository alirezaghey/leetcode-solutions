#  https://leetcode.com/problems/minimum-path-sum/
#  Related Topics: Array, Dynamic Programming
#  Difficulty: Medium


# Initial thoughts:
# We can look at the problem as a tree where each cell is a node in the tree
# that is connected to two other cells (one to its right and one to its bottom)
# We are looking for the minimum path sum that lead to a leaf node (all the leaf
# nodes are the bottom right cell in our matrix)
# In other words, we have to look at all the possible sums that lead to the bottom
# right cell and return the minimum.
# Since this problem has an overlapping substructure, we can avoid redundant calculations
# by using memoization. At each state if the data is available we are going to retrieve it,
# otherwise we are going to fill it.

# Time complexity: O(n) where n == number of cells in the grid
# Space complexity: O(n) where n == number of cells in the grid. In a worst case scenario,
# where our grid has only one row or one column, the recursive stack's depth will equal
# the number of cells in the grid. In addition, our memoization grid needs to havev as much
# cells as the original grid.

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not len(grid) or not len(grid[0]):
            return 0

        R, C = len(grid), len(grid[0])
        dp = [[None] * C for _ in range(R)]

        def dfs(row: int, col: int) -> int:
            if row == R-1 and col == C-1:
                return grid[row][col]

            if dp[row][col]:
                return dp[row][col]

            right = down = float('inf')

            if col < C-1:
                right = dfs(row, col+1)
            if row < R-1:
                down = dfs(row+1, col)

            dp[row][col] = grid[row][col]+min(right, down)
            return dp[row][col]

        return dfs(0, 0)


# Optimization:
# Using a dynamic programming approach, we can fill the grid in a tabular way always looking
# for how to reach the next cell with minimum costs and build on that calculation for calculating
# the minimum cost for reaching the next cell.

# Time complexity: O(n) where n == number of cells in the grid
# Space complexity: O(1)

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not len(grid) or not len(grid[0]):
            return 0

        R, C = len(grid), len(grid[0])

        for i in range(1, C):
            grid[0][i] += grid[0][i-1]

        for i in range(1, R):
            grid[i][0] += grid[i-1][0]

        for i in range(1, R):
            for j in range(1, C):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[-1][-1]
