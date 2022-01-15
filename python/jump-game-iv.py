import collections
from typing import List

class Solution:
    # BFS approach
    # Time complexity: O(V) where V is the length of the array. The indices are considered the nodes of the graph
    # Space complexity: O(V)
    # Note: If we don't properly optimize it the complexity becomes O(V + E) where E could be V^2
    # in the worst case where all the elements in the array except for the first and last
    # are the same. It creates a graph where each node is connecte directly to every other one
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1: return 0
        
        N = len(arr)
        adj_list = collections.defaultdict(list)
        for i, el in enumerate(arr):
            adj_list[el].append(i)
        for key in adj_list:
            adj_list[key].sort(reverse=True)
        
        deq = collections.deque([0])
        seen = set([0])
        res = 0
        
        while deq:
            res += 1
            n = len(deq)
            
            for _ in range(n):
                node = deq.popleft()
                
                if node+1 == N-1: return res
                if node < N-1 and node+1 not in seen:
                    deq.append(node+1)
                    seen.add(node+1)                
                if node > 0 and node-1 not in seen:
                    deq.append(node-1)
                    seen.add(node-1)

                for nei in adj_list[arr[node]]:
                    if nei == N - 1:
                        return res
                    if nei not in seen:
                        deq.append(nei)
                        seen.add(nei)
                adj_list[arr[node]] = [] # the trick