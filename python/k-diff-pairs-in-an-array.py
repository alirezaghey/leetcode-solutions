from collections import defaultdict
from typing import List

class Solution:
    # Time complexity: O(n) where n is the length of nums
    # Space complexity: O(n)
    def findPairs(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        for el in nums:
            dic[el] += 1
        
        res = set()
        for el in nums:
            need = k + el
            if need in dic:
                if need != el:
                    res.add(tuple(sorted([el, need])))
                elif dic[need] > 1:
                    res.add(tuple(sorted([el, need])))
        return len(res)