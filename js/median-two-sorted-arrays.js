https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/
// Related Topics: Array, Binary Search, Divide and Conquer
// Difficulty: Easy

/*
Initial thoughts:
A brute force solution is to merge the input arrays
and find the median. This will cost more in terms of time
and space but is a simple and robust solution.

Time complexity: O(n+m) where n === input1.length and m === input2.length
Space complexity: O(n+m) where n === input1.length and m === input2.length
*/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
const findMedianSortedArrays = (nums1, nums2) => {
  const mergedNums = [];
  const [nums1Length, nums2Length] = [nums1.length, nums2.length];
  let i = (j = 0);

  while (i < nums1Length || j < nums2Length) {
    if (!(j < nums2Length) || (i < nums1Length && nums1[i] <= nums2[j])) {
      mergedNums.push(nums1[i]);
      i++;
    } else {
      mergedNums.push(nums2[j]);
      j++;
    }
  }

  const mid = Math.floor(mergedNums.length / 2);
  if (mergedNums.length % 2 === 0)
    return (mergedNums[mid - 1] + mergedNums[mid]) / 2;
  else return mergedNums[mid];
};

/*
Optimization:
Considering the definition of *median*, we can build a more efficient
algorithm in terms of both space and complexity.

The median is the middle element of an odd-length array and the average
of the two middle elements of an even-length array.

Let's call the smaller array (in terms of its elements) X, and the other
array Y.
If we find a point z in X that partitions the array in a left and a right part,
and take its corresponding point w in Y that partitions the array in a left and right part
such that:
1. xLeft.length + yLeft.length === xRight.length + yRight.length
2. max(xLeft) <= min(yRight)
3. max(yLeft) <= min(xRight)

We have found our guy. In that case:
1. If the number of all elements is odd, return max(xLeft, yLeft)
2. If the number of all elements is even, return (max(xLeft, yLeft)/ min(xRight, yRight)) / 2

But if max(xLeft) > min(yRight):
Our partition (z) is too much to the right and we need to move it to the left.
Otherwise:
Our partition (z) is too much to the left and we need to move it to the right.

Time complexity: O(log min(n,m)) where n === nums1.length and m === nums2.length
Space complexity: O(1) yeeey!
*/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
const findMedianSortedArrays = (numsX, numsY) => {
  if (numsX.length > numsY.length) [numsX, numsY] = [numsY, numsX];

  const lenX = numsX.length;
  const lenY = numsY.length;

  let minPartX = 0;
  let maxPartX = lenX;

  while (minPartX <= maxPartX) {
    const partX = Math.floor((minPartX + maxPartX) / 2);
    const partY = Math.floor((lenX + lenY + 1) / 2) - partX;

    // if the partition is right at the beginning or the end of the array
    // we substitute max/min possible value for the missing value
    const maxLeftX = partX === 0 ? Number.MIN_SAFE_INTEGER : numsX[partX - 1];
    const minRightX = partX === lenX ? Number.MAX_SAFE_INTEGER : numsX[partX];

    const maxLeftY = partY === 0 ? Number.MIN_SAFE_INTEGER : numsY[partY - 1];
    const minRightY = partY === lenY ? Number.MAX_SAFE_INTEGER : numsY[partY];

    if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
      // We found the right point, calculate the media
      // based on even or odd situation
      if ((lenX + lenY) % 2 === 0)
        return (
          (Math.max(maxLeftX, maxLeftY) + Math.min(minRightX, minRightY)) / 2
        );
      else return Math.max(maxLeftX, maxLeftY);
    } else if (maxLeftX > minRightY)
      // We are to much to the right
      maxPartX = partX - 1;
    // We are too much to the left
    else minPartX = partX + 1;
  }

  // This should only happen if the arrays are not sorted
  throw 'Array not sorted propertly!';
};
