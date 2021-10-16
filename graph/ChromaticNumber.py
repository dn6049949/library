"""
Chromatic Number: O(2^N(logN)^2)
ref: https://drken1215.hatenablog.com/entry/2019/01/16/030000
cograph: Minimum number of divisions when dividing the graph into cliques.

I -> dp
f -> pow(dp[s], k)
g[V] -> g
"""


def chromatic_number(v, co=False):
    n = len(v)
    e = [None]*n
    for x, vx in enumerate(v):
        b = 1 << x if not co else 0
        for y in vx:
            b |= 1 << y
        if co:
            b = ~b
        e[x] = b

    B = 1 << n
    dp = [0]*B
    dp[0] = 1
    for s in range(1, B):
        lsb = s & -s
        x = lsb.bit_length() - 1
        dp[s] = dp[s ^ lsb] + dp[s & ~e[x]]

    l = 0
    r = n
    while l+1 < r:
        k = (l+r) >> 1
        g = 0
        for i in range(B):
            s = i ^ (i >> 1)
            if i & 1:
                g += pow(dp[s], k)
            else:
                g -= pow(dp[s], k)
        if g:
            r = k
        else:
            l = k
    return r
