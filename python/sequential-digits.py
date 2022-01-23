from typing import List
import math

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        base = "123456789"
        low_d, high_d = int(math.log10(low))+1, int(math.log10(high))+1
        res = []
        for length in range(low_d, high_d+1):
            for i in range(9-length+1):
                if low <= (num := int(base[i:i+length])) <= high:
                    res.append(num)
        return res


    def sequentialDigits2(self, low: int, high: int) -> List[int]:
        n = len(str(high))
        def backtrack(num, curr, res):
            if len(curr) > n:
                return
            if num == 9:
                return
            
            curr += str(num+1)
            curr_num = int(curr)
            if low <= curr_num <= high:
                res.append(curr_num)
            backtrack(num+1, curr, res)
            
            
        res = []
        first = 1
        for i in range(first, 10):
            backtrack(i, str(i), res)
        return list(sorted(res))