// https://leetcode.com/problems/reverse-only-letters/
// Related Topics: String
// Difficulty: Easy

/*
Initial thoughts:
Using two pointer at the beginning and end of the string we check
whether they are a letter or not. If any of them is not a letter we
only move that character to the inside of the array, if not we swapp
the letters at thos character and move both of them to the inside.
Repeat until the two pointers meet.

Time complexity: O(n) where n === the length of S
Space complexity: O(n) where n === the length of S (the auxilliary space is actually because string are immutable in JS)
*/

/**
 * @param {string} S
 * @return {string}
 */
const reverseOnlyLetters = S => {
  const arrS = S.split('');
  let left = 0;
  let right = arrS.length - 1;
  while (left < right) {
    if (!arrS[left].match(/[a-z]/i)) {
      left++;
      continue;
    }
    if (!arrS[right].match(/[a-z]/i)) {
      right--;
      continue;
    }
    [arrS[left], arrS[right]] = [arrS[right], arrS[left]];
    left++;
    right--;
  }
  return arrS.join('');
};
