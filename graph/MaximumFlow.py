"""
Maximum Flow : O(EV^2)
"""

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


    def _bfs(self, s, t):
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
        while self._bfs(s, t):
            continue
        return self.flow
