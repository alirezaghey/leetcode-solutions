// https://leetcode.com/problems/pascals-triangle/
// Related Topics: Array
// Difficulty: Easy

/*
Initial thoughts:
Considering that each row in Pascal's triangle consists of the sum of each adjacent cells
in the previous row with a 1 added to the beginning and end of the row we can
create the triangle with a nested loop.

Time complexity: O(n^2) where n is the number of rows. The outer loop runs n time while the inner
loop runs (1 + 2 + 3 + ... + n-1 + n) times which is n * (n+1) / 2
Space complexity: O(n^2) where n is the number of rows

*/

/**
 * @param {number} numRows
 * @return {number[][]}
 */
const generate = numRows => {
  if (numRows === 0) return [];

  const result = [[1]];
  for (let i = 0; i < numRows - 1; i++) {
    const tempRow = [1];
    for (let j = 1; j < result[i].length; j++) {
      tempRow.push(result[i][j - 1] + result[i][j]);
    }
    tempRow.push(1);
    result.push(tempRow);
  }
  return result;
};

/*
Recursive approach
*/

/**
 * @param {number} numRows
 * @return {number[][]}
 */
const generate = numRows => {
  if (numRows === 0) return [];

  const result = [[1]];
  generateNextRow(numRows - 1);
  return result;

  function generateNextRow(numRows) {
    if (numRows === 0) return;
    const row = [1];
    for (let i = 1; i < result[result.length - 1].length; i++) {
      row.push(result[result.length - 1][i - 1] + result[result.length - 1][i]);
    }
    row.push(1);
    result.push(row);
    generateNextRow(numRows - 1);
  }
};
