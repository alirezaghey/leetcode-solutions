from typing import List
from functools import lru_cache


class Solution:
    # Dp iterative approach
    # TC: O(n) 2 pass
    # SC: O(n)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [float("inf")]*(len(cost)+2)

        dp[0] = 0

        for i in range(len(cost)):
            dp[i+1] = min(dp[i+1], dp[i]+cost[i])
            dp[i+2] = min(dp[i+2], dp[i]+cost[i])

        res = min(dp[-1], dp[-2])

        dp = [float("inf")] * (len(cost)+2)
        dp[1] = 0

        for i in range(1, len(cost)):
            dp[i+1] = min(dp[i+1], dp[i]+cost[i])
            dp[i+2] = min(dp[i+2], dp[i]+cost[i])

        res = min(res, dp[-1], dp[-2])

        return res

    # DP memoized recursive approach
    # TC: O(n)
    # SC: O(n)
    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        @lru_cache(None)
        def dfs(idx):
            if idx >= len(cost):
                return 0

            return min(dfs(idx+1), dfs(idx+2))+cost[idx]

        return min(dfs(0), dfs(1))
