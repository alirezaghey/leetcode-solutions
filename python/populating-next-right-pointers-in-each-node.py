from typing import Optional
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    # Time complexity: O(n) where n is the number of nodes in the tree
    # Space complexity: O(log n)
    # DFS
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root: return root
        if root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
        
        self.connect(root.left)
        self.connect(root.right)
        return root
    
    # Time complexity: O(n) where n is the number of nodes in the tree
    # Space complexity: O(1)
    # BFS apporach; optimized for space
    def connect2(self, root: Optional[Node]) -> Optional[Node]:
        if not root: return root
        
        new_root = root
        
        while new_root:
            curr = new_root
            while curr:
                if curr.left:
                    curr.left.next = curr.right
                    if curr.next:
                        curr.right.next = curr.next.left
                curr = curr.next
            new_root = new_root.left
        return root
            
    # Time complexity: O(n) where n is the number of nodes in the tree
    # Space complexity: O(n)
    # BFS approach
    def connect3(self, root: Optional[Node]) -> Optional[Node]:
        if not root: return root
        
        deq = deque([root])
        
        while deq:
            n = len(deq)
            for i in range(n):
                node = deq.popleft()
                if i < n-1: node.next = deq[0]
                
                if node.left: deq.append(node.left)
                if node.right: deq.append(node.right)
        
        return root