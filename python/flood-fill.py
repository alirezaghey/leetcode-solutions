#  https://leetcode.com/problems/flood-fill/
#  Related Topics: BFS, DFS
#  Difficulty: Easy


# Initial thoughts:
# Starting with the initial pixel we can approach the problem in a BFS manner.
# Change the first pixel and enqueue its 4-directionally adjacent pixels if they
# comply with the criterion of having the old color and are in bounds with regards
# to the original pixel.

# Time complexity: O(n) where n === number of elements in image
# Space complexity: O(n) where n === number of leements in image
from collections import deque
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        R, C = len(image), len(image[0])
        currPixels = [(sr, sc)]
        oldColor = image[currPixels[0]][currPixels[1]]

        if oldColor == newColor:
            return image

        newPixels = []
        while len(currPixels) > 0:
            r, c = currPixels.pop()
            image[r][c] = newColor
            if r > 0 and image[r-1][c] == oldColor:
                newPixels.append((r-1, c))
            if c+1 < C and image[r][c+1] == oldColor:
                newPixels.append((r, c+1))
            if r+1 < R and image[r+1][c] == oldColor:
                newPixels.append((r+1, c))
            if c > 0 and image[r][c-1] == oldColor:
                newPixels.append((r, c-1))

            if len(currPixels == 0):
                currPixels = newPixels
                newPixels = []

        return image

# Same solution as above (using BFS), but using a real queue for BFS


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        R, C = len(image), len(image[0])
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        currPixels = deque()
        currPixels.append((sr, sc))

        while len(currPixels) > 0:
            r, c = currPixels.popleft()
            image[r][c] = newColor
            if r > 0 and image[r-1][c] == oldColor:
                currPixels.append((r-1, c))
            if c+1 < C and image[r][c+1] == oldColor:
                currPixels.append((r, c+1))
            if r+1 < R and image[r+1][c] == oldColor:
                currPixels.append((r+1, c))
            if c > 0 and image[r][c-1] == oldColor:
                currPixels.append((r, c-1))

        return image

# Using a DFS approach.
# Time and space complexities don't change in comparison to BFS.
# This approach is arguable more elegant, readable, but IMHO
# it "looks" less like a flood fill and if investigating, simulating
# or depicting of a flood fill was in order, DFS couldn't do it.


class Solution:

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        R, C = len(image), len(image[0])
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image

        def dfs(r: int, c: int) -> None:
            image[r][c] = newColor
            if r > 0 and image[r-1][c] == oldColor:
                dfs(r-1, c)
            if c+1 < C and image[r][c+1] == oldColor:
                dfs(r, c+1)
            if r+1 < R and image[r+1][c] == oldColor:
                dfs(r+1, c)
            if c > 0 and image[r][c-1] == oldColor:
                dfs(r, c-1)

        dfs(sr, sc)
        return image
