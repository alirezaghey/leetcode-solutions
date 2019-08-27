// https://leetcode.com/problems/count-and-say/
// Related Topics: String
// Difficulty: Easy

/*
Initial thoughts:
Splitting the input into buckets of equal numbers we concatenate
the number of each bucket with the length of it and put all of them
together. This is done n times

Time complexity: ?
Space complexity: ?

*/

/**
 * @param {number} n
 * @return {string}
 */
const countAndSay = n => {
  result = '1';
  for (let i = 1; i < n; i++) {
    result = result
      .match(/1+|2+|3+|4+|5+|6+|7+|8+|9+/g)
      .map(el => el.length + el[0])
      .join('');
  }
  return result;
};
