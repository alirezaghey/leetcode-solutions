// https://leetcode.com/problems/climbing-stairs/
// Related Topics: Dynamic Programming
// Difficulty: Easy

/*
Initial thoughts:
Considering the fact that the ways we can reach step i equals
the ways we can reach step i-1 + the ways we can reach step i-2
we approach the problem like calculating the Fibonacci number
by calculating every next step based on the last two, starting from
our two base cases where for n === 1 there is one way and for n === 2
there are two ways to reach step n.



Time complexity: O(n)
Space complexity: O(1)

*/

/**
 * @param {number} n
 * @return {number}
 */
const climbStairs = n => {
  if (n === 1) return 1;
  let first = 1,
    second = 2;
  for (let i = 3; i <= n; i++) {
    const third = first + second;
    first = second;
    second = third;
  }
  return second;
};
