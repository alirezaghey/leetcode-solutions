class Solution:
    # TC: O(n)
    # SC: O(1)
    def fib(self, n: int) -> int:
        dp = [0, 1]

        if n < 2:
            return dp[n]

        for _ in range(n-1):
            dp[0], dp[1] = dp[1], dp[0]+dp[1]

        return dp[1]
