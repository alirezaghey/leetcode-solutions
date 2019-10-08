// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
// Related Topics: Array, Stack, Two Pointers
// Difficulty: Medium

/*
Initial thoughts:
Using a stack we can track the number of adjacent characters while checking
the value and current count of the latest character in constant time. If the
count equals the threshold we can just pop the character with one move and
will have access to the (possible) previous character and its count.

Time complexity: O(n) where n === len(s)
Space complexity: O(n) where n === len(s) (that is for the worst case scenario
where all there are no adjacent matching chars))
*/

/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
const removeDuplicates = (s, k) => {
  const stack = [['#', 0]];

  for (let c of s) {
    if (stack[stack.length - 1][0] === c) {
      stack[stack.length - 1][1]++;
      if (stack[stack.length - 1][1] === k) stack.pop();
    } else stack.push([c, 1]);
  }

  return stack.map(el => el[0].repeat(el[1])).join('');
};
