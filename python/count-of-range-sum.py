class Solution:
    # custom merge sort approach
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        pref = [0]
        for el in nums:
            pref.append(pref[-1]+el)
            
        def divide(l, r):
            m = l + (r - l)//2
            if m == l: return 0
            
            res = divide(l, m) + divide(m, r)
            
            i = j = m
            for left in pref[l:m]:
                while i < r and pref[i] - left < lower: i += 1
                while j < r and pref[j] - left <= upper: j += 1
                res += j-i
            
            pref[l:r] = sorted(pref[l:r])
            return res
        return divide(0, len(pref))