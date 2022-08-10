/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} nums
 * @return {TreeNode}
 */
// Time complexity: O(n) where n is the length of the input array
// Space complexity: O(n) if we count the result, otherwise O(log n) for the recursive call stack
// recursive
var sortedArrayToBST = function (nums) {
    const dfs = (left, right) => {
        if (left > right)
            return null;

        const mid = Math.floor((right - left) / 2) + left
        const node = new TreeNode(nums[mid])

        node.left = dfs(left, mid - 1)
        node.right = dfs(mid + 1, right)

        return node
    }

    return dfs(0, nums.length - 1)
};