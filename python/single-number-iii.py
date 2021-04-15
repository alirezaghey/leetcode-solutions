class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for el in nums:
            xor ^= el
        
        mask = 1
        while mask&xor == 0:
            mask <<= 1
        
        a = b = 0
        for el in nums:
            if el&mask == 0:
                a ^= el
            else:
                b ^= el
        
        return [a, b]