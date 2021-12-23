from collections import defaultdict
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indeg = [0]*numCourses
        adj_list = defaultdict(set)
        
        for child, parent in prerequisites:
            adj_list[parent].add(child)
            indeg[child] += 1
        
        res = []
        stack = []
        
        for i, el in enumerate(indeg):
            if el == 0:
                stack.append(i)
                res.append(i)
        
        while stack:
            node = stack.pop()
            for nei in adj_list[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    stack.append(nei)
                    res.append(nei)
        
        if len(res) == numCourses: return res
        else: return []