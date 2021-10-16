"""
Lowest Common Ancestor
init : O(N)
lca : O(logN)
"""


class LCA:
    __slots__ = ["n","h","root","d","p"]
    def __init__(self, v, root=0):
        self.n = len(v)
        self.h = self.n.bit_length()
        self.root = root
        self.d = [None]*self.n
        self.p = [[None]*self.n for _ in range(self.h)]

        self.d[self.root] = 0
        self.p[0][self.root] = self.root
        q = [self.root]
        while q:
            x = q.pop()
            nd = self.d[x] + 1
            for y in v[x]:
                if self.d[y] is None:
                    self.d[y] = nd
                    self.p[0][y] = x
                    q.append(y)

        self.h = (max(self.d)+1).bit_length()

        for i in range(self.h-1):
            j = i+1
            for x, px in enumerate(self.p[i]):
                self.p[j][x] = self.p[i][px]


    def lca(self, x, y):
        p = self.p
        if self.d[x] < self.d[y]:
            x, y = y, x

        k = self.d[x] - self.d[y]
        i = 0
        while k:
            if k&1:
                x = p[i][x]
            i += 1
            k >>= 1

        if x == y:
            return x

        for i in range(self.h)[::-1]:
            if p[i][x] != p[i][y]:
                x = p[i][x]
                y = p[i][y]
        return p[0][x]


    def dist(self, x, y):
        d = self.d
        return d[x] + d[y] - 2 * d[self.lca(x, y)]

