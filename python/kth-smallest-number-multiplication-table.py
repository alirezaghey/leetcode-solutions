class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def distance(x):
            cnt = 0
            for i in range(1, m+1):
                cnt += min(x // i, n)
            return cnt
        
        left, right = 1, m*n
        
        ans = 1
        while left <= right:
            mid = left + (right - left) // 2
            d = distance(mid)
            if d >= k:
                ans = mid
                right = mid-1
            else:
                left = mid+1
        return ans