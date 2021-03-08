from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, 0)
            
            ls, lt = dfs(node.left)
            rs, rt = dfs(node.right)
            
            return (ls+rs+node.val, lt+rt+(abs(ls-rs)))
        
        return dfs(root)[1]