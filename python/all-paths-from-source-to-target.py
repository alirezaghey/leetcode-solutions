from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node, partial_res, res):
            if node == len(graph)-1:
                res.append(partial_res[:])
                return
            
            for nei in graph[node]:
                partial_res.append(nei)
                dfs(nei, partial_res, res)
                partial_res.pop()
        
        res = []
        dfs(0, [0], res)
        return res