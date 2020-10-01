"""
Minimum Cost Flow : O(FElogV)
"""

from heapq import heappush, heappop

class MinCostFlow:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]


    def add_edge(self, fr, to, cap, cost):
        forward = [to, cap, cost, None]
        backward = forward[3] = [fr, 0, -cost, forward]
        self.graph[fr].append(forward)
        self.graph[to].append(backward)


    def flow(self, s, t, f):
        n = self.n
        g = self.graph

        res = 0
        h = [0]*n
        prv_v = [0]*n
        prv_e = [None]*n
        d0 = [float("inf")]*n
        dist = [float("inf")]*n

        while f:
            dist[:] = d0
            dist[s] = 0
            q = [(0, s)]

            while q:
                c, v = heappop(q)
                if dist[v] < c:
                    continue
                r0 = dist[v] + h[v]
                for e in g[v]:
                    w, cap, cost, _ = e
                    if cap > 0 and r0 + cost - h[w] < dist[w]:
                        dist[w] = r = r0 + cost - h[w]
                        prv_v[w] = v
                        prv_e[w] = e
                        heappush(q, (r, w))
            if dist[t] == float("inf"):
            	return None

            for i in range(n):
                h[i] += dist[i]

            d = f
            v = t
            while v != s:
                d = min(d, prv_e[v][1])
                v = prv_v[v]
            f -= d
            res += d * h[t]
            v = t
            while v != s:
                e = prv_e[v]
                e[1] -= d
                e[3][1] += d
                v = prv_v[v]
        return res
