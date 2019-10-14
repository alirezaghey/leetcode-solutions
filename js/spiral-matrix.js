// https://leetcode.com/problems/spiral-matrix/
// Related Topics: Array
// Difficulty: Medium

/*
Initial thoughts:
We are going to read each border of a imaginary outline clockwise
and move inward until there are no more outlines left.
To keep track of the bounderies of our borders, we will have a variable
for each boundary that we increment or decrement accordingly.
To keep track of when we have reached the end of the spiral, we will
simply track the number of elements that we have already read. When that
number equls the number of the elements in the matrix, we are done.

Time complexity: O(n) where n === number of elements in matrix
Space complexity: O(n) where n === number of elements in matrix (that's
for the results array. In some interpretations, this does not count as
auxilliary space.)
*/

/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
  if (matrix.length === 0 || matrix[0].length === 0) return [];
  let left = (top = 0);
  let bottom = matrix.length;
  let right = matrix[0].length;

  let n = 0;
  const lenMatrix = matrix.length * matrix[0].length;
  const result = [];

  while (true) {
    // Top
    for (let i = left; i <= right; i++) {
      result.push(matrix[top][i]);
      n++;
    }
    top++;
    if (n >= lenMatrix) break;

    // Right
    for (let i = top; i <= bottom; i++) {
      result.push(matrix[i][left]);
      n++;
    }
    right--;
    if (n >= lenMatrix) break;

    // Bottom
    for (let i = right; i >= left; i--) {
      result.push(matrix[bottom][i]);
      n++;
    }
    bottom--;
    if (n >= lenMatrix) break;

    // Left
    for (let i = bottom; i >= top; i--) {
      result.push(matrix[i][left]);
      n++;
    }
    left++;
    if (n >= lenMatrix) break;
  }
  return result;
};
