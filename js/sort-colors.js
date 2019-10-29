// https://leetcode.com/problems/sort-colors/
// Related Topics: Array, Two Pointers, Sort
// Difficulty: Medium

/*
Initial thoughts:
Since we are dealing with a small and predefined set of possiblities (3 colors in this case)
we can loop once over the array, creating a frequency table for the 3 colors and then fill
the array according to the freq table.

Time Complexity: O(n) where n == the number of elements in the nums array
Space Complexity: O(1) (the extra space required for the freq table is constant)
*/

/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
const sortColors = nums => {
    const count = Array(3).fill(0);
    for (el of nums) count[el]++;
    let c = 0;
    for (i = 0; i < count.length; i++) {
        for (j = 0; j < count[i]; j++) {
            nums[c++] = i;
        }
    }
};

/*
Optimization:
We can solve this problem in one pass instead of two. The idea is based on the fact that
the sort space in limited two only three distinct individuals. This allows us to have a pointer
at the front, one at the back and swap the colors that belong to the front or the back with them
while moving forward. This way, the color that belongs to the middle will end up at the middle.
There is just one catch: when swapping the current element with the one at the back (bc it belongs
to the back), we can't move our current pointer forward, because the element that we swapped with
could belong to the back (e.g. [2,0,2])

Time Complexity: O(n) where n == the number of elements in the nums array
Space Complexity: O(1) (the extra space required for the freq table is constant)
*/

/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
const sortColors = nums => {
    let left = (curr = 0);
    let right = nums.length - 1;

    while (curr <= right) {
        if (nums[curr] === 0) {
            [nums[curr], nums[left]] = [nums[left], nums[curr]];
            curr++;
            left++;
        } else if (nums[curr] === 2) {
            [nums[curr], nums[right]] = [nums[right], nums[curr]];
            right--;
        } else curr++;
    }
};
