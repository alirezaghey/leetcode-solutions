class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            res = max(res, nums[i])
        return res

# using divide and conquer approach
class Solution:
    def maxSubArray2(self, nums: List[int]) -> int:
        def d_and_d(l, r, nums):
            if l == r: return nums[l]
            
            mid = l + (r - l) // 2
            left = d_and_d(l, mid, nums)
            right = d_and_d(mid+1, r, nums)
            
            l_max = curr = nums[mid]
            for i in range(mid-1, l-1, -1):
                curr += nums[i]
                l_max = max(l_max, curr)
            
            r_max = curr = 0
            for i in range(mid+1, r+1, 1):
                curr += nums[i]
                r_max = max(r_max, curr)
            
            return max(left, right, l_max+r_max)
        
        return d_and_d(0, len(nums)-1, nums)