from typing import List


class Solution:
    # Time complexity: O(n) where n is the length of the seats array
    # Space complexity: O(1)
    # Note: It is crucial to take care of the edge cases of
    # a prefix/suffix of empty seats in the seats array
    def maxDistToClosest(self, seats: List[int]) -> int:
        left = -1
        max_dist = 1
        
        for right, el in enumerate(seats):
            if el == 0:
                if left == -1:
                    max_dist = max(max_dist, right+1)
                else:
                    if (right - left) % 2 == 0: # even
                        max_dist = max(max_dist, (right-left) // 2)
                    else: # odd
                        max_dist = max(max_dist, (right-left+1) // 2)
            else:
                left = right
        
        # taking care of a trailing empy seat sub array that ends with an empy seat
        if seats[-1] == 0:
            max_dist = max(max_dist, len(seats) - left-1)
        
        return max_dist