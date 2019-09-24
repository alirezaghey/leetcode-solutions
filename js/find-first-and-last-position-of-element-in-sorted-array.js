// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
// Related Topics: Array, Binary Search
// Difficulty: Medium

/*
Initial thoughts:
A naive approach is to look at every element of nums to find the beginning
and end of target. This approach's Time complexity is O(n).

To reduce the Time complexity to O(log n) we are going to use binary search.
Let's say we find target at nums[i]. If nums[i-1] === nums[i] we are going to
binary search againt for target between 0 and i and repeat this process until
we find an index k where either k === 0 or nums[k-1] < nums[k].
The same goes for the right bound of our range. If nums[i+1] === nums[i]
we are going to binary search for target between i and nums.length-1 until we
find an index k where either k === nums.length-1 or nums[k] < nums[k+1].
This will be a multitude of log ns at most.

Time complexity: O(log n) where n === nums.length
Space complexity: O(log n);
*/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
const searchRange = (nums, target) => {
  const index = binarySearch(nums, target, 0, nums.length - 1);
  if (index === -1) return [-1, -1];

  // Find left bound
  let left = index;
  while (left > 0 && nums[left] === nums[left - 1]) {
    left = binarySearch(nums, target, 0, left - 1);
  }

  // Find right bound
  let right = index;
  while (right < nums.length - 1 && nums[right] === nums[right + 1]) {
    right = binarySearch(nums, target, right + 1, nums.length - 1);
  }
  return [left, right];
};

const binarySearch = (arr, target, low, high) => {
  if (low > high) return -1;
  const mid = low + Math.floor((high - low) / 2);
  if (arr[mid] === target) return mid;
  else if (arr[mid] > target) return binarySearch(arr, target, low, mid - 1);
  else return binarySearch(arr, target, mid + 1, high);
};

/*
Optimization:
Using an iterative binary search algorithm we can render the space complexity constant

Time complexity: O(log n)
Space complexity: O(1)

*/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
const searchRange = (nums, target) => {
  const index = binarySearchIterative(nums, target, 0, nums.length - 1);
  if (index === -1) return [-1, -1];

  // Find left bound
  let left = index;
  while (left > 0 && nums[left] === nums[left - 1])
    left = binarySearchIterative(nums, target, 0, left - 1);

  // Find right bound
  let right = index;
  while (right < nums.length - 1 && nums[right] === nums[right + 1])
    right = binarySearchIterative(nums, target, right + 1, nums.length - 1);

  return [left, right];
};
const binarySearchIterative = (arr, target, low, high) => {
  while (low <= high) {
    mid = low + Math.floor((high - low) / 2);
    if (arr[mid] === target) return mid;
    else if (arr[mid] > target) high = mid - 1;
    else low = mid + 1;
  }
  return -1;
};
