class Solution:
    def numTrees(self, n: int) -> int:
        if n < 3: return n
        dp = [1, 1, 2]
        
        for i in range(3, n+1):
            curr = 0
            for j in range(1, i+1):
                curr += dp[j-1]*dp[i-j]
            dp.append(curr)
        return dp[-1]