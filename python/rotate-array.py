from typing import List


class Solution:
    # Time complexity: O(n) where n is the length of nums
    # Space complexity: O(1)
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0: return
        
        nums.reverse()
        for i in range(k // 2):
            nums[i], nums[k-1-i] = nums[k-1-i], nums[i]
        for i in range((len(nums)-k) // 2):
            nums[i+k], nums[len(nums)-1-i] = nums[len(nums)-1-i], nums[i+k]
            
        
    # Relatively naive solution
    # Time complexity: O(n)
    # Space complexity: O(n)
    def rotate2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0: return
        tail = nums[len(nums)-k:]
        head = nums[:len(nums)-k]
        for i, el in enumerate(head):
            nums[i+k] = el
        for i, el in enumerate(tail):
            nums[i] = el            
        