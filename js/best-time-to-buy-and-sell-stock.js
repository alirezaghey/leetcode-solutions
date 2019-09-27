// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
// Related Topics: Array, Dynamic Programming
// Difficulty: Easy

/*
Initial thoughts:
The brute force approach is to create a nested loop and check each pair of elements in the input array
searching for the maximum profit

Time complexity: O(n^2) where n === number of prices
Space complexity: O(1)
*/

/**
 * @param {number[]} prices
 * @return {number}
 */
const maxProfitBruteForce = prices => {
  let max = Number.MIN_SAFE_INTEGER;
  for (let i = 0; i < prices.length; i++) {
    for (let j = i + 1; j < prices.length; j++) {
      max = Math.max(max, prices[j] - prices[i]);
    }
  }
  return max > 0 ? max : 0;
};

/*
  Optimization
  Since we are looking for the max of the differences between any prices[i+k] - prices[i]
  where 1 <= k < prices.length for each prices[i] it doesn't matter what the previous prices are.
  It is just enough to compare prices[i] with any prices[j] that comes after it.
  So moving forward we can keep the smallest prices[i] as minPrice and compare it with every
  following prices[j] and keep it if the difference is greater than previous differences.
  This will render our Time Complexity linear.
  
  Time complexity: O(n) where n === number of prices
  Space complexity: O(1)
  */
const maxProfit = prices => {
  if (!prices.length) return 0;

  let max = Number.MIN_SAFE_INTEGER;
  let minPrice = prices[0];
  for (let i = 1; i < prices.length; i++) {
    max = Math.max(max, prices[i] - minPrice);
    minPrice = Math.min(minPrice, prices[i]);
  }
  return max > 0 ? max : 0;
};
