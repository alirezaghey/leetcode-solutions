from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # iterative solution
    # Time complexity: O(log n) in a balanced tree, otherwise O(n)
    # Space complexity: O(1)
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return TreeNode(val)
        
        curr = root
        while True:
            if val < curr.val:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = TreeNode(val)
                    break
            else:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = TreeNode(val)
                    break
        return root
    # recursive solution
    # Time complexity: O(log n) in a balanced tree, otherwise O(n)
    # Space complexity: O(log n) for the stack in a balanced tree, otherwise, O(n)
    def insertIntoBST2(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert(node, val):
            if not node:
                return TreeNode(val)
            
            if val > node.val:
                node.right = insert(node.right, val)
            else:
                node.left = insert(node.left, val)
            
            return node
        
        return insert(root, val)
