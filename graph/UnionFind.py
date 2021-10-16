"""
Union-Find
"""


class UnionFind:

    __slots__ = ["par", "rank"]

    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [0]*n


    def root(self, x):
        if x == self.par[x]:
            return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]


    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
