// https://leetcode.com/problems/length-of-last-word/
// Related Topics: String
// Difficulty: Easy

/*
Initial thoughts:
Looping over the characters of the string in reverse order
we are going to look for a space character and return the
length of the last word (length - (i + 1)). Watch the -1. Since i
indicated the index of the whitespace, the length of the word
we are looking for start at the next character.

Time complexity: O(n) where n === s.length
Space complexity: O(1)

*/

/**
 * @param {string} s
 * @return {number}
 */
const lengthOfLastWord = s => {
  s = s.trim();
  for (var i = s.length - 1; i >= 0; i--) {
    if (s[i] === ' ') break;
  }
  return s.length - (i + 1);
};

/*
Regex solution
*/

/**
 * @param {string} s
 * @returns {number}
 */
const lengthOfLastWord = s => {
  s = s.trim();
  m = s.match(/[^ ]+$/);
  return m ? m[0].length : 0;
};
