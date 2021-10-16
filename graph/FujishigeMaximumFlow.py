"""
Maximum Flow : O(VElog(U))
fujishige's algorithm
ref: https://37zigen.com/fujishige/
"""


class MaximumFlow:
    __slots__ = ["n", "graph", "u"]

    def __init__(self, n):
        self.n = n
        self.graph = [[] for i in range(n)]
        self.u = 0


    def add_edge(self, fr, to, cap=1):
        if self.u < cap:
            self.u = cap
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.graph[fr].append(forward)
        self.graph[to].append(backward)


    def flow(self, s, t):
        n = self.n
        u = self.u
        graph = self.graph
        ex_flow = [0]*n
        while u:
            in_cap = [0]*n
            check = [0]*n
            check[s] = 1
            check_list = [s]
            for x in check_list:
                for y,cap,_ in graph[x]:
                    in_cap[y] += cap
                    if not check[y] and in_cap[y] >= u:
                        check[y] = 1
                        check_list.append(y)
                        if y == t:
                            break

            if not check[t]:
                u >>= 1
                continue

            ex_flow[t] = u
            for x in check_list[:0:-1]:
                for e in graph[x]:
                    y, cap, rev = e
                    if not check[y]:
                        continue
                    f = min(rev[1], ex_flow[x])
                    e[1] += f
                    rev[1] -= f
                    ex_flow[x] -= f
                    ex_flow[y] += f
                check[x] = 0
        return ex_flow[0]
