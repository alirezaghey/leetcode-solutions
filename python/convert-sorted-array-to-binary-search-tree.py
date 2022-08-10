from typing import List, Optional


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time complexity: O(n) where n is thee length of the input array
    # Space complexity: O(n) if we count the result, otherwise O(log n) for the call stack
    # recursive
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(left, right):
            if left > right:
                return None

            mid = ((right - left)//2)+left

            node = TreeNode(nums[mid])

            node.left = dfs(left, mid-1)
            node.right = dfs(mid+1, right)

            return node

        return dfs(0, len(nums)-1)
