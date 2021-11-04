# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(left, node):
            if not node: return 0
            if node.left == None and node.right == None:
                if left: return node.val
                else: return 0
            
            return dfs(True, node.left) + dfs(False, node.right)
        
        return dfs(False, root)