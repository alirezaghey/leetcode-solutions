from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        R, C = len(matrix), len(matrix[0])
        dp = [[0]*(C+1) for _ in range(R+1)]
        res = 0
        
        for r, c in ((r, c) for r in range(R) for c in range(C)):
            if matrix[r][c] == "1":
                dp[r+1][c+1] = min(dp[r][c], dp[r][c+1], dp[r+1][c])+1
                res = max(res, dp[r+1][c+1])
        
        return res**2