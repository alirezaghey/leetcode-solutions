from typing import List

class Solution:
    # bottom up itetrative solution
    # Time complexity: R * C^2 where R is the number of rows and C the number of columns of the grid
    # Space complexity: C^2 (we only need to look back one row)
    def cherryPickup(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        dp =  [[grid[-1][i] if i == j else grid[-1][i] + grid[-1][j] for i in range(C)] for j in range(C)]
        
        for r in range(R-2, -1, -1):
            new_dp = [[0]*C for _ in range(C)]
            for i, j in ((i, j) for i in range(C) for j in range(C)):
                new_dp[i][j] = max(dp[ni][nj] for ni, nj in ((i+ii, j+jj) for ii in range(-1,2) for jj in range(-1,2)) if 0 <= ni < C and 0 <= nj < C)

                new_dp[i][j] += grid[r][i] if i == j else (grid[r][i] + grid[r][j])
            dp = new_dp
        return dp[0][C-1]
                
    # Top down recursive solution
    # Time complexity: O(r * c^2) where r is the number of rows and c the number of columns of the grid
    # Space complexity: O(r * c^2)
    def cherryPickup2(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        
        def dfs(r, c1, c2, memo):
            if r >= R:
                return 0
            if not(0 <= c1 < C) or not(0 <= c2 < C):
                return float("-inf")
            
            if (r, c1, c2) in memo:
                return memo[(r, c1, c2)]
            
            memo[(r, c1, c2)] = (
                max(dfs(r+1, c1+i, c2+j, memo) for i in range(-1, 2) for j in range(-1, 2)) +
                (grid[r][c1] if c1 == c2 else grid[r][c1] + grid[r][c2])
            )
            return memo[(r, c1, c2)]
        
        return dfs(0, 0, len(grid[0])-1, {})
        