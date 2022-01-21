from typing import List


class Solution:
    # Time complexity: (n-k+1) + (n-k) + (n-k-1) + ... + (n-k-(n-k)) =>
    #                  (n-k+1) + (n-k) + (n-k-1) + ... + (1) =>
    #                  (1) + (2) + ... + (n-k+1) =>
    #                  (n-k+1) * (n-k+2) / 2 =>
    #                  O((n-k)^2)
    # Space complexity: O((n-k)^2)
    # Recursive backtracking solution
    # Note: Optimized to bail out early
    # if a path doesn't have the potential to lead to valid results
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(curr, n, partial_res, res):
            if len(partial_res) == k:
                res.append(partial_res[:])
                return
            
            for i in range(curr, n+1):
                if k - len(partial_res) > n+1 - curr: continue
                partial_res.append(i)
                backtrack(i+1, n, partial_res, res)
                partial_res.pop()
        
        res = []
        backtrack(1, n, [], res)
        return res