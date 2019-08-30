// https://leetcode.com/problems/sqrtx/
// Related Topics: Math, Binary Search
// Difficulty: Easy

/*
Initial thoughts:
Using the fact that numbers are sorted by defualt we are going to
test every number starting from 1 until we find the square root
of the input.



Time complexity: O(squreroot(n)) where n === x
Space complexity: O(1)

*/

/**
 * @param {number} x
 * @return {number}
 */
const mySqrt = x => {
  if (x < 2) return x;

  for (let i = 1; i < x / 2 + 1; i++) {
    if (i ** 2 <= x && (i + 1) ** 2 > x) return i;
  }
};

/*
Optimization:
Using binary search, we are going to further decrease the time complexity
to log(n)
*/
