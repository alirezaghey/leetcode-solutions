#  https://leetcode.com/problems/container-with-most-water/
#  Related Topics: Array, Two Pointers
#  Difficulty: Medium


# Initial thoughts:
# We need to maximize the area between two bars (containers).
# The area is always the distance between the bars times the smaller bar.
# The brute force solution is to test each bar with all the others, which
# gives an O(n^2) solution.
# But we could greately optimize our solution with a two pointer approach.
# We start at both ends of the x axis and take the distance between the bars
# times the shorter bar. The we move the short bar towards the other and test
# again for maximum.
# We can be sure that this approach works because we wouldn't have any benefits
# gained from moving the taller bar or from starting from a point where the distance
# between the bars is not maximized.

# In other words:
# The area for any given interval is equal to (right - left) * min(height[right], height[left])
# Suppose height[left] <= height[right]. If we increment left, we skip all the possible lines (i to j-1), (i to j-2)... (i to i+1).
# Since the max height for all of these areas can never be greater than height[i], and the width only decreases,
# we can be sure that we don't lose any better solution in this skipped set.
# Therefore, we can just have 2 pointers and move the one with the lesser height.

# Time complexity: O(n) where an is the number of bars
# Space complexity: O(1)
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        result = 0
        while right > left:
            result = max(result,
                         min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return result
