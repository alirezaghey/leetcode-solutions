// https://leetcode.com/problems/pascals-triangle-ii/
// Related Topics: Array
// Difficulty: Easy

/*
Initial thoughts:
The naive solution is to handle this problem like with did Pascal's Triangle where we create a two dimensional array
with the values of Pascal's triangle up to the row that we need to return and then return the last row.

Optimization:
Since we only need the last row, we can have a one dimensional array that initially holds the first row of
Pascal's triangle and build uppon it by changing the values in place. This way we will decrease the space complexity
by a factor of n.

Time complexity: O(n^2) where n === index of the required row
Space complexity: O(n) where n === index of the required row
*/

/**
 * @param {number} rowIndex
 * @return {number[]}
 */
const getRow = rowIndex => {
  const result = [1];
  for (let i = 1; i <= rowIndex; i++) {
    let prev = result[0];
    for (let j = 1; j < result.length; j++) {
      const curr = result[j];
      result[j] = prev + curr;
      prev = curr;
    }
    result.push(1);
  }
  return result;
};
