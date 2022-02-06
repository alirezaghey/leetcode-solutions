from typing import List

# Time complexity: O(n) where n is the length of nums
# Space complexity: O(1)
# Two pointer approach
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 2
        for i in range(2, len(nums)):
            if nums[left-2] != nums[i]:
                nums[left] = nums[i]
                left += 1
        return left