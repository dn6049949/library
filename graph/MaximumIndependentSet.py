"""
Maximum Independent Set : O(N2^(N/2))
(cograph : Maximum Clique)
"""

def MaximumIndependentSet(n, v, co=False):
    if co: # cograph for maximum clique
        for i in range(n):
            f = [1]*n
            for j in v[i]:
                f[j] = 0
            v[i] = []
            for j in range(n):
                if f[j]:
                    v[i].append(j)
    mid = n>>1
    n1 = mid
    B1 = 1<<n1
    f1 = [1]*B1
    for i in range(mid):
        for j in v[i]:
            if j >= mid:continue
            f1[(1<<i)|(1<<j)] = 0
    for s in range(B1):
        if not f1[s]:
            for i in range(n1):
                f1[s|(1<<i)] = 0

    dp1 = [0]
    for i in range(n1):
        dp1 += [i+1 for i in dp1]
    for s in range(B1):
        if not f1[s]:
            dp1[s] = 0

    n2 = n-mid
    B2 = 1<<n2
    f2 = [1]*B2
    for i in range(mid,n):
        x = i-mid
        for j in v[i]:
            if j < mid:continue
            y = j-mid
            f2[(1<<x)|(1<<y)] = 0
    for s in range(B2):
        if not f2[s]:
            for i in range(n2):
                f2[s|(1<<i)] = 0

    dp2 = [0]
    for i in range(n2):
        dp2 += [i+1 for i in dp2]
    for s in range(B2):
        if not f2[s]:
            dp2[s] = 0

    for s in range(B2):
        for i in range(n2):
            ns = s|(1<<i)
            if dp2[ns] < dp2[s]:
                dp2[ns] = dp2[s]

    t = [B2-1]*B1
    for i in range(n1):
        s = 1<<i
        for j in v[i]:
            if j < mid:continue
            t[s] ^= 1<<(j-mid)
    for s in range(B1):
        for i in range(n1):
            bi = 1<<i
            if s&bi:continue
            t[s|bi] = t[s]&t[bi]

    res = 0
    for s in range(B1):
        m = dp1[s]+dp2[t[s]]
        if res < m:
            res = m
    return res
