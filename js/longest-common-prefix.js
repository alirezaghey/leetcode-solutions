// https://leetcode.com/problems/longest-common-prefix/
// Related Topics: String, Array
// Difficulty: Easy

/*
Initial thoughts:
We are going to look at each index of every string
at the same time, comparing them to their counterpart
in the first string, adding the character to our results
if all of the strings have the same character, and returning
the results in case of a difference.

Time complexity: O(n * min(s)) where s is the length of the longest common prefix
Space complexity: O(min(s)) where s is the length of the longest common prefix

*/

/**
 * @param {string[]} strs
 * @return {string}
 */
const longestCommonPrefix = strs => {
  if (!strs.length) return '';
  const result = [];
  for (let i = 0; i < strs[0].length; i++) {
    for (let j = 1; j < strs.length; j++) {
      if (strs[0][i] !== strs[j][i]) return result.join('');
    }
    result.push(strs[0][i]);
  }
  return result.join('');
};

/*
Optimization:
Using the counter variable we can forgoe the result tracking variable
and just slice and return it at the end, rendering the space complexity constant.

Time complexity: O(n * min(s)) where s is the length of the longest common prefix
Space complexity: O(1)
*/

/**
 * @param {string[]} strs
 * @return {string}
 */
const longestCommonPrefix = strs => {
  if (!strs.length) return '';
  for (var i = 0; i < strs[0].length; i++) {
    for (let j = 1; j < strs.length; j++) {
      if (strs[0][i] !== strs[j][i]) return strs[0].substr(0, i);
    }
  }
  return strs[0].substr(0, i);
};
