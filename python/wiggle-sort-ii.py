class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sorted_nums = list(sorted(nums))
        i ,j = len(nums)-1, 1
        while j < len(nums):
            nums[j] = sorted_nums[i]
            i, j = i-1, j+2
        
        j = 0
        while j < len(nums):
            nums[j] = sorted_nums[i]
            i, j = i-1, j+2