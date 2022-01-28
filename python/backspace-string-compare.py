class Solution:
    # Time complexity: O(n + m) where n and m are the lengths of s and t
    # Space cmoplexity: O(n + m)
    def backspaceCompare(self, s: str, t: str) -> bool:
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