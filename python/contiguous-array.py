from typing import List


class Solution:
    # Time complexity: O(n) where n is the length of nums
    # Space complexity: O(n)
    def findMaxLength(self, nums: List[int]) -> int:
        count, res, dic = 0, 0, {0: -1}
        for i, el in enumerate(nums):
            count += 1 if el else -1
            if count in dic:
                res = max(res, i - dic[count])
            else:
                dic[count] = i
        return res