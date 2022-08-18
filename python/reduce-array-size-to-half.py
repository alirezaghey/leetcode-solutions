from typing import List
from collections import Counter


class Solution:
    # TC: O(n * log n) where n is the length of the input array
    # SC: O(n)
    def minSetSize(self, arr: List[int]) -> int:
        counter = Counter(arr)
        counter = list(sorted(x for y, x in counter.items()))

        need = len(arr)//2
        res = 0
        for el in reversed(counter):
            need -= el
            res += 1
            if need <= 0:
                return res
