from collections import defaultdict

class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        self.best = float("-inf")
        
        def backtrack(curr_node, curr_time, curr_val, adj_list, visited):
            if curr_time <= maxTime // 2:
                self.best = max(self.best, curr_val)
            if curr_node == 0:
                self.best = max(self.best, curr_val)
            
            for nei, t in adj_list[curr_node]:
                if curr_time + t <= maxTime:
                    if nei not in visited:
                        visited.add(nei)
                        backtrack(nei, curr_time+t, curr_val+values[nei], adj_list, visited)
                        visited.remove(nei)
                    else:
                        backtrack(nei, curr_time+t, curr_val, adj_list, visited)
        
                
                
                
                
        adj_list = defaultdict(list)
        for u, v, t in edges:
            adj_list[u].append((v, t))
            adj_list[v].append((u, t))
        
        backtrack(0, 0, values[0], adj_list, set([0]))
        return self.best