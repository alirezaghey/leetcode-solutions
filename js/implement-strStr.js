// https://leetcode.com/problems/implement-strstr/
// Related Topics: String, Two Pointers
// Difficulty: Easy

/*
Initial thoughts:
The brute force solution works with two pointers that checks
every substring of the haystack for a match with needle.

Time complexity: O(n*m) where n === haystack.length and m === needle.length
Space complexity: O(1)
*/

/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
const strStr = (haystack, needle) => {
  if (needle.length === 0 || haystack === needle) return 0;
  for (let i = 0; i < haystack.length - needle.length; i++) {
    if (haystack[i] !== needle[0]) continue;
    for (let j = 0; j < needle.length; j++) {
      if (haystack[i + j] !== needle[j]) break;
      if (j === needle.length - 1) return i;
    }
  }
  return -1;
};
