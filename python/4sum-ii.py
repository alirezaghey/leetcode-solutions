from typing import List
from collections import defaultdict, Counter

class Solution:
    # Time complexity: O(n^2) where n is the length of nums
    # Space complexity: O(n^2)
    # Using python's Counter and sum
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        ct = Counter(x+y for x in nums1 for y in nums2)
        res = sum(ct[-(x+y)] for x in nums3 for y in nums4)
        return res


    # Time complexity: O(n^2) where n is the length of nums
    # Space complexity: O(n^2)
    def fourSumCount2(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        res = 0
        dic = defaultdict(int)
        for x, y in ((x, y) for x in nums1 for y in nums2):
            dic[x + y] += 1
        for x, y in ((x, y) for x in nums3 for y in nums4):
            res += dic[-(x+y)]
        return res
        