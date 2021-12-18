class Solution:
    def atMostNGivenDigitSet(self, digits, n):
        up, ans, T, str_n = [0]*10, 0, len(digits), str(n)
        for i in range(10):
            for dig in digits:
                up[i] += (dig < str(i))
        
        k, d_set = len(str_n), set(digits)
        for i in range(k):
            if i > 0 and str_n[i-1] not in d_set: break
            ans += up[int(str_n[i])] * T**(k-i-1)
        
        addon = (T**k - 1)//(T-1) - 1 if T != 1 else k - 1
        return ans + addon + (not set(str_n) - set(digits))