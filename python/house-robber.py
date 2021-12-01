from typing import List

class Solution:
    # bottom up iterative
    # TC: O(n)
    # SC: O(1)
    def rob(self, nums: List[int]) -> int:
        take, not_take = nums[0], 0
        for i in range(1, len(nums)):
            take, not_take = not_take + nums[i], max(take, not_take)
        return max(take, not_take)
            
    # bottom up iterative
    # TC: O(n)
    # SC: O(n)
    def rob2(self, nums: List[int]) -> int:
        dp = [[0]*2 for _ in range(len(nums))]
        dp[0][0] = nums[0]
        
        for i in range(1, len(nums)):
            dp[i][1] = max(dp[i-1][0], dp[i-1][1])
            dp[i][0] = dp[i-1][1] + nums[i]
        
        return max(dp[-1][0], dp[-1][1])
    # top down memoized recursive
    # TC: O(n) where n is the length of nums
    # SC: O(n)
    def rob3(self, nums: List[int]) -> int:
        def dfs(idx, taken, dp):
            if idx >= len(nums):
                return 0
            
            if (idx, taken) in dp:
                return dp[(idx, taken)]
            
            if taken:
                dp[(idx, taken)] = dfs(idx+1, False, dp)
            else:
                dp[(idx, taken)] = max(dfs(idx+1, True, dp)+nums[idx], dfs(idx+1, False, dp))
            
            return dp[(idx, taken)]
        
        return dfs(0, False, {})