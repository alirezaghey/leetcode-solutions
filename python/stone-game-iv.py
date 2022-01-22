from functools import cache
import math

class Solution:
    # Time complexity: O(sqrt(n) * n)
    # Space complexity: O(n)
    # Iterative bottom up
    # Note: Running the inner loop in reverse produces consistent shorter times
    # This must be due to the fact that False value tend to be more at larger numbers
    # I still don't have the intuition for why that is though, in terms of the game play
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n+1)
        
        for i in range(1, n+1):
            dp[i] = not all(dp[i - j**2] for j in range(math.floor(i**0.5), 0, -1))
        return dp[-1]
    
    
    # Time complexity: O(sqrt(n) * n)
    # Space complexity: O(n)
    # Iterative bottom up solution
    def winnerSquareGame2(self, n: int) -> bool:
        dp = [False]
        
        for i in range(1, n+1):
            dp.append(not all(dp[i - j**2] for j in range(1, math.floor(i**(1/2))+1)))
        
        return dp[-1]
    
    # Time complexity: O(sqrt(n) * n)
    # Space complexity: O(n)
    # Recursive top down memoized approach
    # None: Optimized compared to the further below algorithm
    def winnerSquareGame3(self, n: int) -> bool:
        @cache
        def solve(n):
            if n == 0:
                return False
            for i in range(1, math.floor(n**(1/2))+1):
                if not solve(n-i**2):
                    return True
            return False
        return solve(n)
    
    
    # Time complexity: O(sqrt(n) * n)
    # Space complexity: O(n)
    # Recursive approach with memoization
    def winnerSquareGame4(self, n: int) -> bool:
        @cache
        def solve(turn, n):
            if n == 0:
                if turn:
                    return False
                else:
                    return True
            if n == 1:
                if turn:
                    return True
                else:
                    return False
            if n == 2:
                if turn:
                    return False
                else:
                    return True

            if turn == True: # Alice turn
                for i in range(1, math.floor(n**(1/2))+1):
                    if solve(False, n - i*i):
                        return True
                return False
            else: # Bob turn
                for i in range(1, math.floor(n**(1/2))+1):
                    if solve(True, n - i*i) == False:
                        return False
                return True
        return solve(True, n)