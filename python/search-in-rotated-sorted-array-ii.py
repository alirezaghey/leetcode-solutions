from typing import List


class Solution:
    # Time complexity: O(n) in case all numbers of duplicates
    # If the numbers are distinct O(log n)
    # Space complexity: O(1)
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0:
            return False

        left = 0
        right = len(nums)-1
        while left <= right:
            while left < right and nums[left] == nums[left+1]:
                left += 1
            while left < right and nums[right] == nums[right-1]:
                right -= 1

            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            elif nums[left] <= nums[mid]:  # left sorted
                if target < nums[mid] and target >= nums[left]:
                    right = mid-1
                else:
                    left = mid+1
            else:  # right sorted
                if target > nums[mid] and target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1

        return False
