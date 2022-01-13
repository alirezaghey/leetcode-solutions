from typing import List

class Solution:
    # Time complexity: O(n * log n)
    # Space complexity: O(1) or whatever the space complexity of the sorting algorithm is
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], x[1]))
        
        res = 0
        curr = None
        for start, end in points:
            if curr == None:
                curr = (start, end)
            elif start <= curr[1]:
                curr = (max(curr[0], start), min(curr[1], end))
            else:
                res += 1
                curr = (start, end)
        if curr:
            res += 1
        return res