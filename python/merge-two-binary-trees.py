from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time complexity: O(max(n, m)) where n and m are the number of nodes in tree1 and tree2
    # Space complexity: O(max(n, m))
    # BFS approach
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1: return root2
        if not root2: return root1
        
        deq = deque([(root1, root2)])
        
        while deq:
            node1, node2 = deq.popleft()
            
            node1.val += node2.val
            if not node1.left:
                node1.left = node2.left
            elif node1.left and node2.left:
                deq.append((node1.left, node2.left))
            if not node1.right:
                node1.right = node2.right
            elif node1.right and node2.right:
                deq.append((node1.right, node2.right))
        return root1
            
    # Time complexity: O(max(n, m)) where n and m are the number of nodes in tree1 and tree2
    # Space complexity: O(max(n, m))
    # DFS approach
    def mergeTrees2(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node1, node2):
            if not node1: return node2
            if not node2: return node1
            
            node1.val += node2.val
            node1.left = dfs(node1.left, node2.left)
            node1.right = dfs(node1.right, node2.right)
            
            return node1
        
        return dfs(root1, root2)