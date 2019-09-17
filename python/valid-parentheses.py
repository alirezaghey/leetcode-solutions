# https://leetcode.com/problems/valid-parentheses/
# Related Topics: String, Stack
# Difficulty: Easy


# Initial thoughts:
# Creating a lookup table for all the types of parentheses and
# using a stack we touch every element of the input string and
# if it's an opening parenthes push it on the stack and if its
# a closing parenthes we pop one from the stack checking if it's
# a valid counterpart for the current parenthes.
# At the end, the stack must be empty

# Time complexity: O(n) where n === s.length
# Space complexity: O(n) where n === s.length


class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {"(": ")", "[": "]", "{": "}"}
        stack = []

        for p in s:
            if p in lookup:
                stack.append(lookup[p])
            else:
                if len(stack) == 0 or stack.pop() != p:
                    return False

        return len(stack) == 0
