// https://leetcode.com/problems/remove-element/
// Related Topics: Array, Two Pointers
// Difficulty: Easy

/*
Initial thoughts:
In order to achieve the goald of removing invalid elements
from the array with O(1) extra space we are going to use two pointers
where the first points to the end of the clean array and the second to
the current element.
Moving forward with the current pointer we copy each valid element to the
head of the clean array and increment the pointer to the head of the clean
array by one.

Time complexity: O(n) where n === array.length
Space complexity: O(1)
*/

/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
const removeElement = (nums, val) => {
  let headOfCleanArr = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== val) {
      nums[headOfCleanArr] = nums[i];
      headOfCleanArr++;
    }
  }
  return headOfCleanArr;
};
