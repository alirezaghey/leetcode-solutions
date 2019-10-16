#  https://leetcode.com/problems/triangle/
#  Related Topics: Array, Dynamic Programming
#  Difficulty: Medium


# Initial thoughts:
# Looking at the triangle like a binary tree enables us to try out
# every possible root to leaf path looking for the path with the
# minimum sum of values. This can be done in a DFS approach, our
# base case will be when our current depth equals the length of the
# triangle. This would have a time complexity of O(2^depth) which in
# this case is more than O(n) where n is the number of elements in the
# whole triangle. That's is because every deper level of row in the triangle
# has only one more element compared to the row above it and not double
# the elements like it would be in a real binary tree.
# Without dynamic programming our solution would exceed the time limit.

# Time complexity: O(2^depth) where depth == len(triangle)
# Space complexity: O(depth) where depth == len(triangle)
# from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        def dfs(idx: int, depth: int) -> int:
            if depth == len(triangle):
                return 0
            return min(dfs(idx, depth+1), dfs(idx+1, depth+1))+triangle[depth][idx]

        return dfs(0, 0)

# Optimization:
# By caching the results for each node
# we can render the time complexity of our solution linear.

# Time Complexity: O(n) where n is the number of elements in the whole triangle
# Space Complexity: O(n) where n is the number of elements in the whole triangle


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[None] * (i+1) for i in range(len(triangle))]

        def dfs(idx: int, depth: int) -> int:
            if depth == len(triangle):
                return 0

            if dp[depth][idx] == None:
                dp[depth][idx] = min(
                    dfs(idx, depth+1), dfs(idx+1, depth+1))+triangle[depth][idx]
            return dp[depth][idx]

        return dfs(0, 0)

# Optimization:
# While doing this problem in a recursive manner may be better
# illustration and solving purposes, it is more efficient space-wise
# if we solve it iteratively. It is still linear in terms of space but
# the extra space for the recursive stack is saved

# Time Complexity: O(n) where n is the number of elements in the whole triangle
# Space Complexity: O(n) where n is the number of elements in the whole triangle


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]

        dp = [[None]*(i+1) for i in range(len(triangle))]

        for i in range(len(triangle[len(triangle)-1])):
            dp[len(triangle)-1][i] = triangle[len(triangle)-1][i]

        for row in range(len(triangle)-2, -1, -1):
            for col in range(len(triangle[row])):
                dp[row][col] = triangle[row][col] + \
                    min(dp[row+1][col], dp[row+1][col+1])

        return dp[0][0]

# Optimization:
# Now, since we only need the results of one row (the previous) at a time
# we are going to reduce the auxilliary space to a one dimensional array
# that has the length of the depth of the triangle (that is the same as the last
# row of the tirangle)

# Time Complexity: O(n) where n is the number of elements in the whole triangle
# Space Complexity: O(m) where m is the number of elements in the last row
# of the triangle


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]

        dp = [el for el in triangle[-1]]

        for row in range(len(triangle)-2, -1, -1):
            for col in range(len(triangle[row])):
                dp[col] = triangle[row][col] + \
                    min(dp[col], dp[col+1])

        return dp[0]
