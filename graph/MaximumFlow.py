"""
Maximum Flow : O(V^2E)
ref: https://tjkendev.github.io/procon-library/python/max_flow/dinic.html
"""

from collections import deque

class Dinic:
    __slots__ = ["n", "graph", "level", "it"]


    def __init__(self, n):
        self.n = n
        self.graph = [[] for i in range(n)]


    def add_edge(self, fr, to, cap=1):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.graph[fr].append(forward)
        self.graph[to].append(backward)


    def bfs(self, s, t):
        self.level = level = [None]*self.n
        deq = deque([s])
        level[s] = 0
        graph = self.graph
        while deq:
            v = deq.popleft()
            lv = level[v] + 1
            for w, cap, _ in graph[v]:
                if cap and level[w] is None:
                    level[w] = lv
                    deq.append(w)
        return level[t] is not None


    def dfs(self, v, t, f):
        if v == t:
            return f
        level = self.level
        for e in self.graph[v]:
            w, cap, rev = e
            if cap and level[v] < level[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0


    def flow(self, s, t):
        flow = 0
        graph = self.graph
        while self.bfs(s, t):
            f = float("inf")
            while f:
                f = self.dfs(s, t, float("inf"))
                flow += f
        return flow
