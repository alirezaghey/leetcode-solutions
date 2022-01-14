class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0: return 0
        if s[0] == "-":
            sign = -1
            s = s[1:]
        elif s[0] == "+":
            sign = 1
            s = s[1:]
        else:
            sign = 1
        
        res = 0
        i = 0
        while i < len(s) and s[i].isdigit():
            res *= 10
            res += int(s[i])
            i += 1
        res = res * sign
        if res < -2**31:
            return -2**31
        elif res > 2**31-1:
            return 2**31-1
        else:
            return res