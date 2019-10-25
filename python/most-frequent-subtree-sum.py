#  https://leetcode.com/problems/most-frequent-subtree-sum/
#  Related Topics: Hash Table, Tree, DFS
#  Difficulty: Medium


# Initial thoughts:
# Traversing the tree in a post order DFS manner, we are going to create
# a freqency table of all the subtree sums and return those sums that occur
# most at the end.

# Time Complexity: O(n) where n == number of nodes in the tree
# Space Complexity: O(n) where n == number of nodes in the tree (In a worst case
# situation, each and every subtree has a unique sum that requires a separate entry
# in our freqency table)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        dic = defaultdict(int)

        def dfs(root: TreeNode) -> int:
            if root == None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            dic[root.val+left+right] += 1
            return root.val+left+right

        dfs(root)

        m = float('-inf')

        for key, val in dic.items():
            if val > m:
                finalRes = [key]
                m = val
            elif val == m:
                finalRes.append(key)

        return finalRes
