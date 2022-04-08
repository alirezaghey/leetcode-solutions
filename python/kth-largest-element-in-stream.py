import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.hp = list(sorted([num for num in nums], reverse=True))[:k]
        heapq.heapify(self.hp)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.hp, val)
        if len(self.hp) > self.k:
            heapq.heappop(self.hp)
        return self.hp[0]
