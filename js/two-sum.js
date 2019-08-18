/*
Initial thoughts:
Comparing each and every element of the array
with the remaining elements after that specific one,
we check whether they add up to the target value and
return the indices.

Time complexity: O(n^2)
Space complexity: O(1)

*/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) return [i, j];
    }
  }
};

/*
Optimization:
We could set up a lookup dictionary to reduce the
time complexity of the inner loop to O(1), trading space
for time.

Time complexity: O(n)
Space complexity: O(n)

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
  const lookup = {};
  nums.forEach((num, i) => (lookup[num] = i));

  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];
    if (lookup[complement] !== undefined && lookup[complement] !== i)
      return [i, lookup[complement]];
  }
};

/*
Optimization:
We can furhter optimize our solution to check for the complement
and fill the lookup dictionary in one go.

Time complexity: O(n)
Space complexity: O(n)
*/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
  const lookup = {};

  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];
    if (lookup[complement] !== undefined) return [lookup[complement], i];
    else lookup[nums[i]] = i;
  }
};
