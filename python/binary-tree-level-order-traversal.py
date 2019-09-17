# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Related Topics: Tree, BFS
# Difficulty: Easy


# Initial thoughts:
# Using a BFS approach, we are going to queue the nodes for the next level
# in a temporary queue and visit each node in the current queue while adding
# their children to the temp queue.
# When the current queue is empty, we are going to make the temp queue,
# the current queue and start the process again untill there is no node left.
# [JS Note]: Since JavaScript does not have a default Queue data structure and
# using JS arrays as a queue will has an O(n) time complexity when shifting the head
# we will create our own Queue abstract datatype based on a singly linked list.

# Time complexity: O(n) where n is the number of nodes in the tree
# Space complexity: O(n) where n is the number of nodes in the tree;
# That is because we need to temporarily queue the nodes in a particular level
# and since the last level of a binary tree holds approximately n/2 nodes, the
# space complelxity is O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
from typing import List


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        currQueue = deque()
        currQueue.append(root)

        tempQueue = deque()

        result = []
        tempRes = []

        while len(currQueue):
            node = currQueue.popleft()
            if node:
                tempRes.append(node.val)
                if node.left:
                    tempQueue.append(node.left)
                if node.right:
                    tempQueue.append(node.right)
            if(len(currQueue) == 0):
                if len(tempRes):
                    result.append(tempRes)
                tempRes = []
                currQueue = tempQueue
                tempQueue = deque()

        return result
