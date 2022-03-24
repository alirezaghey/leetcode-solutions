from typing import List

class Solution:
    # Time complexity: O(n * log n)
    # Space complexity: O(1) or whatever the sorting algorithm uses
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        res = 0
        right = len(people)-1
        
        for i, p in enumerate(people):
            if i > right:
                break
            if i == right:
                res += 1
                break
            else:
                if p + people[right] <= limit:
                    right -= 1
                res += 1
        
        return res