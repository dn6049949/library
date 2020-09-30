import math
from collections import deque
import sys
input = sys.stdin.buffer.readline

def lca(x, y):
    if d[x] < d[y]:
        x,y = y,x
    dy = d[y]
    k = d[x]-dy
    while k:
        x = p[x][int(math.log(k,2))]
        k = d[x]-dy

    if x == y:
        return x

    for i in range(h)[::-1]:
        if p[x][i] != p[y][i]:
            x = p[x][i]
            y = p[y][i]
    return p[x][0]

n = int(input())
v = [[] for i in range(n)]
for i in range(n-1):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    v[a].append(b)
    v[b].append(a)

# bfsで各ノードの親を取得
d = [0]*n
d[0] = 1
p = [[] for i in range(n)]
p[0].append(0)
q = deque([0])
while q:
    x = q.popleft()
    nd = d[x]+1
    for y in v[x]:
        if not d[y]:
            d[y] = nd
            p[y].append(x)
            q.append(y)

# p[x][i] := xの2^i個上のノード
h = int(math.log(max(d),2))+1
for i in range(h-1):
    for x in range(n):
        p[x].append(p[p[x][i]][i])

q = int(input())
for _ in range(q):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    print(d[a]+d[b]-2*d[lca(a,b)]+1)
