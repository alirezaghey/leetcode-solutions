class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        
        for i in range(len(nums)-2, -1, -1):
            res.append(res[-1]*nums[i+1])
        
        res.reverse()
        
        curr = 1
        for i in range(len(nums)):
            res[i] *= curr
            curr *= nums[i]
        
        return res