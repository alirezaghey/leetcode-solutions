// https://leetcode.com/problems/minimum-absolute-difference/
// Related Topics: Array
// Difficulty: Easy

/*
Initial thoughts:
First we need to find the minimum absolute difference between any two elements in the array.
This can be done by comparing each element with every other element which would take O(n^2)
or we could sort the array and then compare adjacent elements to find the min difference, which
takes O(n * log n).
Then we need to find every pair that has the same absolute difference as the min diff. This could
also be done in O(n^2) or we could work on the sorted array and only compare adjacent arrays. This
takes only O(n)

Time complexity: O(n * log n) where n === len(arr)
Space complexity: O(n) where n === len(arr) That's for the results array in case every pair in the
original array is an answer
*/

/**
 * @param {number[]} arr
 * @return {number[][]}
 */
const minimumAbsDifference = arr => {
  arr.sort((a, b) => a - b);
  let minDiff = Number.MAX_VALUE;

  for (let i = 1; i < arr.length; i++)
    minDiff = Math.min(minDiff, arr[i] - arr[i - 1]);
  const result = [];
  for (let i = 1; i < arr.length; i++)
    if (arr[i] - arr[i - 1] === minDiff) result.push([arr[i - 1], arr[i]]);
  return result;
};

/*
Optimization:
We can calculate the result (the correct pairs) in one go while we are
culculating the minimum difference. When working on a sorted array we can
be sure that if we find a new minimum difference, the previous results are
of no value anymore and the pair that created the new min difference also
belongs to the results array. While checking for the minimum diff, if we
find a diff that equals our previous minimum diff, we also know that the
result array until now is correct and this very new pair also belongs to it.
For other differences that are above the current min diff, we can be sure
that they are of no value to us.

Time complexity: O(n * log n)
Space complexity: O(n)
*/

/**
 * @param {number[]} arr
 * @return {number[][]}
 */
const minimumAbsDifference = arr => {
  arr.sort((a, b) => a - b);
  minDiff = Number.MAX_VALUE;
  let result = [];
  for (let i = 1; i < arr.length; i++) {
    const temp = arr[i] - arr[i - 1];
    if (temp < minDiff) {
      minDiff = temp;
      result = [[arr[i - 1], arr[i]]];
    } else if (temp === minDiff) result.push([arr[i - 1], arr[i]]);
  }
  return result;
};
