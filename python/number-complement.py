from math import log10, floor

class Solution:
    def findComplement(self, num: int) -> int:
        res = 0
        num = int(bin(num)[2:], 10)
        digits = floor(log10(num))
        for i in range(digits, -1, -1):
            res <<= 1
            power = 10**i
            n = num // power
            num = num % power
            res |= 0 if n else 1
        return res
            
        
    def findComplement2(self, num: int) -> int:
        res = []
        while num:
            res.append("0" if num & 1 else "1")
            num >>= 1
        return int("".join(reversed(res)), 2)