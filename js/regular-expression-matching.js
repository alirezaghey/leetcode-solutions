// https://leetcode.com/problems/regular-expression-matching/
// Related Topics: String, Dynamic Programming, Backtracking
// Difficulty: Hard

/*
Initial thoughts:
Using dynamic programming we are going to create a two
dimensional matrix where the rows' index indicates the position
in our string and the columns' index indicates the position
in our pattern.
matrix[0][0] is always true, because an empty string always matches
with an empty pattern.
The rest of the first row and column are all false, because there can't
be a non-empty string that matches an empty pattern and vice-versa.
For a string to match with a pattern up to a specific character,
matrxi[i][j] must be true.

Conditions for solving the matrix is as follows:
1- if (str[i] === pattern[j] || pattern[j] === ".") => matrix[i][j] = matrix[i-1][j-1]
2- if (patter[j] === "*") =>
    2a- if (str[i] === pattern[j-1] || pattern[j-1] === ".") => matrxi[i][j] = matrix[i-1][j]
    2b- else matrix[i][j] = matrxi[i][j-2] (zero occurence)

Time complexity: O(n*m) where n === str.length and m === pattern.length
Space complexity: O(n*m)
*/

/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
const isMatch = (s, p) => {
  // creating the matrix;
  const matchMatrix = [];
  for (let i = 0; i < s.length + 1; i++)
    matchMatrix.push(new Array(p.length + 1));

  // [0][0] is always true
  matchMatrix[0][0] = true;

  // initializing the first row and dealing with patterns like "a*b*c*"
  for (let i = 1; i < matchMatrix[0].length; i++) {
    if (p[i - 1] === '*') matchMatrix[0][i] = matchMatrix[0][i - 2];
    else matchMatrix[0][i] = false;
  }

  for (let i = 1; i < matchMatrix.length; i++) {
    for (let j = 1; j < matchMatrix[0].length; j++) {
      if (s[i - 1] === p[j - 1] || p[j - 1] === '.')
        matchMatrix[i][j] = matchMatrix[i - 1][j - 1];
      else if (p[j - 1] === '*') {
        matchMatrix[i][j] = matchMatrix[i][j - 2];
        if (s[i - 1] === p[j - 2] || p[j - 2] === '.')
          matchMatrix[i][j] = !!(matchMatrix[i][j] | matchMatrix[i - 1][j]);
      } else matchMatrix[i][j] = false;
    }
  }
  return !!matchMatrix[s.length][p.length];
};

/*
Simple solution using JS native regex facilities :)
*/

/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
const isMatch = (s, p) => {
  return new RegExp(`^${p}$`).test(s);
};
