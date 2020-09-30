# 最大流 O(EV^2)

from collections import deque

class Dinic:
    def __init__(self, size):
        self.size = size
        self.graph = [[] for _ in range(size)]
        self.cap = [[0]*size for _ in range(size)]

    def add_edge(self, fr, to, cap=1):
        self.graph[fr].append(to)
        self.graph[to].append(fr)
        self.cap[fr][to] = cap

    def bfs(self, s, t):
        self.level = [None]*self.size
        pre = [None]*self.size
        self.level[s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            if v == t:
                break
            lv = self.level[v] + 1
            for w in self.graph[v]:
                if self.cap[v][w] and self.level[w] is None:
                    self.level[w] = lv
                    pre[w] = v
                    q.append(w)
        else:
            return False

        path = [t]
        f = float("inf")
        w = t
        while w != s:
            v = pre[w]
            path.append(v)
            cap = self.cap[v][w]
            if cap < f:
                f = cap
            w = v

        for i in range(1, len(path)):
            v, w = path[-i],path[-i-1]
            self.cap[v][w] -= f
            self.cap[w][v] += f

        self.flow += f
        return True


    def flow(self, s, t):
        self.flow = 0
        while self.bfs(s, t):
            continue
        return self.flow


n,m,K = map(int, input().split())
c = list(map(lambda x:ord(x)-ord("a"), input().split()))
v = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    v[a].append(b)
    v[b].append(a)
d = []
q = deque()
for i in range(n):
    q.append(i)
    di = [float("inf")]*n
    di[i] = 0
    while q:
        x = q.popleft()
        nd = di[x]+1
        if nd > K:
            continue
        for y in v[x]:
            if nd < di[y]:
                di[y] = nd
                q.append(y)
    d.append(di)

g = Dinic(n+2)
for i in range(n):
    ci = c[i]
    if not ci&1:
        g.add_edge(0,i+1)
        for j in range(n):
            if d[i][j] > K:
                continue
            if (ci-c[j])%26 in (1,25):
                g.add_edge(i+1,j+1)
    else:
        g.add_edge(i+1,n+1)
print(g.flow(0,n+1))
