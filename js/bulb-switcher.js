// https://leetcode.com/problems/bulb-switcher/
// Related Topics: Math, Brainteaser
// Difficulty: Medium

// Time complexity: O(sqrt(n)) where n is the number of nodes in the Linked List
// Space complexity: O(1)

/**
 * @param {number} n
 * @return {number}
 */
const bulbSwitch = n => {
  return Math.sqrt(n) | 0;

  // count = 0;
  // for (let i = 1; i*i <= n; i++) count++
  // return count
};
