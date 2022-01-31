from typing import List


class Solution:
    # Time complexity: O(n + m) where n and m are the number of customers and banks
    # Space complexity: O(1)
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = 0
        for customer in accounts:
            curr = 0
            for bank in customer:
                curr += bank
            res = max(res, curr)
        return res
    
    # Time complexity: O(n + m) where n and m are the number of customers and banks
    # Space complexity: O(1)
    def maximumWealth2(self, accounts: List[List[int]]) -> int:
        return max(sum(customer) for customer in accounts)