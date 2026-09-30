class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, node):
        cur = node
        while cur != self.par[cur]:
            self.par[cur] = self.par[self.par[cur]]
            cur = self.par[cur]
        return cur

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.rank[pu] > self.rank[pv]:
            self.par[pv] = pu
        elif self.rank[pv] > self.rank[pu]:
            self.par[pu] = pv
        else:
            self.par[pv] = pu
            self.rank[pu] += 1
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = UnionFind(n)
        res = n
        for u, v in edges:
            if dsu.union(u, v):
                res -= 1
        return res