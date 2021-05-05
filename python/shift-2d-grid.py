class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        R, C = len(grid), len(grid[0])
        k = k % (R * C)
        
        res = [[0]*C for _ in range(R)]
        
        for (r, c) in ((r, c) for c in range(C) for r in range(R)):
            res[(r+(c+k)//C)%R][(c+k)%C] = grid[r][c]
        
        return res