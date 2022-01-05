from typing import List


class Solution:
    # Time complexity: O(n) where n is the length of the string
    # Space complexity: O(1)
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i], s[~i] = s[~i], s[i]