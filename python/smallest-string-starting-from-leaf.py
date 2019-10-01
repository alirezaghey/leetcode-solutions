# https://leetcode.com/problems/smallest-string-starting-from-leaf/
#  Related Topics: Tree, DFS
#  Difficulty: Medium


# Initial thoughts:
# Using a DFS approach, we are going to log each path from root to leaf.
# Whenever we encounter a leaf, we are going to reverse the built path and
# compare it to the answer that we have until then and update it if this string
# is lexicographically smaller.


# Time complexity: O(n * log n) where n === the number of nodes in the tree.
# The idea is # that we have to visit each node in a DFS algorithm and for each possible leaf at the end
# of the tree we have to compare the built string to the current answer. String comparison
# takes O(l) where l equals the length of the shorter string in a comparison. In a ballanced
# tree the length of the strings will equal the depth of the tree with is log(n), and the number
# of leaf nodes will be roughly n/2 (half of the nodes in a ballanced binary tree are at the deepest level).
# This will translate into (n/2 * log(n)) comparisons plus n for the DFS traversal => (n/2 * log(n)) + n,
# which becomes O(n * log n) in big O notation.
# Please note that in a perfectly unballanced binary tree that looks like a linked list, our strings will be
# of length n (instead of log n) but since we are dealing with just one comparison, the end result will have a
# lesser time complexity than the previous calculation, namely n (for DFS traversal) and n (for one comparison) =>
# n + n => O(n), so we stick with the first calculation, as it shows us the upper bound.

# Space complexity: O(n) where n === the number of nodes in the tree (that's a worst case where
# the binary tree is fully unballanced and looks like a linked list)

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self) -> None:
        self.answer = "~"

    def smallestFromLeaf(self, root: TreeNode) -> str:
        self.traverse(root, [])
        return self.answer

    def traverse(self, root: TreeNode, currPath: List[str]) -> None:
        if root == None:
            return

        currPath.append(self.getChar(root.val))
        if root.left == None and root.right == None:
            self.answer = min(self.answer, "".join(reversed(currPath)))
        self.traverse(root.left, currPath)
        self.traverse(root.right, currPath)
        currPath.pop()

    def getChar(self, num: int) -> str:
        return chr(num + ord('a'))
