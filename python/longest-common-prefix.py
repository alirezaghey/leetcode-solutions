# https://leetcode.com/problems/longest-common-prefix/
# Related Topics: String, Array
# Difficulty: Easy


# Initial thoughts:
# We are going to look at each index of every string
# at the same time, comparing them to their counterpart
# in the first string, adding the character to our results
# if all of the strings have the same character, and returning
# the results in case of a difference.

# Time complexity: O(n * min(s)) where s is the length of the strings
# Space complexity: O(min(s)) where s is the length of the strings
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        if not len(strs):
            return "".join(res)
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if i >= len(strs[j]) or strs[0][i] != strs[j][i]:
                    return "".join(res)
            res.append(strs[0][i])
        return "".join(res)


# Optimization:
# Using the counter variable we can forgoe the result tracking variable
# and just slice and return it at the end, rendering the space complexity constant.

# Time complexity: O(n * min(s)) where s is the length of the longest common prefix
# Space complexity: O(1)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not len(strs):
            return ""
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if i >= len(strs[j]) or strs[0][j] != strs[j][i]:
                    return strs[0][0:i]
        return strs[0]
