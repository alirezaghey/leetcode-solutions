class Solution:
    # Time complexity: O(n log n) where n is the length of any of the strings
    # Space complexity: O(1)
    def findTheDifference(self, s: str, t: str) -> str:
        s = "".join(list(sorted(s)))
        t = "".join(list(sorted(t)))
        
        for x, y in zip(s, t):
            if x != y: return y
        return t[-1]