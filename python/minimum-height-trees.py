from typing import List
from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n < 3: return [i for i in range(n)]
        
        adj_list = defaultdict(set)
        
        for x, y in edges:
            adj_list[x].add(y)
            adj_list[y].add(x)
        
        leafs = [x for x in adj_list if len(adj_list[x]) == 1]
        
        while len(adj_list) > 2:
            new_leafs = []
            for leaf in leafs:
                for neighbor in adj_list[leaf]:
                    adj_list[neighbor].remove(leaf)
                    if len(adj_list[neighbor]) == 1:
                        new_leafs.append(neighbor)
                del adj_list[leaf]
            leafs = new_leafs
        
        return adj_list.keys()