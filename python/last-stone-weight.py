import heapq
from typing import List


class Solution:
    # Time complexity: O(n * log n)
    # Space complexity: O(1)
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)
        while len(stones) > 1:
            larger, smaller = heapq.heappop(stones), heapq.heappop(stones)
            larger -= smaller
            if larger < 0:
                heapq.heappush(stones, larger)

        return abs(stones.pop()) if stones else 0
