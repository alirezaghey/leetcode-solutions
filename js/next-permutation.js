// https://leetcode.com/problems/next-permutation/
// Related Topics: Array
// Difficulty: Medium

/*
Initial thoughts:
In order to create the next permutation, we need to think about how a permutation
is build from its smallest value (lexicographically or mathematically) to it greatest
and just take that approach one step further.
Suppose we have (2,3,1). We would sort the numbers ascending
coming to (1,2,3). Now let's create the six permutations for this:
(1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2), (3,2,1)
Let's do another one (1,2,3,4). We will have:
(1,2,3,4), (1,2,4,3), (1,3,2,4), (1,3,4,2), (1,4,2,3), (1,4,3,2),...
Let's do another one (1,2,3,4,5). We will have:
(1,2,3,4,5), (1,2,3,5,4), (1,2,4,3,5), (1,2,4,5,3), (1,2,5,3,4), (1,2,5,4,3), (1,3,2,4,5)
A pattern is starting to emerge:
It appears that to create the next permutation, we need to look from right to left and
find the first occurence where nums[i] > nums[i-1]. Now, we can't just swap nums[i] with
nums[i-1] because we could skip some permutations and get a much bigger than just the next one.
The solution is to take the smallest number after nums[i-1] that is just greater than nums[i-1]
ans swap it with nums[i-1]. The remaining numbers after num[i-1] need to be added after nums[i-1]
ascending.
The thing is that they are already sorted, just in descending order, so we need to reverse the numbers after num[i-1]

Time complexity: O(n) where n == length of nums
Space complexity: O(1)

*/

/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
const nextPermutation = nums => {
  // Find first occurence where nums[i] > nums[i-1]
  for (var i = nums.length - 2; i >= 0; i--) {
    if (nums[i] < nums[i + 1]) break;
  }
  if (i < 0) {
    // This is already the greatest permutation possible. Return reversed nums as required
    let j = nums.length - 1;
    let k = 0;
    while (k < j) {
      [nums[k], nums[j]] = [nums[j], nums[k]];
      k++;
      j--;
    }
    return;
  }
  // Find the first occurence (from right) of the smallest number that is just greater than nums[i]
  let index = -1;
  for (let j = nums.length - 1; j > i; j--) {
    if (nums[j] > nums[i]) {
      if (index === -1) index = j;
      else if (nums[j] < nums[index]) index = j;
    }
  }

  // swap nums[i] with the smallest number in the right partition that is just greater than itself
  [nums[i], nums[index]] = [nums[index], nums[i]];

  // reverse everything after nums[i] and return
  let j = nums.length - 1;
  let k = i + 1;
  while (k < j) {
    [nums[k], nums[j]] = [nums[j], nums[k]];
    k++;
    j--;
  }
  return;
};
