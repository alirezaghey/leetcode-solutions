from typing import List


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3: return False
        
        found_peak = False
        for i in range(1, len(arr)-1):
            if not found_peak:
                if arr[i] <= arr[i-1]:
                    return False
                if arr[i] == arr[i+1]:
                    return False
                if arr[i] > arr[i+1]:
                    found_peak = True
            else:
                if arr[i] <= arr[i+1]:
                    return False
        return found_peak