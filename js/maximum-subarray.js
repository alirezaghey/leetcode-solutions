// https://leetcode.com/problems/maximum-subarray/
// Related Topics: Array, Dynamic Programming, Divide and Conquer
// Difficulty: Easy

/*
Initial thoughts:
Using a sliding window, we are going to create a submax and a max
and always taking the greater value of them.
If submax becomes less than zero we reset it to zero.

Time complexity: O(n) where n === nums.length
Space complexity: O(1)

*/
/**
 * @param {number[]} nums
 * @return {number}
 */
const maxSubArray = nums => {
  return nums.reduce(
    (acc, el) => {
      acc.subMax += el;
      acc.max = Math.max(acc.max, acc.subMax);
      acc.subMax = acc.subMax < 0 ? 0 : acc.subMax;
      return acc;
    },
    { max: Number.MIN_SAFE_INTEGER, subMax: 0 }
  ).max;
};
