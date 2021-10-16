"""
NTT convolve : O((|A|+|B|)log(|A|+|B|))
calculate the convolution of A and B, using NTT

NTT : https://www.nayuki.io/page/number-theoretic-transform-integer-dft
implement : https://math314.hateblo.jp/entry/2015/05/07/014908
"""

mod = 469762049

def ntt(a, mod, n, sig=1):
    fa = a+[0]*(n-len(a))
    h = pow(3, (mod - 1) // n, mod)
    if sig < 0:
        h = pow(h, mod-2, mod)
    i = 0
    m = n >> 1
    for j in range(1, n - 1):
        k = m
        i ^= k
        while i < k:
            k >>= 1
            i ^= k
        if j < i:
            fa[i], fa[j] = fa[j], fa[i]
    m = 1
    while m < n:
        m2 = m << 1
        base = pow(h, n // m2, mod)
        w = 1
        for x in range(m):
            for i in range(x, n, m2):
                j = i + m
                u = fa[i]
                d = fa[j] * w
                if d >= mod:
                    d %= mod
                fai = u + d
                if mod <= fai:
                    fai -= mod
                fa[i] = fai
                faj = u - d
                if faj < 0:
                    faj += mod
                fa[j] = faj
            w *= base
            if w >= base:
                w %= mod
        m = m2

    for i in range(n):
        if fa[i] < 0:
            fa[i] += mod
    return fa


def intt(a, mod, n):
    inv = pow(n, mod-2, mod)
    res = ntt(a, mod, n, -1)
    return [ri*inv%mod for ri in res]


def convolve(a, b, mod):
    l = len(a)+len(b)
    n = 1<<(l-1).bit_length()
    Fa = ntt(a, mod, n)
    Fb = ntt(b, mod, n)
    F = [fa * fb % mod for fa, fb in zip(Fa,Fb)]
    f = intt(F, mod, n)
    return f[:l]


s = list(map(lambda x:int(x)*2-1, input()))
t = list(map(lambda x:1-int(x)*2, input()))[::-1]

f = [(i+len(t))%mod for i in conv(s,t,mod)[len(t)-1:len(s)]]
print(min(f)>>1)