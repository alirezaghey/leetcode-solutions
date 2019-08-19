// Related Topics: Math
// Difficulty: Easy

/*
Initial thoughts:
The easiest way to solve this problems is by converting the number
to an array of strings and then reversing the array joining the
elements and casting it back to a number.
One problem that we need to watch out for is that if the number is
doesn't fit in a 32-bit signed integer, we need to return 0;
JS default number types are 64-bit floats and to simulate that,
we can define a MAX and MIN and if the result is greater or less
than MAX and MIN return 0.
This approach has a time complexity of O(log n), the number of digits,
and a space complexity of O(log n), because we define character for every digit.

Optimization:
A more effective method is to use math to solve the problem. The traditional push
and pop on arrays can be simulated on numbers by using employing basic arithmetic.


Time complexity: O(log n) because x has approximately log10(n) digits
Space complexity: O(1)

*/

/**
 * @param {number} x
 * @return {number}
 */
const reverse = x => {
  const MAX = Math.pow(2, 31) - 1;
  const MIN = Math.pow(-2, 31);

  let result = 0;

  while (x !== 0) {
    const t = x % 10;
    x = (x / 10) | 0;

    if (result > MAX / 10 || (result === MAX / 10 && t > 7)) return 0;
    if (result < MIN / 10 || (result === MIN / 10 && t < -8)) return 0;

    result = result * 10 + t;
  }
  return result;
};
