class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Linear time complexity
# due to the use of a dictionary
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def dfs(left, right, inOrdDic, inorder, postorder):
            if left > right:
                return None
            if left == right:
                postorder.pop()
                return TreeNode(inorder[left])
            
            root_idx = inOrdDic[postorder[-1]]
            root = TreeNode(inorder[root_idx])
            postorder.pop()
            
            root.right = dfs(root_idx+1, right, inOrdDic, inorder, postorder)
            root.left = dfs(left, root_idx-1, inOrdDic, inorder, postorder)
            
            return root
        
        inOrdDic = {el: i for i, el in enumerate(inorder)}
        return dfs(0, len(inorder)-1, inOrdDic, inorder, postorder)

# Quadratic time complexity
# Because of linear searches for the root node in the inorder traversal
# and the slicing of the inorder traversal
class Solution:
    def buildTree2(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def dfs(inorder, postorder):
            if not inorder:
                return None
            elif len(inorder) == 1:
                postorder.pop()
                return TreeNode(inorder[0])
            
            root_idx = inorder.index(postorder[-1])
            root = TreeNode(inorder[root_idx])
            
            postorder.pop()
            root.right = dfs(inorder[root_idx+1:], postorder)
            root.left = dfs(inorder[:root_idx], postorder)
            
            return root
        
        return dfs(inorder, postorder)