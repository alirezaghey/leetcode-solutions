// https://leetcode.com/problems/merge-sorted-array/
// Related Topics: Array, Two Pointers
// Difficulty: Easy

/*
Initial thoughts:
Using two pointers we are going to compare the elements of nums1 and nums2
and fill nums1 from tail to head.

Time complexity: O(n + m) where n + m === nums1.length
Space complexity: O(1)

*/

/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
const merge = (nums1, m, nums2, n) => {
  let pNums1 = m - 1,
    pNums2 = n - 1;

  while (pNums1 >= 0 || pNums2 >= 0) {
    if (pNums2 < 0 || (pNums1 >= 0 && nums1[pNums1] > nums2[pNums2])) {
      nums1[pNums1 + pNums2 + 1] = nums1[pNums1];
      pNums1--;
    } else {
      nums1[pNums1 + pNums2 + 1] = nums2[pNums2];
      pNums2--;
    }
  }
};
