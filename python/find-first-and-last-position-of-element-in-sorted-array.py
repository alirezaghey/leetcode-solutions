# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Related Topics: Array, Binary Search
# Difficulty: Medium


# Initial thoughts:
# A naive approach is to look at every element of nums to find the beginning
# and end of target. This approach's Time complexity is O(n).

# To reduce the Time complexity to O(log n) we are going to use binary search.
# Let's say we find target at nums[i]. If nums[i-1] === nums[i] we are going to
# binary search againt for target between 0 and i and repeat this process until
# we find an index k where either k === 0 or nums[k-1] < nums[k].
# The same goes for the right bound of our range. If nums[i+1] === nums[i]
# we are going to binary search for target between i and nums.length-1 until we
# find an index k where either k === nums.length-1 or nums[k] < nums[k+1].
# This will be a multitude of log ns at most.

# Time complexity: O(log n) where n === nums.length
# Space complexity: O(log n) because of the recursive binary search

from typing import List
import bisect

# Note: Everything after searchRange2 is old and not optimal
# I realize that I've learned some lessons over the past couple of years
class Solution:

    # Time complexity: O(log n) where n is the length of nums
    # Space complexity: O(1)
    # Implementing my own bisect_left/bisect_right functions
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bisect_left(arr, target):
            left, right = 0, len(arr)
            
            while left < right:
                mid = left + (right - left) // 2
                if target > arr[mid]:
                    left = mid+1
                else:
                    right = mid
            return left
        
        def bisect_right(arr, target):
            left, right = 0, len(arr)
            
            while left < right:
                mid = left + (right - left) // 2
                if target < arr[mid]:
                    right = mid
                else:
                    left = mid+1
            return left
        
        if len(nums) == 0: return [-1, -1]
        left = bisect_left(nums, target)
        if left >= len(nums) or nums[left] != target:
            return [-1, -1]
        
        right = bisect_right(nums, target)
        return [left, right-1]
        
    # Time complexity: O(log n) where n is the length of nums
    # Space compleixty: O(1)
    # Using pythons built-in bisect module
    def searchRange2(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0: return [-1, -1]
        
        left = bisect.bisect_left(nums, target)
        if left >= len(nums) or nums[left] != target:
            return [-1, -1]
        right = bisect.bisect_right(nums, target)
        return [left, right-1]



    def searchRange3(self, nums: List[int], target: int) -> List[int]:
        def BinarySearch(nums: List[int], target: int, low: int, high: int) -> int:
            if low > high:
                return -1
            mid = low + (high-low)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return BinarySearch(nums, target, low, mid-1)
            else:
                return BinarySearch(nums, target, mid+1, high)

        index = BinarySearch(nums, target, 0, len(nums)-1)
        if index == -1:
            return [-1, -1, ]

        # Find left bound
        left = index
        while left > 0 and nums[left] == nums[left-1]:
            left = BinarySearch(nums, target, 0, left-1)

        # Find right bound
        right = index
        while right < len(nums)-1 and nums[right] == nums[right+1]:
            right = BinarySearch(nums, target, right+1, len(nums))

        return [left, right]



    # Optimization:
    # Using a iterative binary search we can render the space complexity constant
    # although this will arguably have a less readable code

    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def searchRange4(self, nums: List[int], target: int) -> List[int]:
        def BinarySearchIterative(nums: List[int], target: int, low: int, high: int) -> int:
            while low <= high:
                mid = low + (high-low)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    high = mid-1
                else:
                    low = mid+1
            return -1

        index = BinarySearchIterative(nums, target, 0, len(nums))
        if index == -1:
            return [-1, -1]

        # Find left bound
        left = index
        while left > 0 and nums[left] == nums[left-1]:
            left = BinarySearchIterative(nums, target, 0, left-1)

        # Find right bound
        right = index
        while right < len(nums)-1 and nums[right] == nums[right+1]:
            right = BinarySearchIterative(nums, target, right+1, len(nums)-1)

        return [left, right]


