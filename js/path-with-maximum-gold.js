// https://leetcode.com/problems/path-with-maximum-gold/
// Related Topics: DFS, Backtracking
// Difficulty: Medium

/*
Initial thoughts:
Aside from the starting cell, each cell has at most three paths that go out of it
(that's because we can't go back to our previous cell since we have already visited it).
We need to recursively check every possibility to find the optimal solution.
Using backtracking to investigate every possible path from a given starting cell
we are going to search for the maximum value. The backtracking will be implemented
in a depth first approach, since this will take less auxilliary space and is also
more natural to implement.
Since we can start our search at any cell in the grid, we are going to apply this
algorithm to every cell of the grid as the starting point.

Time complexity: O(n*m*3^(m*n)) [THIS IS NOT CORRECT! NEEDS REVIEW] where n === grid width and m === grid heigth
Space complexity: O(n) where n === number of cells in the grid. This is the worst case
where our algorithm is able to visit each and every cell in a given path and so the depth
of our virtual tree equals the number of nodes in it.
*/

/**
 * @param {number[][]} grid
 * @return {number}
 */
const getMaximumGold = grid => {
  if (grid.length === 0 || grid[0].length === 0) return 0;

  const [R, C] = [grid.length, grid[0].length];

  let max = Number.MIN_VALUE;
  for (let r = 0; r < R; r++)
    for (let c = 0; c < C; c++) max = Math.max(max, dfs(r, c, 0));
  return max;

  function dfs(r, c, curr) {
    if (r < 0 || r >= R || c < 0 || c >= C || grid[r][c] === 0) return curr;

    const temp = grid[r][c];
    grid[r][c] = 0;

    const top = dfs(r - 1, c, curr + temp);
    const right = dfs(r, c + 1, curr + temp);
    const bottom = dfs(r + 1, c, curr + temp);
    const left = dfs(r, c - 1, curr + temp);

    grid[r][c] = temp;
    return Math.max(top, right, bottom, left);
  }
};
