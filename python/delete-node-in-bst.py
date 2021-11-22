class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None
        
        if root.val < key: root.right = self.deleteNode(root.right, key)
        elif root.val > key: root.left = self.deleteNode(root.left, key)
        
        else:
            if root.left == None and root.right == None: return None # doesn't have any children
            if root.left == None and root.right: return root.right # has only right chilren
            if root.right == None and root.left: return root.left # has only left children

            # below is the case when it has both left and right children
            curr = root.right
            while curr.left:
                curr = curr.left

            root.val = curr.val
            root.right = self.deleteNode(root.right, curr.val)
        return root
        