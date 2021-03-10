from typing import List

class Solution:
    # iterative dp solution
    # TC: O(n)
    # SC: O(1)
    def maxProduct(self, nums: List[int]) -> int:
        if nums[-1] < 0:
            negative, positive = nums[-1], 0
        else:
            negative, positive = 0, nums[-1]
            
        best = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            if nums[i] == 0:
                negative = positive = 0
            elif nums[i] < 0:
                negative, positive = min(nums[i], nums[i]*positive), max(nums[i], nums[i]*negative)
            else:
                negative, positive = min(nums[i], nums[i]*negative), max(nums[i], nums[i]*positive)
            best = max(best, positive)
        return best
    # iterative dp solution
    # TC: O(n)
    # SC: O(n)
    def maxProduct2(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        if nums[-1] < 0:
            dp[-1] = (0, nums[-1])
        else:
            dp[-1] = (nums[-1], 0)
        
        best = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            if nums[i] == 0:
                dp[i] = (0, 0)
            elif nums[i] < 0:
                dp[i] = (max(nums[i]*dp[i+1][1], nums[i]), min(nums[i]*dp[i+1][0], nums[i]))
            else:
                dp[i] = (max(nums[i]*dp[i+1][0], nums[i]), min(nums[i]*dp[i+1][1], nums[i]))
            best = max(best, *dp[i])
        return best