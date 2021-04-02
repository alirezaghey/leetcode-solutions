import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, s: int) -> int:
        def dfs(node, prev_sum, dic):
            if not node: return 0
            
            curr_sum = prev_sum + node.val
            res = dic[curr_sum - s]
            dic[curr_sum] += 1
            res += dfs(node.left, curr_sum, dic)
            res += dfs(node.right, curr_sum, dic)
            
            dic[curr_sum] -= 1
            return res
        
        return dfs(root, 0, collections.defaultdict(int, {0: 1}))