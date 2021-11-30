from typing import List

class Solution:
    # Approach:
    # Create dp where dp[i][j] is the sum of continues 1s to the left in row i including for j itself
    # For each column of the dp, for each row, look for continues rows without zero, take their min times the count of rows
    # That's the maximum area we can achieve
    # Note that we need to start at each row once
    # Also, we can break if we find a row that is zero
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
            R = len(matrix)
            if R == 0: return 0
            C = len(matrix[0])
            
            dp = [[0]*C for _ in range(R)]
            
            for r in range(R):
                for c in range(C):
                    if matrix[r][c] == "0": continue
                    dp[r][c] = 1 + (dp[r][c-1] if c > 0 else 0)
                    
            best = 0
            for c in range(C):
                for r in range(R):
                    curr = count = 0
                    for r1 in range(r, R):
                        if curr == 0:
                            if dp[r1][c] == 0: break
                            else:
                                curr = dp[r1][c]
                                count = 1
                                best = max(best, curr)
                        else:
                            if dp[r1][c] == 0:
                                curr = count = 0
                                continue
                            else:
                                best = max(best, dp[r1][c])
                                curr = min(curr, dp[r1][c])
                                count += 1
                                best = max(best, count*curr)
            return best
 