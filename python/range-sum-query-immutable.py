#  https://leetcode.com/problems/range-sum-query-immutable/
#  Related Topics: Dynamic Programming
#  Difficulty: Easy


# Initial thoughts:
# The naive approach is to look at each and every element every time
# and sum them. This would have a Time Complexity of O(n) and a Space Complexity of O(1)

# Optimization:
# Using a Dynamic Programming approach, we can create an array where array[k] holds the sum
# of all the elements from nums[0] to nums[k].
# Looking from the sum between i and j (where i <= j) we are going to take array[j] that holds
# the sum from nums[0] to nums[j] and subtract array[i] from it (which holds the sum from nums[0] to nums[i])
# If we do the preprocessing wisely, it won't take more than O(n) and the lookup time for the consequent sums
# is constant.
# Please note that this trade wouldn't have made sense if it wasn't specifically stated that the sum of different
# ranges will be called repeatedly.

# Time complexity: O(n) where n is the number of element in nums
# Space complexity: O(n) where n is the number of elements in nums

from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self._nums = nums
        self._dp = self.preprocess()

    def sumRange(self, i: int, j: int) -> int:
        return self._dp[j+1] - self._dp[i]

    def preprocess(self) -> List[int]:
        dp = [0 for i in range(len(self._nums)+1)]
        for i in range(len(self._nums)):
            dp[i+1] = dp[i] + self._nums[i]
        return dp

    def sumRangeNaive(self, i: int, j: int) -> int:
        sum = 0
        for k in range(i, j+1):
            sum += self._nums[k]
        return sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
