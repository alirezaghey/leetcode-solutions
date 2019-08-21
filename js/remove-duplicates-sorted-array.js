// Related Topics: Array, Two Pointers
// Difficulty: Easy

/*
Initial thoughts:
Since we want to remove the duplicates in place we're going to
use two pointers, increasing the first each time we fine a new
unique element and assigning that element to its previous place.

Time complexity: O(n) where n is the number of elements
Space complexity: O(1)

*/

/**
 * @param {number[]} nums
 * @return {number}
 */
const removeDuplicates = nums => {
  let i = 0;
  for (let j = 1; j < nums.length; j++) {
    if (nums[i] !== nums[j]) {
      i++;
      nums[i] = nums[j];
    }
  }
  return ++i;
};
