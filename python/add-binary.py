class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry, i, j = 0, len(a)-1, len(b)-1
        
        while i >= 0 or j >= 0:
            curr = carry
            if i >= 0:
                curr += int(a[i])
                i -= 1
            if j >= 0:
                curr += int(b[j])
                j -= 1
            res.append(curr%2)
            carry = curr // 2
        
        if carry:
            res.append(carry)
        return "".join(map(str, reversed(res)))
    
    def addBinary2(self, a: str, b: str) -> str:
        res = []
        carry, i, j = 0, len(a)-1, len(b)-1
        
        while i >= 0 and j >= 0:
            curr = carry + int(a[i]) + int(b[j])
            res.append(curr%2)
            carry = curr // 2
            i, j = i-1, j-1
        
        while i >= 0:
            curr = carry + int(a[i])
            res.append(curr%2)
            carry = curr // 2
            i -= 1
        
        while j >= 0:
            curr = carry + int(b[j])
            res.append(curr%2)
            carry = curr // 2
            j -= 1
        
        if carry:
            res.append(carry)
        return "".join(map(str, reversed(res)))