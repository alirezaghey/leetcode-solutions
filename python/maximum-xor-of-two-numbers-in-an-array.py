from typing import List


class Solution:
    # Time complexity: O(n) where n is the length of nums
    # Space complexity: O(n)
    def findMaximumXOR(self, nums: List[int]) -> int:
        masks = [2**i for i in range(31, -1, -1)]
        res = 0
        
        trie = {}
        for num in nums:
            node = trie
            for mask in masks:
                bit = num & mask
                bit = 1 if bit > 0 else 0
                if bit not in node:
                    node[bit] = {}
                node = node[bit]
        
            curr = 0
            node = trie
            for mask in masks:
                bit = num & mask
                bit = 1 if bit > 0 else 0
                if bit^1 in node:
                    curr += mask
                    node = node[bit^1]
                elif bit in node:
                    node = node[bit]
                else:
                    break
            res = max(res, curr)
        return res