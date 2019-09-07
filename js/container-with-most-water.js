// https://leetcode.com/problems/container-with-most-water/
// Related Topics: Array, Two Pointers
// Difficulty: Medium

/*
Initial thoughts:
We need to maximize the area between two bars (containers).
The area is always the distance between the bars times the smaller bar.
The brute force solution is to test each bar with all the others, which
gives an O(n^2) solution.
But we could greately optimize our solution with a two pointer approach.
We start at both ends of the x axis and take the distance between the bars
times the shorter bar. The we move the short bar towards the other and test
again for maximum.
We can be sure that this approach works because we wouldn't have any benefits
gained from moving the taller bar or from starting from a point where the distance
between the bars is not maximized.

Time complexity: O(n) where an is the number of bars
Space complexity: O(1)
*/

const maxArea = height => {
  let left = 0;
  let right = height.length - 1;
  let result = 0;

  while (right > left) {
    result = Math.max(
      result,
      Math.min(height[left], height[right]) * (right - left)
    );
    if (height[left] < height[right]) left++;
    else right--;
  }
  return result;
};
