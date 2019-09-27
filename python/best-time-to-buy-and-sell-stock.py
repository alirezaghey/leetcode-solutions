#  https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#  Related Topics: Array, Dynamic Programming
#  Difficulty: Easy


# Initial thoughts:
# The brute force approach is to create a nested loop and check each pair of elements in the input array
# searching for the maximum profit

# Time complexity: O(n^2) where n === number of prices
# Space complexity: O(1)
from typing import List


class Solution:
    def maxProfitBruteForce(self, prices: List[int]) -> int:
        maxProfit = float('-inf')
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] - prices[i] > maxProfit:
                    maxProfit = prices[j] - prices[i]
        return maxProfit if maxProfit > 0 else 0

# Optimization
# Since we are looking for the max of the differences between any prices[i+k] - prices[i]
# where 1 <= k < prices.length for each prices[i] it doesn't matter what the previous prices are.
# It is just enough to compare prices[i] with any prices[j] that comes after it.
# So moving forward we can keep the smallest prices[i] as minPrice and compare it with every
# following prices[j] and keep it if the difference is greater than previous differences.
# This will render our Time Complexity linear.

# Time complexity: O(n) where n === number of prices
# Space complexity: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        if not len(prices):
            return 0
        maxProfit = float('-inf')
        minPrice = prices[0]
        for i in range(1, len(prices)):
            maxProfit = max(maxProfit, prices[i]-minPrice)
            minPrice = min(minPrice, prices[i])
        return maxProfit if maxProfit > 0 else 0
