from math import sqrt
from collections import defaultdict, Counter

class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))
    
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        xp, yp = self.find(x), self.find(y)
        self.p[xp] = yp
        
class Solution:
    def find_factors(self,n, cache):
        if n in cache: return cache[n]
        
        for i in range(2, int(sqrt(n)+1)):
            if n % i == 0:
                cache[n] = self.find_factors(n//i, cache) | set([i])
                return cache[n]
        return set([n])
    
    def largestComponentSize(self, A: List[int]) -> int:
        n = len(A)
        uf = UnionFind(n)
        connection_dict = defaultdict(list)
        factor_cache = dict()
        
        for i, el in enumerate(A):
            s_factors = self.find_factors(el, factor_cache)
            for f in s_factors:
                connection_dict[f].append(i)
        
        for indices in connection_dict.values():
            for i in range(len(indices)-1):
                uf.union(indices[i], indices[i+1])
        
        return max(Counter(uf.find(i) for i in range(n)).values())        

