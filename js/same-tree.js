// https://leetcode.com/problems/same-tree/
// Related Topics: Tree, Depth-first Search
// Difficulty: Easy

/*
Initial thoughts:
For two trees to be the same, their structure and values must be the same.
Using a Depth-frist Search approach we are going to touch and compare each
node on both trees at the same time and return false if there is any
dissimilarity. If our algorithm reaches the end without encountering any
viariance between the nodes, we return true.

Time complexity: O(Min(n,m)) where n === number of nodes in p and m === number of nodes in q.
The reason is that if the trees are not the same, the number of the nodes could differ but our
algorithm will stop at most after visiting all the nodes of the smaller tree. 
Space complexity: O(n) in the worst case when the trees are completely unbalanced and
O(log n) if they are completely balanced.

*/

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
const isSameTree = (p, q) => {
  function check(p, q) {
    // both leaf
    if (!p && !q) return true;
    // one leaf
    if ((!p && q) || (p && !q)) return false;
    if (p.val !== q.val) return false;
    return true;
  }
  const queue = [[p, q]];
  while (queue.length) {
    const [p, q] = queue.shift();
    if (!check(p, q)) return false;
    if (p) {
      queue.push([p.left, q.left]);
      queue.push([p.right, q.right]);
    }
  }
  return true;
};
