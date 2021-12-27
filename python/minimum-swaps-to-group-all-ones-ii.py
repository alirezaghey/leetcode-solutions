from typing import List


class Solution:
    # Sliding window approach
    # Time complexity: O(n)
    # Space complexity: O(1)
    def minSwaps(self, nums: List[int]) -> int:
        ones = sum(nums)
        nums += nums
        
        max_nums_window = curr_nums_window = sum(nums[:ones])
        left, right = 0, ones-1
        for i in range(len(nums)-ones):
            if nums[left+i] == 1:
                curr_nums_window -= 1
            if nums[right+i+1] == 1:
                curr_nums_window += 1
            max_nums_window = max(max_nums_window, curr_nums_window)
        return ones - max_nums_window