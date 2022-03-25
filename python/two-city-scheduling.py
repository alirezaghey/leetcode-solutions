from functools import cache
from typing import List


class Solution:
    # Time complexity: O(n^3) where n is the length of costs
    # Space complexity: O(n^3)
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs)//2

        @cache
        def dfs(i, A, B):
            if i >= len(costs):
                return 0

            total = float("inf")
            if A < N and B < N:
                total = min(dfs(i+1, A+1, B) +
                            costs[i][0], dfs(i+1, A, B+1)+costs[i][1])
            elif A < N:
                total = sum(x for x, y in costs[i:])
            else:
                total = sum(y for x, y in costs[i:])
            return total

        return dfs(0, 0, 0)
