from functools import cache
from typing import List

class Solution:
    # iterative dp solution
    # this approach uses an array for dp instead of a set
    # TC: O(n * m) where n is the length of nums and m is sum(nums)//2
    # SC: O(m)
    def canPartition(self, nums: List[int]) -> bool:
        half = sum(nums) / 2
        if half != int(half):
            return False
        half = int(half)
        
        dp = [False] * (half+1)
        dp[half] = True
        
        for num in nums:
            for el, state in enumerate(dp):
                if state == False: continue
                new_el = el - num
                if new_el == 0: return True
                if new_el > 0:
                    dp[new_el] = True
        
        return False


    # iterative solution
    # TC: O(n * m) where n is the length of nums and m is sum(nums)/2
    # SC: O(m)
    def canPartition2(self, nums: List[int]) -> bool:
        half = sum(nums) / 2
        if half != int(half):
            return False
        half = int(half)
        
        dp = set([half])
        for num in nums:
            new_dp = set()
            for state in dp:
                n_state = state-num
                if n_state == 0: return True
                if n_state > 0:
                    new_dp.add(n_state)
                new_dp.add(state)
            dp = new_dp
        return False




    # recursive memoized solution
    # TC: O(n * m) where n is length of nums and m is sum(nums)/2
    # SC: O(n * m) for the recursive stack and the cache
    def canPartition1(self, nums: List[int]) -> bool:
        half = sum(nums) / 2
        if half != int(half):
            return False
        half = int(half)
        
        @cache
        def dfs(idx, curr):
            if curr == 0:
                return True
            if curr < 0:
                return False
            if idx >= len(nums):
                return False
            
            for i in range(idx, len(nums)):
                return dfs(idx+1, curr-nums[i]) or dfs(idx+1, curr)
        
        return dfs(0, half)