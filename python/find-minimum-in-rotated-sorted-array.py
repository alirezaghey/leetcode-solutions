from typing import List

class Solution:
    # Time complexity: O(log n) where n is the length of nums
    # Space complexity: O(1)
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1] or len(nums) == 1: return nums[0]
        
        left, right = 0, len(nums)-1
        res = float("inf")
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] <= nums[-1]: # right side
                res = min(res, nums[mid])
                right = mid-1
            else: # left side
                left = mid+1
        return res