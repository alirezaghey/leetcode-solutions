// https://leetcode.com/problems/search-a-2d-matrix/
// Related Topics: Array, Binary Search
// Difficulty: Medium

/*
Initial thoughts:
Since each row of the matrix is sorted and the first element of each row
is larger than the last element of the previous row, we can find out whether
our target element is available by first performing a binary search on the rows
of the matrix. If we find a potential row that could possibly harbor our target
we are going to perform a binary search on the cells on that specific row.
Such a row must have the following properties: row[0] <= target and row[-1] >= target

Time Complexity: O(log(n) + log(m)) where n == len(matrix) and m == len(matrix[0])
Space Complexity: O(1)
*/

/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
const searchMatrix = (matrix, target) => {
    if (!matrix || !matrix.length || !matrix[0].length) return false;

    let row = null;
    let [left, right] = [0, matrix.length - 1];

    while (left <= right) {
        const mid = Math.floor((right - left) / 2) + left;
        if (target < matrix[mid][0]) right = mid - 1;
        else if (target > matrix[mid][matrix[0].length - 1]) left = mid + 1;
        else {
            row = mid;
            break;
        }
    }

    if (row === null) return false;

    [left, right] = [0, matrix[0].length - 1];
    while (left <= right) {
        const mid = Math.floor((right - left) / 2) + left;
        if (target < matrix[row][mid]) right = mid - 1;
        else if (target > matrix[row][mid]) left = mid + 1;
        else return true;
    }
    return false;
};
