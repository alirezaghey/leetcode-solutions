// https://leetcode.com/problems/range-sum-query-immutable/
// Related Topics: Dynamic Programming
// Difficulty: Easy

/*
Initial thoughts:
The naive approach is to look at each and every element every time
and sum them. This would have a Time Complexity of O(n) and a Space Complexity of O(1)

Optimization:
Using a Dynamic Programming approach, we can create an array where array[k] holds the sum
of all the elements from nums[0] to nums[k].
Looking from the sum between i and j (where i <= j) we are going to take array[j] that holds
the sum from nums[0] to nums[j] and subtract array[i] from it (which holds the sum from nums[0] to nums[i])
If we do the preprocessing wisely, it won't take more than O(n) and the lookup time for the consequent sums
is constant.
Please note that this trade wouldn't have made sense if it wasn't specifically stated that the sum of different
ranges will be called repeatedly.

Time complexity: O(n) where n is the number of element in nums
Space complexity: O(n) where n is the number of elements in nums
*/

/**
 * @param {number[]} nums
 */
var NumArray = function(nums) {
  this.nums = nums;
  this.dp = this.preprocess();
};

/**
 * @param {number} i
 * @param {number} j
 * @return {number}
 */
NumArray.prototype.sumRange = function(i, j) {
  return this.dp[j + 1] - this.dp[i];
};

NumArray.prototype.preprocess = function() {
  const dp = Array(this.nums.length + 1).fill(0);
  for (i = 0; i < this.nums.length; i++) {
    dp[i + 1] = dp[i] + this.nums[i];
  }
  return dp;
};

/**
 * @param {number} i
 * @param {number} j
 * @return {number}
 */
NumArray.prototype.sumRangeNaive = function(i, j) {
  let sum = 0;
  for (k = i; k <= j; i++) sum += this.nums[k];
  return sum;
};

/**
 * Your NumArray object will be instantiated and called as such:
 * var obj = new NumArray(nums)
 * var param_1 = obj.sumRange(i,j)
 */
