from functools import cache

class Solution:
    # iterative solution
    # TC: O(n)
    # SC: O(1)
    def numTilings(self, n: int) -> int:
        dp = [1,1,2]
        if n <= 2:
            return dp[n]
        MOD = 1_000_000_007
        
        for _ in range(2, n):
            third, second, first = dp
            dp[0], dp[1], dp[2] = second, first, (2*first+third)% MOD
        return dp[-1]
        
        
    # recursive memoized solution
    # TC: O(n)
    # SC: O(n) for the recursive call stack and memoization
    def numTilings2(self, n: int) -> int:
        MOD = 1_000_000_007
        @cache
        def calc(n):
            if n == 0:
                return 1
            if n <= 2:
                return n
            
            return (2*calc(n-1)+calc(n-3)) % MOD
        
        return calc(n)