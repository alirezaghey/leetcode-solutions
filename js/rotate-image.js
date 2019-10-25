// https://leetcode.com/problems/rotate-image/
// Related Topics: Array
// Difficulty: Medium

/*
Initial thoughts:
Looking at the matrix in liers, we are going to swap elements in
clockwise order while moving inward into the middle of the matrix

Time Complexity: O(n) where n == the number of cells in our matrix
Space Complexity: O(1)
*/

/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
const rotate = matrix => {
    const n = matrix.length - 1;
    for (let i = 0; i < Math.floor(matrix.length / 2); i++) {
        for (let j = i; j < n - i; j++) {
            const temp = matrix[i][j];
            matrix[i][j] = matrix[n - j][i];
            matrix[n - j][i] = matrix[n - i][n - j];
            matrix[n - i][n - j] = matrix[j][n - i];
            matrix[j][n - i] = temp;
        }
    }
};
