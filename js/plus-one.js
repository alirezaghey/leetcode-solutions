// https://leetcode.com/problems/plus-one/
// Related Topics: Array
// Difficulty: Easy

/*
Initial thoughts:
Looping over the array from the end backwards we are going to add one to
the value, always taking care that the value does not become greater than 9.
If there is no remainder(carry) we break out of the loop, otherwise we carry
the remainder to the digit to the left.
At the end of the loop we check to make sure that there is no carry remaining,
if there is some remainder, we are going to add it to the head of the array.

Time complexity: O(n) where n === digits.length
Space complexity: O(1)

*/

/**
 * @param {number[]} digits
 * @return {number[]}
 */
const plusOne = digits => {
  let carry = 1;
  for (let i = digits.length - 1; i >= 0; i--) {
    let temp = digits[i] + carry;
    carry = (temp / 10) | 0;
    temp = temp % 10;
    digits[i] = temp;
    if (!carry) break;
  }
  if (carry) digits.unshift(carry);
  return digits;
};
