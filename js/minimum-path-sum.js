// https://leetcode.com/problems/minimum-path-sum/
// Related Topics: Array, Dynamic Programming
// Difficulty: Medium

/*
Initial thoughts:
We can look at the problem as a tree where each cell is a node in the tree
that is connected to two other cells (one to its right and one to its bottom)
We are looking for the minimum path sum that lead to a leaf node (all the leaf
nodes are the bottom right cell in our matrix)
In other words, we have to look at all the possible sums that lead to the bottom
right cell and return the minimum.
Since this problem has an overlapping substructure, we can avoid redundant calculations
by using memoization. At each state if the data is available we are going to retrieve it,
otherwise we are going to fill it.

Time complexity: O(n) where n == number of cells in the grid
Space complexity: O(n) where n == number of cells in the grid. In a worst case scenario,
where our grid has only one row or one column, the recursive stack's depth will equal
the number of cells in the grid. In addition, our memoization grid needs to havev as much
cells as the original grid.
*/

/**
 * @param {number[][]} grid
 * @return {number}
 */
const minPathSum = grid => {
    if (!grid || !grid.length || !grid[0].length) return 0;

    const R = grid.length;
    const C = grid[0].length;

    const dp = Array(R)
        .fill(null)
        .map(() => Array(C).fill(undefined));

    return dfs(0, 0);

    function dfs(row, col) {
        if (row === R - 1 && col === C - 1) return grid[row][col];

        if (dp[row][col] !== undefined) return dp[row][col];

        let right = (bottom = Number.POSITIVE_INFINITY);

        if (col < C - 1) right = dfs(row, col + 1);
        if (row < R - 1) bottom = dfs(row + 1, col);

        dp[row][col] = grid[row][col] + Math.min(right, bottom);
        return dp[row][col];
    }
};

/*
Optimization:
Using a dynamic programming approach, we can fill the grid in a tabular way always looking
for how to reach the next cell with minimum costs and build on that calculation for calculating
the minimum cost for reaching the next cell.

Time complexity: O(n) where n == number of cells in the grid
Space complexity: O(1)
*/

/**
 * @param {number[][]} grid
 * @return {number}
 */
const minPathSum = grid => {
    if (!grid || !grid.length || !grid[0].length) return 0;

    const R = grid.length;
    const C = grid[0].length;

    for (let i = 1; i < C; i++) grid[0][i] += grid[0][i - 1];

    for (let i = 1; i < R; i++) grid[i][0] += grid[i - 1][0];

    for (let i = 1; i < R; i++)
        for (let j = 1; j < C; j++)
            grid[i][j] += Math.min(grid[i - 1][j], grid[i][j - 1]);

    return grid[R - 1][C - 1];
};
