class Solution:
    # Time complexity: O(max(n, m)) where n and m are the length of s and t
    # Space complexity: O(1)
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s)-1, len(t)-1
        
        while i >= 0 or j >= 0:
            c = 0
            while i >= 0 and (s[i] == "#" or c > 0):
                if s[i] == "#":
                    c += 1
                else:
                    c -= 1
                i -= 1
            
            c = 0
            while j >= 0 and (t[j] == "#" or c > 0):
                if t[j] == "#":
                    c += 1
                else:
                    c -= 1
                j -= 1
            
            if i >= 0 and j >= 0:
                if s[i] != t[j]: return False
                i, j = i-1, j-1
            else:
                break
        

            
        return i < 0 and j < 0

    # Time complexity: O(n + m) where n and m are the lengths of s and t
    # Space cmoplexity: O(n + m)
    def backspaceCompare2(self, s: str, t: str) -> bool:
        ss, tt = [], []
        
        for c in s:
            if c == "#" and ss:
                ss.pop()
            elif c != "#":
                ss.append(c)
        
        for c in t:
            if c == "#" and tt:
                tt.pop()
            elif c != "#":
                tt.append(c)
        print(ss, tt)
        return "".join(ss) == "".join(tt)