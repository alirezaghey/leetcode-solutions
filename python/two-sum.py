# Related Topics: Array, Hash Table
# Difficulty: Easy


# Initial thoughts:
# Comparing each and every element of the array
# with the remaining elements after that specific one,
# we check whether they add up to the target value and
# return the indices.

# Time complexity: O(n^2) where n == len(nums)
# Space complexity: O(1)

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]


# Optimization:
# We could set up a lookup dictionary to reduce the
# time complexity of the inner loop to O(1), trading space
# for time.

# Time complexity: O(n) where n == len(nums)
# Space complexity: O(n) where n == len(nums)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {nums[i]: i for i in range(len(nums))}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in lookup and i != lookup[complement]:
                return [lookup[complement], i]


# Optimization:
# We can further optimize our solution to check for the complement
# and fill the lookup dictionary in one go.

# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = dict()
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in lookup:
                return [lookup[complement], i]
            else:
                lookup[nums[i]] = i
