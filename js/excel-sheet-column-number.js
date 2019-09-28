// https://leetcode.com/problems/excel-sheet-column-number/
// Related Topics: Math
// Difficulty: Easy

/*
Initial thoughts:
This is like a base 26 number system where the alphabet letters represent 1 through 26.
We need to convert their ascii code to the number they represent by subtracting 64 (since
they are captical letters and A has the number 65)
In addition we have to take care of their position. In a one letter "number", "A" represents
1, while if one letter is added to its right, it represents 26. This can be remedied by
multiplying our number by 26 each time we calculate the value of a new letter and add it to it.

Time complexity: O(n) where n === the length of s
Space complexity: O(1)
*/

/**
 * @param {string} s
 * @return {number}
 */
const titleToNumber = s => {
  let result = 0;
  for (let i = 0; i < s.length; i++) {
    result *= 26;
    result += s.charCodeAt(i) - 64;
  }
  return result;
};
