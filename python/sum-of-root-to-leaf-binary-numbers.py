from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, curr):
            if not node: return 0
            
            curr <<= 1
            curr |= node.val
            
            if node.left == None and node.right == None:
                return curr
            
            return dfs(node.left, curr) + dfs(node.right, curr)
        
        return dfs(root, 0)