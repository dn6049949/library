"""
LowLink (bridge and articulation)
init : O(|V|+|E|)
"""

import sys
sys.setrecursionlimit(1000000)

class LowLink:
    def __init__(self, v):
        def dfs(x, par):
            self.pre[x] = self.low[x] = self.cnt
            self.cnt += 1
            is_articulation = False
            n = 0
            for y in v[x]:
                if self.pre[y] is None:
                    n += 1
                    lowy = dfs(y, x)
                    if lowy < self.low[x]:
                        self.low[x] = lowy
                    if self.pre[x] <= lowy:
                        if self.pre[x]:
                            is_articulation = True
                        if self.pre[x] < lowy:
                            self.bridge.append((x,y))
                else:
                    if par != y and self.pre[y] < self.low[x]:
                        self.low[x] = self.pre[y]

            if par is None and n > 1:
                is_articulation = True

            if is_articulation:
                self.articulation.append(x)

            return self.low[x]


        self.size = len(v)
        self.pre = [None]*self.size
        self.low = [None]*self.size
        self.articulation = []
        self.bridge = []
        for x in range(self.size):
            if self.pre[x] is None:
                self.cnt = 0
                dfs(x, None)
