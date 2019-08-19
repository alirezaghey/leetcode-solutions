// Related Topics: Math, Array
// Difficulty: Easy

/*
Initial thoughts:
Converting the number to an array of strings
we can reverse the array and check wheter it
equals the original.

Time complexity: O(log n) because x has approximately log10(n) digits
Space complexity: O(n) because we need to convert the number to string

*/
/**
 * @param {number} x
 * @return {boolean}
 */

const isPalindrome = x => {
  let revX = x.toString().split('');

  // It's enough to copy half of the array
  // bc we are checking for a palindrome
  for (let i = 0; i < revX.length / 2; i++) revX[revX.length - i - 1] = revX[i];
  return x.toString() === revX.join('');
};

/*
Optimization:
Using basic math and arithmetic, we can reverse the number.
Problem is that we could run into an overflow.
The idea is to only revert half of the number and compare it
to the other half, using the property of palindromes that its
first half must equal the second. If it has an odd number of digits
that ditit (the middle one) does not affect our algorithm.

Time complexity: O(log n) because x has approximately log10(n) digits
Space complexity: O(1)
*/
/**
 * @param {number} x
 * @return {boolean}
 */
const isPalindrome = x => {
  // handling edge cases
  if (x < 0 || (x % 10 === 0 && x != 0)) {
    return false;
  }

  let revertedNumber = 0;
  // when x becomes equal or less than the reverted number
  // we know that we have reverted the right half of the number
  while (x > revertedNumber) {
    revertedNumber = revertedNumber * 10 + (x % 10);
    x = (x / 10) | 0;
  }

  // making sure that if it has an odd number of digits
  // we still catch the palindrome
  return x === revertedNumber || x === ((revertedNumber / 10) | 0);
};
