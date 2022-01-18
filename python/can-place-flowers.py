from typing import List


class Solution:
    # Time complexity: O(n) where n is the length of flowerbed
    # Space complexity: O(1)
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0: return True
        prev = -1
        
        for i, el in enumerate(flowerbed):
            if el == 1:
                prev = i
            elif (prev == -1 or i - prev > 1) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                    n -= 1
                    prev = i
                    if n == 0:
                        return True
        return False