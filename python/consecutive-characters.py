from itertools import groupby
class Solution:
    def maxPower(self, s: str) -> int:
        return max(len(list(g)) for _, g in groupby(s))
    
    
    def maxPower2(self, s: str) -> int:
        best, curr_count, curr_char = 1, 1, s[0]
        
        for i in range(1, len(s)):
            if s[i] == curr_char:
                curr_count += 1
            else:
                curr_char = s[i]
                curr_count = 1
            best = max(best, curr_count)
        return best