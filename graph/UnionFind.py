def root(x):
    if x == par[x]:
        return x
    par[x] = root(par[x])
    return par[x]

def unite(x,y):
    x = root(x)
    y = root(y)
    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1

par = list(range(n))
rank = [0]*n
