# LowLink
"""
橋と関節点の列挙
O(|V|+|E|)
"""

class LowLink:
    def __init__(self, v):
        self.size = len(v)
        self.v = v
        self.pre = [None]*self.size
        self.low = [None]*self.size
        self.articulation = []
        self.bridge = []
        for x in range(self.size):
            if self.pre[x] is None:
                self.cnt = 0
                self.dfs(x, None)

    def dfs(self, x, par):
        self.pre[x] = self.low[x] = self.cnt
        self.cnt += 1
        is_articulation = False
        n = 0
        for y in self.v[x]:
            if self.pre[y] is None:
                n += 1
                lowy = self.dfs(y, x)
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


n,m = map(int, input().split())
v = [[] for i in range(n)]
for i in range(m):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    v[a].append(b)
    v[b].append(a)
ans = LowLink(v)
print(len(ans.bridge))
