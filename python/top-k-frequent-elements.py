from collections import defaultdict
import heapq
from typing import List


class Solution:
    # Time complexity: O(n log k)
    # Space complexity: O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hp = []
        counter = defaultdict(int)
        in_heap = set()

        for num in nums:
            counter[num] += 1
            if hp and hp[0][1] == num:
                heapq.heappushpop(hp, (counter[num], num))
            elif len(hp) < k and num not in in_heap:
                heapq.heappush(hp, (counter[num], num))
                in_heap.add(num)
            elif hp[0][0] < counter[num] and num not in in_heap:
                while hp[0][0] < counter[hp[0][1]]:
                    heapq.heappushpop(hp, (counter[hp[0][1]], hp[0][1]))
                if hp[0][0] < counter[num]:
                    in_heap.remove(hp[0][1])
                    in_heap.add(num)
                    heapq.heappushpop(hp, (counter[num], num))

        return [y for x, y in hp]
