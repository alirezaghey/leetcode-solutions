from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
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