class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        best = 1
        curr = 0
        
        for el in nums:
            curr += el
            if curr < 1:
                best = max(best, 1 - curr)
        return best