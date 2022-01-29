from typing import List


class Solution:
    # Time complexity: O(n) where n is the length of heights
    # Space complexity: O(n)
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        res = 0
        stack = [-1]
        
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                w = i - stack[-1] -1
                res = max(res, h*w)
            stack.append(i)
        # heights.pop()
        return res