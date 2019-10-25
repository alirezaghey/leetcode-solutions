// https://leetcode.com/problems/most-frequent-subtree-sum/
// Related Topics: Hash Table, Tree, DFS
// Difficulty: Medium

/*
Initial thoughts:
Traversing the tree in a post order DFS manner, we are going to create
a freqency table of all the subtree sums and return those sums that occur
most at the end.

Time Complexity: O(n) where n == number of nodes in the tree
Space Complexity: O(n) where n == number of nodes in the tree (In a worst case
situation, each and every subtree has a unique sum that requires a separate entry
in our freqency table)
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
 * @return {number[]}
 */
const findFrequentTreeSum = root => {
    if (!root) return [];

    const m = new Map();

    function dfs(root) {
        if (!root) return 0;

        const left = dfs(root.left);
        const right = dfs(root.right);

        const val = root.val + left + right;
        if (m.has(val)) m.set(val, m.get(val) + 1);
        else m.set(val, 1);
        return val;
    }

    dfs(root);
    let max = Number.NEGATIVE_INFINITY;
    let finalRes;
    for (let [key, val] of m.entries()) {
        if (val > max) {
            max = val;
            finalRes = [key];
        } else if (val === max) finalRes.push(key);
    }
    return finalRes;
};
