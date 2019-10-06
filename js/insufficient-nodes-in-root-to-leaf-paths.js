// https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/
// Related Topics: Tree, DFS
// Difficulty: Medium

/*
Initial thoughts:
We are going to do a post order traversal of the tree and
calculate sum of the value of every path from every leaf upwards.
Every node is responsible for setting its children that have a
value less than limit to null and returning the greater path sum
of any of its children to its parent for evaluation.
Since nodes only decide about their children, an edge case is when
the root itself needs to be deleted. That will be handled by the
calling function that will receive the maximum leaf to root path sum.

Time complexity: O(n) where n === number of nodes in the tree
Space complexity: O(n) where n === number of nodes in the tree (that is in the
worst case where the tree is fully unballanced. In a fully ballanced tree, the
space complexity renders to O(log n) where log n equals the depth of the tree)
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
 * @param {number} limit
 * @return {TreeNode}
 */
const sufficientSubset = (root, limit) => {
  return dfs(root, 0) < limit ? null : root;

  function dfs(root, currSum) {
    if (root === null) return currSum;

    const left = dfs(root.left, currSum + root.val);
    const right = dfs(root.right, currSum + root.val);

    let max;
    if (root.left === null) max = right;
    else if (root.right === null) max = left;
    else max = Math.max(left, right);

    if (left < limit) root.left = null;
    if (right < limit) root.right = null;

    return max;
  }
};
