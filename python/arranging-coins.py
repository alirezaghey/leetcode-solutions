class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        res = 1
        
        while left <= right:
            mid = left + (right - left) // 2
            if mid*(mid+1)/2 <= n:
                res = mid
                left = mid+1
            else:
                right = mid-1
        return res

# O(n) solution
#    def arrangeCoins(self, n: int) -> int:
#        res = 0
#        i = 1
#        
#        while i <= n:
#            res += 1
#            n -= i
#            i += 1
#        return res