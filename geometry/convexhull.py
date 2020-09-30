# 凸包 O(NlogN)

def det(a,b):
    return a[0]*b[1]-a[1]*b[0]

def minus(a,b):
    return (a[0]-b[0],a[1]-b[1])

def convex_hull(ps):
    n = len(ps)
    ps.sort()
    k = 0
    qs = [0]*(n+2)
    for i in range(n):
        while k > 1 and det(minus(qs[k-1], qs[k-2]), minus(ps[i], qs[k-1])) < 0:
            k -= 1
        qs[k] = ps[i]
        k += 1
    t = k
    for i in range(n-1)[::-1]:
        while k > t and det(minus(qs[k-1], qs[k-2]), minus(ps[i], qs[k-1])) < 0:
            k -= 1
        qs[k] = ps[i]
        k += 1
    qs = qs[:min(n,k-1)]
    return qs
