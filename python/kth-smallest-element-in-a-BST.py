from typing import Optional


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(h) where h is the depth of the tree
    # Recursive approach
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = None

        def in_order(node, num):
            if not node:
                return num

            res = in_order(node.left, num)
            res += 1
            if res == k:
                self.res = node.val
            res = in_order(node.right, res)
            return res

        in_order(root, 0)
        return self.res
