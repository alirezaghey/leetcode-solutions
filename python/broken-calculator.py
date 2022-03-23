class Solution:
    # Time complexity: O(log n) where n == target
    # Space complexity: O(1)
    def brokenCalc(self, startValue: int, target: int) -> int:
        res = 0
        while target > startValue:
            res += 1
            if target % 2:
                target += 1
            else:
                target //= 2
        
        return res + startValue - target