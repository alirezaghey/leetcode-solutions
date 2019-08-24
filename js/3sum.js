// https://leetcode.com/problems/3sum/
// Related Topics: Array, Two Pointers
// Difficulty: Medium

/*
Initial thoughts:
Sorting the array and using a two pointer approach
we are going to loop over every element in the array.
We create two pointers for the rest of the elements
and check whether they create a solution, all the while
checking that the values are unique.

Time complexity: O(n^2)
Space complexity: O(n);
*/

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
const threeSum = nums => {
  nums.sort((a, b) => a - b);
  const result = [];
  for (let i = 0; i < nums.length; i++) {
    // skipping duplicates
    if (i !== 0 && nums[i] === nums[i - 1]) continue;
    let left = i + 1;
    let right = nums.length - 1;
    while (left < right) {
      const s = nums[i] + nums[left] + nums[right];
      // too small; move to the right
      if (s < 0) left++;
      // too big; move to the left
      else if (s > 0) right--;
      // bingo
      else {
        result.push([nums[i], nums[left], nums[right]]);
        // skipping duplicates
        while (left + 1 < right && nums[left] === nums[left + 1]) left++;
        while (right - 1 > left && nums[right] === nums[right - 1]) right--;
        left++;
        right--;
      }
    }
  }
  return result;
};
