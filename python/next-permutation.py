#  https://leetcode.com/problems/next-permutation/
#  Related Topics: Array
#  Difficulty: Medium

# Initial thoughts:
# In order to create the next permutation, we need to think about how a permutation
# is build from its smallest value (lexicographically or mathematically) to it greatest
# and just take that approach one step further.
# Suppose we have (2,3,1). We would sort the numbers ascending
# coming to (1,2,3). Now let's create the six permutations for this:
# (1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2), (3,2,1)
# Let's do another one (1,2,3,4). We will have:
# (1,2,3,4), (1,2,4,3), (1,3,2,4), (1,3,4,2), (1,4,2,3), (1,4,3,2),...
# Let's do another one (1,2,3,4,5). We will have:
# (1,2,3,4,5), (1,2,3,5,4), (1,2,4,3,5), (1,2,4,5,3), (1,2,5,3,4), (1,2,5,4,3), (1,3,2,4,5)
# A pattern is starting to emerge:
# It appears that to create the next permutation, we need to look from right to left and
# find the first occurence where nums[i] > nums[i-1]. Now, we can't just swap nums[i] with
# nums[i-1] because we could skip some permutations and get a much bigger than just the next one.
# The solution is to take the smallest number after nums[i-1] that is just greater than nums[i-1]
# ans swap it with nums[i-1]. The remaining numbers after num[i-1] need to be added after nums[i-1]
# ascending.
# The thing is that they are already sorted, just in descending order, so we need to reverse the numbers after num[i-1]

# Time complexity: O(n) where n == length of nums
# Space complexity: O(1)

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Find the partition where nums[i] > nums[i-1]
        for i in reversed(range(1, len(nums))):
            if nums[i] > nums[i-1]:  # found partition
                # Find the smallest number after nums[i-1] that is greater than nums[i-1]
                foundIndex = -1
                for j in reversed(range(i, len(nums))):
                    if nums[j] > nums[i-1]:
                        if foundIndex == -1:
                            foundIndex = j
                        else:
                            if nums[j] < nums[foundIndex]:
                                foundIndex = j
                # Swap the numbers
                nums[i-1], nums[foundIndex] = nums[foundIndex], nums[i-1]
                # Reverse everything after nums[i-1] in place
                j = len(nums)-1
                while i < j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
                return
        # there is no greater permutation than what is already given so reverse it and return
        for j in range(len(nums)//2):
            nums[j], nums[len(nums)-1-j] = nums[len(nums)-1-j], nums[j]
        return
