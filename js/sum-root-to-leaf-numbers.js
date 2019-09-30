// https://leetcode.com/problems/sum-root-to-leaf-numbers/
// Related Topics: Tree, DFS
// Difficulty: Medium

/*
Initial thoughts:
Using a DFS approach we are going to traverse every path from the root to its leafs, all
the while combining the digits at the current node's value. This will be done using basic
math (numberUntilNow = numberUntilNow * 10 + newDigit).
Since numbers are value types in JS and for every recursive function call a new copy
will be created from the number we have created until that point, we don't need to worry
about the numbers from different paths to get mixed up.
At the end of the route, when both leafs are null, we are going to return the number.
Since we are going to add the result of the paths in the left subtree with the path in the
right subtree, the end result will be the total of all the paths in the binary tree.

Time complexity: O(n) where n === the number of nodes in the tree
Space complexity: O(n) where n === the number of noded in the tree (that's a worst case where
the binary tree is fully unballance and looks like a linked list)
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
const sumNumbers = root => {
  return traverse(root, 0);
};

/**
 * @param {TreeNode} root
 * @param {number} num
 * @return {number}
 */
const traverse = (root, num) => {
  if (root === null) return 0;
  num = num * 10 + root.val;
  if (root.left === null && root.right === null) return num;
  return traverse(root.left, num) + traverse(root.right, num);
};
