// https://leetcode.com/problems/maximum-depth-of-binary-tree/
// Related Topics: Tree, DFS
// Difficulty: Easy

/*
Initial thoughts:
Using a DFS algorithm, we are going to recursively traverse each path
until we encounter a leaf node (both childs are null), counting the depth
and comparing the results to get the max.

Time complexity: O(n) in the worst case when the tree is fully unbalanced
Space complexity: O(n) for the recursive stack

*/

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
const maxDepth = root => {
  // base case
  if (!root) return 0;

  return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
};

/*
Iterative approach

Time complexity: O(n)
Space complexity: O(n) we need to use a stack to follow the depth
*/

/**
 * @param {TreeNode} root
 * @return {number}
 */
const maxDepth = root => {
  if (!root) return 0;
  let stack = [root];
  let tempStack = [];
  let count = 0;

  while (stack.length) {
    let temp = stack.pop();

    if (temp.left) tempStack.push(temp.left);
    if (temp.right) tempStack.push(temp.right);

    if (!stack.length) {
      count++;
      stack = tempStack;
      tempStack = [];
    }
  }
  return count;
};
