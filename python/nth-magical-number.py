from math import lcm

class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        lower, upper = min(a, b), n * a
        MOD = 1_000_000_007
        best = float("inf")
        least_common_mult = lcm(a, b)
        
        while lower <= upper:
            mid = lower + (upper - lower) // 2
            
            curr = mid // a + mid // b - (mid // least_common_mult)
            if curr >= n:
                best = min(best, mid)
                upper = mid - 1
            else:
                lower = mid + 1
        return best % MOD
