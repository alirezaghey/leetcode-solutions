from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        words = [Counter(word) for word in words]
        res = []
        
        for c in words[0]:
            curr = words[0][c]
            for i in range(1, len(words)):
                curr = min(curr, words[i][c])
                if curr == 0:
                    break
            if curr > 0:
                res.extend([c]*curr)
        return res