// https://leetcode.com/problems/spiral-matrix-ii/
// Related Topics: Array
// Difficulty: Medium

/*
Initial thoughts:
We are going to write each border of an imaginary outline clockwise
and move inward until there are no more outlines left.
To keep track of the bounderies of our borders, we will have a variable
for each boundary that we increment or decrement accordingly.
To keep track of when we have reached the end of the spiral, we will
simply track the number of elements that we have already read. When that
number equals the number of the elements in the matrix, we are done.

Time complexity: O(n^2) where n === length of a side of our square matrix
Space complexity: O(n^2) where n === length of a side of our square matrix
(that's for the results array. In some interpretations, this does not count as
auxilliary space.)
*/

/**
 * @param {number} n
 * @return {number[][]}
 */
const generateMatrix = n => {
  if (n === 0) return [];

  const result = [];
  for (i = 0; i < n; i++) result.push(Array(n));

  let left = (top = 0);
  let right = (bottom = n - 1);
  let count = 1;
  const lenMatrix = n ** 2;

  while (true) {
    // Top
    for (let i = left; i <= right; i++) result[top][i] = count++;
    top++;
    if (count > lenMatrix) break;

    // Right
    for (let i = top; i <= bottom; i++) result[i][right] = count++;
    right--;
    if (count > lenMatrix) break;

    // Bottom
    for (let i = right; i >= left; i--) result[bottom][i] = count++;
    bottom--;
    if (count > lenMatrix) break;

    // Left
    for (let i = bottom; i >= top; i--) result[i][left] = count++;
    left++;
    if (count > lenMatrix) break;
  }
  return result;
};
