// https://leetcode.com/problems/flood-fill/
// Related Topics: BFS, DFS
// Difficulty: Easy

/*
Initial thoughts:
Starting with the initial pixel we can approach the problem in a BFS manner.
Change the first pixel and enqueue its 4-directionally adjacent pixels if they
comply with the criterion of having the old color and are in bounds with regards
to the original pixel.

Time complexity: O(n) where n === number of elements in image
Space complexity: O(n) where n === number of leements in image
*/

/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} newColor
 * @return {number[][]}
 */
const floodFill = (image, sr, sc, newColor) => {
  const [R, C] = [image.length, image[0].length];
  const oldColor = image[sr][sc];
  if (oldColor === newColor) return image;
  let currPixels = [[sr, sc]];

  let newPixels = [];
  while (currPixels.length > 0) {
    const [r, c] = currPixels.pop();
    image[r][c] = newColor;
    if (r > 0 && image[r - 1][c] === oldColor) newPixels.push([r - 1, c]);
    if (c + 1 < C && image[r][c + 1] === oldColor) newPixels.push([r, c + 1]);
    if (r + 1 < R && image[r + 1][c] === oldColor) newPixels.push([r + 1, c]);
    if (c > 0 && image[r][c - 1] === oldColor) newPixels.push([r, c - 1]);

    if (currPixels.length === 0) {
      currPixels = newPixels;
      newPixels = [];
    }
  }
  return image;
};

/*
Using a DFS approach.
Time and space complexities don't change in comparison to BFS.
This approach is arguable more elegant, readable, but IMHO
it "looks" less like a flood fill and if investigating, simulating
or depicting of a flood fill was in order, DFS couldn't do it.
*/

/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} newColor
 * @return {number[][]}
 */
const floodFill = (image, sr, sc, newColor) => {
  const [R, C] = [image.length, image[0].length];
  const oldColor = image[sr][sc];
  if (oldColor === newColor) return image;
  const dfs = (r, c) => {
    image[r][c] = newColor;
    if (r > 0 && image[r - 1][c] === oldColor) dfs(r - 1, c);
    if (c + 1 < C && image[r][c + 1] === oldColor) dfs(r, c + 1);
    if (r + 1 < R && image[r + 1][c] === oldColor) dfs(r + 1, c);
    if (c > 0 && image[r][c - 1] === oldColor) dfs(r, c - 1);
  };

  dfs(sr, sc);
  return image;
};
