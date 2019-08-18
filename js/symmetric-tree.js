// Related Topics: Tree, DFS, BFS
// Difficulty: Easy

/*
Initial thoughts:
In a symmetric tree, the left half of of the tree is
the exact mirror image of the right half of it.
Recursively, we divide the problem into smalle sub problems
and check whether that is true.

Time complexity: O(n) since we have to touch every node once
Space complexity: O(n) The tree's depth in the worst case of
a completely unbalanced tree is n.
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
 * @return {boolean}
 */
var isSymmetric = function(root) {
  return check(root, root);
};

const check = (p, q) => {
  // they're both null
  if (!p && !q) return true;
  // one of them is null
  if (!p || !q) return false;
  // their value is unequal
  if (p.val !== q.val) return false;
  return check(p.left, q.right) && check(p.right, q.left);
};

/*
Iterative solution:
Using a BFS approach, we add nodes to a queue
checking whether the left equals the right

Time complexity: O(n) since we have to touch every node once
Space complexity: O(n) for the queue where we have to add every node
*/

const isSymmetric = root => {
  if (!root) return true;
  const queue = [root.left, root.right];
  while (queue.length > 0) {
    const p = queue.pop();
    const q = queue.pop();

    // both are null, check next pair
    if (!p && !q) continue;
    // only one is null, unsymetrical
    if (!p || !q) return false;
    // their values are not equal;
    if (p.val !== q.val) return false;

    queue.push(q.left, p.right, q.right, p.left);
  }
  return true;
};
