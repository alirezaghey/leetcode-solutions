from collections import defaultdict
from typing import List


class Solution:
    # Time complexity: O(n) where n is the length of nums
    # Space complexity: O(n)
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1
        curr, res = 0, 0
        
        for el in nums:
            curr += el
            res += dic[curr - k]
            dic[curr] += 1
        return res