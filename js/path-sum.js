// https://leetcode.com/problems/path-sum/
// Related Topics: Tree, DFS
// Difficulty: Easy

/*
Initial thoughts:
Using a DFS algorithm we are going to check every path from root to its leafs
and subtracts the the nodes values from the given sum. If at the end sum turns
out to be zero, we have a path with the given sum.
One thing to be aware of is that we need to check that we are at a leaf. The condition
for that is the both its left and right children are null. It is not enough to check that
the node itself is null because the null node could be the child from partent node that
has its other child not null.

Time complexity: O(n) where n === the number of nodes in the tree
Space complexity: O(n) where n === the number of nodes in the tree (in the worst case when
we are dealing with a tree that is full unballanced and looks like a linked list)
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
 * @param {number} sum
 * @return {boolean}
 */
const hasPathSum = (root, sum) => {
  if (root === null) return false;
  if (root.left === null && root.right === null) return sum - root.val === 0;
  return (
    hasPathSum(root.left, sum - root.val) ||
    hasPathSum(root.right, sum - root.val)
  );
};
