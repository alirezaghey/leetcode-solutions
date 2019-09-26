// https://leetcode.com/problems/range-sum-query-2d-immutable/
// Related Topics: Dynamic Programming
// Difficulty: Medium

/*
Initial thoughts:
The naive approach is to look at each and every element every time
and sum them. This would have a Time Complexity of O(n) and a Space Complexity of O(1)

Optimization:
Using a Dynamic Programming approach, we can create a suplemental matrix where each element
contains the sum of all the values before it in that specific row plus itself.
Now to find the sum of the elements in a box in the matrix we need to add the sums for each
row in that box.
This is very similar to range-sum-query-immutable.py and its solution and will only add another
dimension to the whole problem.
Preprocessing will take up O(n) where n === matrix.width * matrix.heigth
Lookup time for a box inside the matrix is O(matrix.height) since the sum of a row can be calculated
in constant time.

Time complexity: O(n) where n === matrix.width * matrix.heigth
Space complexity: O(n) where n === matrix.width * matrix.heigth
*/

/**
 * @param {number[][]} matrix
 */
var NumMatrix = function(matrix) {
  this.matrix = matrix;
  this.dp = this.preprocess();
};

/**
 * @param {number} row1
 * @param {number} col1
 * @param {number} row2
 * @param {number} col2
 * @return {number}
 */
NumMatrix.prototype.sumRegion = function(row1, col1, row2, col2) {
  let sum = 0;
  for (let i = row1; i <= row2; i++) {
    sum += this.dp[i][col2 + 1] - this.dp[i][col1];
  }
  return sum;
};

NumMatrix.prototype.preprocess = function() {
  const dp = [];
  for (let i = 0; i < this.matrix.length; i++) {
    const row = Array(this.matrix[0].length + 1).fill(0);
    for (let j = 0; j < this.matrix[0].length; j++) {
      row[j + 1] = row[j] + this.matrix[i][j];
    }
    dp.push(row);
  }
  return dp;
};

/**
 * @param {number} row1
 * @param {number} col1
 * @param {number} row2
 * @param {number} col2
 * @return {number}
 */
NumMatrix.prototype.sumRegionNaive = function(row1, col1, row2, col2) {
  let sum = 0;
  for (let i = row1; i <= row2; i++)
    for (let j = col1; j <= col2; j++) sum += this.matrix[i][j];
  return sum;
};

/*
Optimization:
We could render the lookup time constant by storing the sum of the whole box before an element
in the dp array. Then with some basic arithmetic we can calculate any box in the matrix.

Time Complexity: O(n) where n === matrix.width * matrix.heigth
Space Complexity: O(n) where n === matrix.width * matrix.heigth
*/

/**
 * @param {number[][]} matrix
 */
var NumMatrix = function(matrix) {
  this.matrix = matrix;
  this.dp = this.preprocess();
};

/**
 * @param {number} row1
 * @param {number} col1
 * @param {number} row2
 * @param {number} col2
 * @return {number}
 */
NumMatrix.prototype.sumRegion = function(row1, col1, row2, col2) {
  return (
    this.dp[row2 + 1][col2 + 1] -
    this.dp[row1][col2 + 1] -
    this.dp[row2 + 1][col1] +
    this.dp[row1][col1]
  );
};

NumMatrix.prototype.preprocess = function() {
  if (this.matrix.length === 0 || this.matrix[0].length === 0) return null;
  const dp = [Array(this.matrix[0].length + 1).fill(0)];
  for (let i = 0; i < this.matrix.length; i++) {
    const row = Array(this.matrix[0].length + 1).fill(0);
    for (let j = 0; j < this.matrix[0].length; j++) {
      row[j + 1] = dp[i][j + 1] + row[j] - dp[i][j] + this.matrix[i][j];
    }
    dp.push(row);
  }
  return dp;
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * var obj = new NumMatrix(matrix)
 * var param_1 = obj.sumRegion(row1,col1,row2,col2)
 */
