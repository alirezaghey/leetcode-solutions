#  https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
#  Related Topics: Tree, DFS
#  Difficulty: Medium


# Initial thoughts:
# Using a DFS approach we are going to calculate the max depth first.
# Then, we are going to hold a reference to all of the deepest nodes in
# a set (also using a DFS approach). In the same run for getting the deepest
# nodes, we are going to populate a dictionary that will hold a reference to
# all the nodes in the tree as the key and their parents as the value.
# Now, having all the deepest nodes and all the parent child pairs, we can
# go up the parent ladder until we find a common ancestor for all the deepest
# nodes.


# Time complexity: O(n) where n === number of nodes in the tree. We are going to
# traverse the tree once to calculate the max depth, which is O(n) because we have
# to visit every node. Then we have to find the deepest nodes, which is also O(n).
# Then we have to reduce the deepest nodes set to their common parent, which takes
# O(n) in a worst case scenario where we are dealing with a perfectly ballanced tree.

# Space complexity: O(n) where n === number of nodes in the tree. We have to create
# a dictionary to keep track of the nodes and their parents, which is O(n). For the
# recursive calls in a dfs we als have log(n) stack frames, which renders to O(n).

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.parents = {}
        self.maxDepth = None

    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        self.maxDepth = self.calculateMax(root)

        deepestNodes = set()
        self.getDeepestNodes(root, deepestNodes, None, 0)

        while len(deepestNodes) > 1:
            tempNodes = set()
            for node in deepestNodes:
                tempNodes.add(self.parents[node])
            deepestNodes = tempNodes
        return deepestNodes.pop()

    def getDeepestNodes(self, root: TreeNode, deepestNodes, parent: TreeNode, currDepth: int) -> None:
        if root == None:
            return
        self.parents[root] = parent
        currDepth += 1
        if currDepth == self.maxDepth:
            deepestNodes.add(root)
        self.getDeepestNodes(root.left, deepestNodes, root, currDepth)
        self.getDeepestNodes(root.right, deepestNodes, root, currDepth)

    def calculateMax(self, root: TreeNode) -> int:
        if root == None:
            return 0

        return max(self.calculateMax(root.left), self.calculateMax(root.right))+1

# Different approach:
# We can paint all the nodes with their depth in one go while saving their parents.
# Then we are going to clculate the max depth and filter out the nodes with maximum
# depth. At last, we are going to search for a common ancestor among the deepest nodes
# and return it.

# Time Complexity: O(n) where n === number of nodes. We do a DFS to create a dictionary
# with all the nodes, their depth, and their parent. That is O(n). Then we are going to
# loop over the dictionary to find the maximum depth, which is also O(n). Then we are
# going to loop over the dictionary to filter out all the nodes with the maximum depth,
# which is also O(n). Then we are going to find a common parent to all the deepest nodes
# which takes O(n) at most. This is O(4*n) which renders to O(n)
# Space complexity: O(n) where n === number of nodes.


class Solution:
    def __init__(self):
        self.nodes = {None: (0, None)}
        self.maxDepth = None

    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        self.traverse(root, None)

        maximum = 0
        for v in self.nodes.values():
            maximum = max(maximum, v[0])

        deepestNodes = set()
        for key, value in self.nodes.items():
            if value[0] == maximum:
                deepestNodes.add(key)

        while len(deepestNodes) > 1:
            tempNodes = set()
            for node in deepestNodes:
                tempNodes.add(self.nodes[node][1])
            deepestNodes = tempNodes

        return deepestNodes.pop()

    def traverse(self, root, parent):
        if root == None:
            return
        depth = self.nodes[parent][0]+1
        self.nodes[root] = (depth, parent)
        self.traverse(root.left, root)
        self.traverse(root.right, root)
