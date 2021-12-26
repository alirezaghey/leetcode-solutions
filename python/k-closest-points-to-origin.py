import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp = []
        
        for x, y in points:
            d = x**2 + y**2
            if len(hp) >= k:
                heapq.heappushpop(hp, (-d, x, y))
            else:
                heapq.heappush(hp, (-d, x, y))
        
        return [(x, y) for d, x, y in hp]