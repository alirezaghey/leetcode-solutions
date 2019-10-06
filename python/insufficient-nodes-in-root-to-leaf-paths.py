#  https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/
#  Related Topics: Tree, DFS
#  Difficulty: Medium


# Initial thoughts:
# We are going to do a post order traversal of the tree and
# calculate sum of the value of every path from every leaf upwards.
# Every node is responsible for setting its children that have a
# value less than limit to null and returning the greater path sum
# of any of its children to its parent for evaluation.
# Since nodes only decide about their children, an edge case is when
# the root itself needs to be deleted. That will be handled by the
# calling function that will receive the maximum leaf to root path sum.

# Time complexity: O(n) where n === number of nodes in the tree
# Space complexity: O(n) where n === number of nodes in the tree (that is in the
# worst case where the tree is fully unballanced. In a fully ballanced tree, the
# space complexity renders to O(log n) where log n equals the depth of the tree)

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:

        def dfs(root: TreeNode, currSum: int) -> int:
            if root == None:
                return currSum

            left = dfs(root.left, currSum+root.val)
            right = dfs(root.right, currSum+root.val)

            if root.left == None:
                maximum = right
            elif root.right == None:
                maximum = left
            else:
                maximum = max(left, right)

            if left < limit:
                root.left = None
            if right < limit:
                root.right = None

            return maximum

        return None if dfs(root, 0) < limit else root
