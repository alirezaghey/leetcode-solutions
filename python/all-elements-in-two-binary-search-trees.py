from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    # Time complexity: O(n + m) where n and m are the number of nodes of the trees
    # Space complexity: O(n + m) even if we don't consider the results list auxilliary
    # This is a 2 pass solution
    # we first create separate inorder lists of the trees
    # and then merge them together
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def read_nodes(node, res):
            if not node: return
            
            read_nodes(node.left, res)
            res.append(node.val)
            read_nodes(node.right, res)
        
        def merge(A, B):
            res = []
            i = j = 0
            while i < len(A) and j < len(B):
                if A[i] < B[j]:
                    res.append(A[i])
                    i += 1
                else:
                    res.append(B[j])
                    j += 1
            if i < len(A):
                res.extend(A[i:])
            elif j < len(B):
                res.extend(B[j:])
            return res
                
                
        res1, res2 = [], []
        read_nodes(root1, res1)
        read_nodes(root2, res2)
        return merge(res1, res2)
    
    # Time complexity: O(n + m) where n and m are the number of nodes of each tree
    # Space complxity: O(max(depth tree1, depth tree2)) if we don't count the results list
    # Using python's yield to create an inorder traversal generator for both trees
    # and merge them on the go
    # Effective times are about 10x slower than 2 pass solutions that create 2 separate lists first
    # and then mergee them together
    # This is possibly due to repeated function calls of this solution
    # which are quite expensive in python
    def getAllElements2(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def next_inorder(node):
            if node and node.left: 
                yield from next_inorder(node.left)
            yield node
            if node and node.right:
                yield from next_inorder(node.right)
        
        def get_next(gen):
            try:
                return next(gen)
            except StopIteration:
                return None
        
        tree1, tree2 = next_inorder(root1), next_inorder(root2)
        
        node1, node2 = get_next(tree1), get_next(tree2)
        
        res = []
        while node1 and node2:
            if node1.val < node2.val:
                res.append(node1.val)
                node1 = get_next(tree1)
            else:
                res.append(node2.val)
                node2 = get_next(tree2)
        
        while node1:
            res.append(node1.val)
            node1 = get_next(tree1)
        while node2:
            res.append(node2.val)
            node2 = get_next(tree2)
        
        return res
            