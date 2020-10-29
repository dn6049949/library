"""
Strongly Connected Components : O(V+E)
"""

import sys
from collections import deque
sys.setrecursionlimit(10**7)

def scc(v):
    n = len(v)
    def dfs(x):
        d[x] = 0
        for y in v[x]:
            if d[y]:
                dfs(y)
        path.append(x)
    
    def revbfs(x,i):
        q = deque([x])
        res[x] = i
        while q:
            x = q.popleft()
            for y in rev[x]:
                if res[y] is None:
                    res[y] = i
                    q.append(y)

    rev = [[] for _ in range(n)]
    for i,vi in enumerate(v):
        for j in v[i]:
            rev[j].append(i)
    
    path = []
    d = [1]*n
    for x in range(n):
        if d[x]:
            dfs(x)
    i = 0
    res = [None]*n
    for x in path[::-1]:
        if res[x] is None:
            revbfs(x,i)
            i += 1
    return res