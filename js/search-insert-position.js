// https://leetcode.com/problems/search-insert-position/
// Related Topics: Array, Binary Search
// Difficulty: Easy

/*
Initial thoughts:
The brute force solution is to loop over all the elements
all the while checking if they equal the searched value or
are greater than the search value and return that index.
If no match is found, the element would be inserted at the
end of the array and our answer would be the array length -1.

Time complexity: O(n) where n === nums.length
Space complexity: O(1)
*/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
const searchInsert = (nums, target) => {
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] >= target) return i;
  }
  return nums.length;
};

/*
/*
Optimization:
Considering the fact that the input array is sorted
we can use binary search to find our target, reducing
our time complexity to log n.

Time complexity: O(log n) where n === nums.length
Space complexity: O(1)
*/

/**
 * @param {number[]} nums
 * @param {number} target
 * @returns {number}
 */
const searchInsert = (nums, target) => {
  let low = 0;
  let high = nums.length - 1;
  let mid = 0;
  while (low <= high) {
    mid = Math.floor((high - low) / 2 + low);
    if (nums[mid] > target) {
      high = mid - 1;
    } else if (nums[mid] < target) {
      low = mid + 1;
    } else return mid;
  }
  // target was not found; return insertion position
  return target > nums[mid] ? ++mid : mid;
};
