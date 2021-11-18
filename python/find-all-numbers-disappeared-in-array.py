# Inplace, O(n) time, O(1) space
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i, el in enumerate(nums):
            if nums[abs(el)-1] > 0:
                nums[abs(el)-1] *= -1
        
        return [i+1 for i in range(len(nums)) if nums[i] > 0]

# Using a set, O(n) time and O(n) space    
# class Solution:
#     def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#         s = set(nums)
#         return [i for i in range(1,len(nums)+1) if i not in s]
                    