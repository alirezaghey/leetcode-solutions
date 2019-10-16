// https://leetcode.com/problems/triangle/
// Related Topics: Array, Dynamic Programming
// Difficulty: Medium

/*
Initial thoughts:
Looking at the triangle like a binary tree enables us to try out
every possible root to leaf path looking for the path with the
minimum sum of values. This can be done in a DFS approach, our
base case will be when our current depth equals the length of the
triangle. This would have a time complexity of O(2^depth) which in
this case is more than O(n) where n is the number of elements in the
whole triangle. That's is because every deper level of row in the triangle
has only one more element compared to the row above it and not double
the elements like it would be in a real binary tree.
Without dynamic programming our solution would exceed the time limit.

Time complexity: O(2^depth) where depth == len(triangle)
Space complexity: O(depth) where depth == len(triangle)
from typing import List
*/

/**
 * @param {number[][]} triangle
 * @return {number}
 */
const minimumTotal = triangle => {
  return dfs(0, 0);
  function dfs(idx, depth) {
    if (depth == triangle.length) return 0;

    return (
      Math.min(dfs(idx, depth + 1), dfs(idx + 1, depth + 1)) +
      triangle[depth][idx]
    );
  }
};

/*
 Optimization:
 By caching the results for each node
 we can render the time complexity of our solution linear.

 Time Complexity: O(n) where n is the number of elements in the whole triangle
 Space Complexity: O(n) where n is the number of elements in the whole triangle
*/
/**
 * @param {number[][]} triangle
 * @return {number}
 */
const minimumTotal = triangle => {
  const dp = [];
  for (let i = 0; i < triangle.length; i++) dp.push(Array(i + 1));
  return dfs(0, 0);
  function dfs(idx, depth) {
    if (depth == triangle.length) return 0;

    if (dp[depth][idx] === undefined)
      dp[depth][idx] =
        Math.min(dfs(idx, depth + 1), dfs(idx + 1, depth + 1)) +
        triangle[depth][idx];
    return dp[depth][idx];
  }
};

/*
 Optimization:
 While doing this problem in a recursive manner may be better
 illustration and solving purposes, it is more efficient space-wise
 if we solve it iteratively. It is still linear in terms of space but
 the extra space for the recursive stack is saved

 Time Complexity: O(n) where n is the number of elements in the whole triangle
 Space Complexity: O(n) where n is the number of elements in the whole triangle
*/
/**
 * @param {number[][]} triangle
 * @return {number}
 */
const minimumTotal = triangle => {
  if (triangle.length === 1) return triangle[0][0];

  const dp = [];
  for (let i = 0; i < triangle.length; i++) dp.push(Array(i + 1));
  for (let i = 0; i < triangle[triangle.length - 1] - 1; i++)
    dp[triangle.length - 1][i] = triangle[triangle.length - 1][i];

  for (let i = triangle.length - 2; i >= 0; i--) {
    for (let j = 0; i < triangle[i].length; i++) {
      dp[i][j] = Math.min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j];
    }
  }
  return dp[0][0];
};
/*
 Optimization:
 Now, since we only need the results of one row (the previous) at a time
 we are going to reduce the auxilliary space to a one dimensional array
 that has the length of the depth of the triangle (that is the same as the last
 row of the tirangle)

 Time Complexity: O(n) where n is the number of elements in the whole triangle
 Space Complexity: O(m) where m is the number of elements in the last row
 of the triangle
*/
/**
 * @param {number[][]} triangle
 * @return {number}
 */
const minimumTotal = triangle => {
  if (triangle.length === 1) return triangle[0][0];

  const dp = [];
  for (const el of triangle[triangle.length - 1]) dp.push(el);

  for (let i = triangle.length - 2; i >= 0; i--) {
    for (let j = 0; j < triangle[i].length; j++) {
      dp[j] = Math.min(dp[j], dp[j + 1]) + triangle[i][j];
    }
  }
  return dp[0];
};
