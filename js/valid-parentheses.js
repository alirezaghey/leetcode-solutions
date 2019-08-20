// Related Topics: String, Stack
// Difficulty: Easy

/*
Initial thoughts:
Creating a lookup table for all the types of parentheses and
using a stack we touch every element of the input string and
if it's an opening parenthes push it on the stack and if its
a closing parenthes we pop one from the stack checking if it's
a valid counterpart for the current parenthes.
At the end, the stack must be empty

Time complexity: O(n) where n === s.length
Space complexity: O(n) where n === s.length

*/
/**
 * @param {string} s
 * @return {boolean}
 */
const isValid = s => {
  const stack = [];

  for (let i = 0; i < s.length; i++) {
    const temp = s[i];
    if (opening[temp]) stack.push(temp);
    else if (stack.pop() !== closing[temp]) return false;
  }
  return stack.length === 0;
};

const opening = { '(': ')', '[': ']', '{': '}' };
const closing = { ')': '(', ']': '[', '}': '{' };
