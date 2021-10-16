"""
Union-Find with weight
unite(x,y,w) := y = x+w
"""


class UnionFind:

    __slots__ = ["par", "rank", "weight_"]

    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [0]*n
        self.weight_ = [0]*n


    def root(self, x):
        if x == self.par[x]:
            return x
        r = self.root(self.par[x])
        self.weight_[x] += self.weight_[self.par[x]]
        self.par[x] = r
        return r


    def unite(self, x, y, w):
        w += self.weight(x)-self.weight(y)
        x = self.root(x)
        y = self.root(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.weight_[x] = -w
        else:
            self.par[y] = x
            self.weight_[y] = w
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1


    def weight(self, x):
        self.root(x)
        return self.weight_[x]
