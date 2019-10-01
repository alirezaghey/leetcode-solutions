// https://leetcode.com/problems/smallest-string-starting-from-leaf/
//  Related Topics: Tree, DFS
//  Difficulty: Medium

/*
Initial thoughts:
Using a DFS approach, we are going to log each path from root to leaf.
Whenever we encounter a leaf, we are going to reverse the built path and
compare it to the answer that we have until then and update it if this string
is lexicographically smaller.


Time complexity: O(n * log n) where n === the number of nodes in the tree.
The idea is # that we have to visit each node in a DFS algorithm and for each possible leaf at the end
of the tree we have to compare the built string to the current answer. String comparison
takes O(l) where l equals the length of the shorter string in a comparison. In a ballanced
tree the length of the strings will equal the depth of the tree with is log(n), and the number
of leaf nodes will be roughly n/2 (half of the nodes in a ballanced binary tree are at the deepest level).
This will translate into (n/2 * log(n)) comparisons plus n for the DFS traversal => (n/2 * log(n)) + n,
which becomes O(n * log n) in big O notation.
Please note that in a perfectly unballanced binary tree that looks like a linked list, our strings will be
of length n (instead of log n) but since we are dealing with just one comparison, the end result will have a
lesser time complexity than the previous calculation, namely n (for DFS traversal) and n (for one comparison) =>
n + n => O(n), so we stick with the first calculation, as it shows us the upper bound.

Space complexity: O(n) where n === the number of nodes in the tree (that's a worst case where
the binary tree is fully unballanced and looks like a linked list)
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
 * @return {string}
 */

const smallestFromLeaf = root => {
  const answer = ['~'];
  traverse(root, [], answer);
  return answer[0];
};

/**
 *
 * @param {TreeNode} root
 * @param {string[]} currPath
 * @param {string[]} answer
 */
const traverse = (root, currPath, answer) => {
  if (root === null) return;

  currPath.push(toChar(root.val));
  if (root.left === null && root.right === null) {
    const temp = currPath
      .slice()
      .reverse()
      .join('');
    answer[0] = temp < answer[0] ? temp : answer[0];
  }
  traverse(root.left, currPath, answer);
  traverse(root.right, currPath, answer);
  currPath.pop();
};
/**
 *
 * @param {number} num
 * @return {string}
 */
const toChar = num => {
  return String.fromCharCode(num + 'a'.charCodeAt(0));
};
