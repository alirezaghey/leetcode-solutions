from collections import deque
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        RIGHT, LEFT, DOWN, UP = range(1, 5)
        R, C = len(grid), len(grid[0])
        
        best = float("inf")
        dic = {(0,0): 0}
        deq = deque([(0,0,0)])
        
        while deq:
            r, c, cost = deq.popleft()
            if r == R-1 and c == C-1:
                best = min(best, cost)
                if best == 0: return 0
            
            for nr, nc, direc in ((r-1, c, UP), (r, c+1, RIGHT),
                                    (r+1, c, DOWN), (r, c-1, LEFT)):
                if nr < 0 or nr >= R or nc < 0 or nc >= C: continue # coords out of bound
                new_cost = cost+1 if direc != grid[r][c] else cost # cost increase if direction differs
                if (nr, nc) in dic and dic[(nr,nc)] <= new_cost: continue # we have visited this cell with smaller cost
                dic[(nr, nc)] = new_cost
                deq.append((nr, nc, new_cost))
                
        return best