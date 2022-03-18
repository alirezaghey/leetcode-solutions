class Solution:
    # Time complexity: O(n) where n the length of the input string is
    # Space complexity: O(1)
    def removeDuplicateLetters(self, s: str) -> str:
        last_index = {c:i for i, c in enumerate(s)}
        res = []
        
        for i, c in enumerate(s):
            if c not in res:
                while res and c < res[-1] and i < last_index[res[-1]]:
                    res.pop()
                res.append(c)
        return "".join(res)