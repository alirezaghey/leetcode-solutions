// https://leetcode.com/problems/path-sum-ii/
// Related Topics: Tree, DFS
// Difficulty: Medium

/*
Initial thoughts:
Using a DFS algorithm we are going to check every path from root to its leafs
and subtracts the the nodes values from the given sum. If at the end sum turns
out to be zero, we have a path with the given sum.
One thing to be aware of is that we need to check that we are at a leaf. The condition
for that is that both its left and right children are null. It is not enough to check that
the node itself is null because the null node could be the child from a parent node that
has its other child not null (in any case the definition of a leaf IS that both its children must be nulls)
Now, to return all the valid paths we need to save them in a temporary solution variable that we pass along
and push that to a result variable that will hold all the solutions.
Keeping track of the result variable is easy but tracking the solution variable has two option:
We either copy the solution array each time we call the function recursively (which will badly increase our
Space Complexity) or we can simulate the stack by pushing the current nodes variable to the back of it
and then popping it when the recursion returns.
But there is a catch: Since arrays are reference values, we need to copy (deep copy) the solution array to
the result array if it turns out to be a correct solution, otherwise, it will be the same array whose values
will be popped out one by one when the recursive functions return and we end up with an empty solution.

Time complexity: O(n) where n === the number of nodes in the tree
Space complexity: O(depth * 2^depth) this auxilliary space is needed for the result variable. Consider a worst
case scenario where we deal with a fully ballanced tree where every path is a solution. In this case the number
of our solutions will equal the number of leaf nodes which are 2^depth of the tree and each solution will hold
a number of nodes equal to the depth of the tree.
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
 * @return {number[][]}
 */
const pathSum = (root, sum) => {
  result = [];
  traverse(root, sum, [], result);
  return result;
};

/**
 *
 * @param {TreeNode} root
 * @param {number} sum
 * @param {number[]} solution
 * @param {number[][]} result
 */
const traverse = (root, sum, solution, result) => {
  if (root === null) return;
  solution.push(root.val);
  if (root.left === null && root.right === null && sum - root.val === 0)
    result.push([...solution]);

  traverse(root.left, sum - root.val, solution, result);
  traverse(root.right, sum - root.val, solution, result);
  solution.pop();
};
