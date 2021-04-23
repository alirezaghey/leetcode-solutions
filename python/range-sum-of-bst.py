from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node, low, high):
            if not node:
                return 0
            
            res = node.val if (low <= node.val <= high) else 0
            if node.val > low: res += dfs(node.left, low, high)
            if node.val < high: res += dfs(node.right, low, high)
            
            return res
        
        return dfs(root, low, high)