class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(rows, diags, anti_diags, partial_res, res):
            if len(partial_res) >= n:
                res.append(write_out_nqueens(partial_res))
                return
            
            c = len(partial_res)
            for r in range(n):
                if r not in rows and r-c not in diags and r+c not in anti_diags:
                    rows.add(r); diags.add(r-c); anti_diags.add(r+c)
                    partial_res.append(r)
                    backtrack(rows, diags, anti_diags, partial_res, res)
                    partial_res.pop()
                    rows.remove(r); diags.remove(r-c); anti_diags.remove(r+c)
        def write_out_nqueens(arr):
            res = []
            for el in arr:
                res.append("."*el + "Q" + "."*(n-el-1))
            return res
        
        res = []
        backtrack(set(), set(), set(), [], res)
        return res