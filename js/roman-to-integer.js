// https://leetcode.com/problems/roman-to-integer/
// Related Topics: Math, String, Hash Table
// Difficulty: Easy

/*
Initial thoughts:
We are going to create a lookup table for every combination of Roman numbers
Since there are both two-letter and one-letter combinations, looping over the
input string, we first check for the two-letter combination in the lookup and
if it's not there, we take the one-letter combination, all the way adding the
values to the result.

Time complexity: O(n) we have to look at each character in the input string
Space complexity: O(1) 

*/

/**
 * @param {string} s
 * @return {number}
 */
const romanToInt = s => {
  let r = 0;
  for (let i = s.length; i > 0; i--) {
    if (lookup[s.slice(i - 2, i)]) {
      r += lookup[s.slice(i - 2, i)];
      i--;
    } else {
      r += lookup[s.slice(i - 1, i)];
    }
  }
  return r;
};

const lookup = {
  I: 1,
  V: 5,
  X: 10,
  L: 50,
  C: 100,
  D: 500,
  M: 1000,
  IV: 4,
  IX: 9,
  XL: 40,
  XC: 90,
  CD: 400,
  CM: 900
};
