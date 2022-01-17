import collections
from typing import List


class Solution:
    # Time complexity: O(n * m) where n and m are the rows and columns of the grid
    # Space complexity: O(n * m)
    # DFS
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        
        def dfs(r, c):
            grid[r][c] = 0
            
            res = 0
            for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                nr, nc = r+dr, c+dc
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1:
                    res += dfs(nr, nc)+1
            return res
        
        res = 0
        for r, c in ((i, j) for i in range(R) for j in range(C)):
            if grid[r][c] == 1:
                res = max(res, dfs(r, c)+1)
        return res
    
    
    # Time complexity: O(n * m) where n and m are the rows and columns of the grid
    # Space complexity: O(n * m)
    # BFS
    def maxAreaOfIsland2(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        
        def bfs(r, c):
            res = 0
            deq = collections.deque([(r, c)])
            grid[r][c] = 0
            
            while deq:
                r, c = deq.popleft()
                res += 1
                
                for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        deq.append((nr, nc))
            return res
        
        res = 0
        for r, c in ((i, j) for i in range(R) for j in range(C)):
            if grid[r][c] == 1:
                res = max(res, bfs(r, c))
        return res