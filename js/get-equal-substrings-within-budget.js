// https://leetcode.com/problems/get-equal-substrings-within-budget/
// Related Topics: Array, Sliding Window
// Difficulty: Medium

/*
Initial thoughts:
This problem boils down to a maximum sum problem if we had an array
of the differences between the two arrays in question. Such an array
can be created by taking the absolute value of the subtraction of corresponding
elements between the two input arrays.
Using a sliding window, we are going to move the right side forward and subtract
the value at that position from our budget while the budget is above zero.
If the budget goes sub zero, we are going to move the left side of the sliding window
forward while adding the value at that position the the budget, all the while
looking for the maximum length of the sliding window.

Time complexity: O(n) where n === len(s)
Space complexity: O(1)
*/

/**
 * @param {string} s
 * @param {string} t
 * @param {number} maxCost
 * @return {number}
 */
const equalSubstring = (s, t, maxCost) => {
  let left = (right = 0);
  let result = (tempResult = 0);

  while (right < s.length) {
    temp = Math.abs(s.charCodeAt(right) - t.charCodeAt(right));
    if (maxCost - temp >= 0) {
      maxCost -= temp;
      tempResult++;
      right++;
      if (tempResult > result) result++;
    } else {
      maxCost += Math.abs(s.charCodeAt(left) - t.charCodeAt(left));
      tempResult--;
      left++;
    }
  }
  return result;
};

/*
Optimization
Since we are going to look for the maximum possible length of the
sliding window, we don't actually need to explicitly track and move
the sliding window.
We are going to loop over the array and subtract the values from our budget
whenever the budget is less than zero we are going to move the left side of
the sliding window and add its value to the budget.
The resulting distance between the left side and right side at the end is
the maximum possible.
*/

/**
 * @param {string} s
 * @param {string} t
 * @param {number} maxCost
 * @return {number}
 */
const equalSubstring = (s, t, maxCost) => {
  let left = 0;
  for (var right = 0; right < s.length; right++) {
    maxCost -= Math.abs(s.charCodeAt(right) - t.charCodeAt(right));
    if (maxCost < 0) {
      maxCost += Math.abs(s.charCodeAt(left) - t.charCodeAt(left));
      left++;
    }
  }
  return right - left;
};
