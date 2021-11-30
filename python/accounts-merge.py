from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        accounts = [(account[0], set(account[1:])) for account in accounts]
        
        for i in range(len(accounts)):
            for j in range(i+1, len(accounts)):
                if not accounts[i][1].isdisjoint(accounts[j][1]):
                    uf.union(i, j)
        res = {}
        for i in range(len(accounts)):
            p = uf.find(i)
            if p not in res:
                res[p] = [accounts[i][0], accounts[i][1]]
            else:
                res[p][1].update(accounts[i][1])
        return [[value[0], *sorted(value[1])] for value in res.values()]
                

        
class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
    
    def find(self, x):
        while self.root[x] != x:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]
        return x
    
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y: return True
        
        if self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        elif self.rank[root_y] > self.rank[root_x]:
            self.root[root_x] = root_y
        else:
            self.rank[root_x] += 1
            self.root[root_y] = root_x
        return False