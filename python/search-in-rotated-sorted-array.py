from typing import List


class Solution:
    # Time complexity: O(log n) where n is the length of nums
    # Space complexity: O(1)
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] < target:
                if nums[mid] < nums[-1]: # right part
                    if target > nums[-1]:
                        right = mid-1
                    else:
                        left = mid+1
                else: # left part
                    left = mid+1
            elif nums[mid] > target:
                if nums[mid] < nums[-1]: # right part
                    right = mid-1
                else: # left part
                    if target < nums[0]:
                        left = mid+1
                    else:
                        right = mid-1
            else:
                return mid
        
        return -1