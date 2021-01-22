from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # memoized dfs
    # TC: O(n) where n is the number of nodes in the tree
    # SC: O(n)
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node, taken, mem):
            if node == None: return 0
            
            if (node, taken) in mem:
                return mem[(node, taken)]
            
            if taken:
                mem[(node, taken)] = dfs(node.left, False, mem) + dfs(node.right, False, mem)
            else:
                mem[(node, taken)] = max(
                    dfs(node.left, True, mem) + dfs(node.right, True, mem) + node.val,
                    dfs(node.left, False, mem) + dfs(node.right, False, mem)
                )
            
            return mem[(node, taken)]
        
        return dfs(root, False, dict())