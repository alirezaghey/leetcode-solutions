from typing import List
import math
import bisect

class Solution:
    # Time complexity: O(n * log m) where n is the length of piles
    # and m is max(piles)
    # Space complexity: O(1)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            mid = l + (r - l) // 2
            curr = 0
            for el in piles:
                curr += math.ceil(el / mid)
                if curr > h: break
            if curr > h:
                l = mid+1
            else:
                res = min(res, mid)
                r = mid-1
        return res
    # Time comlexity: O(n * log n + log m * log n * n) where n is the length of piles
    # and m is max(piles)
    # Space complexity: O(1) or whatever space the sorting algorithm needs
    # Note: Sorting piles is not necessary for AC
    # It is better or worse than an algorithm where you don't sort piles
    # depending on the length of piles
    # If piles is big enough in comparison to its max value sorting makes much more sense
    def minEatingSpeed2(self, piles: List[int], h: int) -> int:
        piles.sort()
        l, r = 1, piles[-1]
        
        res = r
        
        while l <= r:
            mid = l + (r-l) // 2
            
            idx = bisect.bisect_right(piles, mid)
            curr = idx
            for i in range(idx, len(piles)):
                curr += math.ceil(piles[i] / mid)
                if curr > h:
                    break
            if curr > h:
                l = mid+1
            else:
                res = min(res, mid)
                r = mid-1
        return res

