from typing import List


class Solution:
    # Time complexity: O(log n)
    # Space complexity: O(1)
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = left + (right - left)//2
            if target > nums[mid]:
                left = mid+1
            elif target < nums[mid]:
                right = mid-1
            else:
                return mid

        return -1
