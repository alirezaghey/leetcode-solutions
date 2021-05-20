class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = left + (right - left)//2
            
            if mid != 0 and mid < len(nums)-1:
                if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                    return nums[mid]
            elif mid == len(nums)-1:
                if nums[mid] != nums[mid-1]:
                    return nums[mid]
            elif mid == 0:
                if nums[mid] != nums[mid+1]:
                    return nums[mid]
            
            if mid % 2 == 0: # both sides are equal
                if nums[mid-1] != nums[mid]:
                    left = mid+1
                else:
                    right = mid-1
            else:
                if nums[mid-1] == nums[mid]:
                    left = mid+1
                else:
                    right = mid-1