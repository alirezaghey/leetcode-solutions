class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        
        while x or y:
            res += (x^y) & 1
            x, y = x >> 1, y >> 1
        return res