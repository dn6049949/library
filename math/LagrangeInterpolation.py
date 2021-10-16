"""
ラグランジュ補間
N+1個の点列(xi,yi)を通るN次多項式を計算(%mod)

(1) f(x)のxの係数の取得 : O(N^2) (f(t)の取得は係数をもとにO(N)でできる)
(2) f(t)の取得 : O(N) (条件 : 与えられる点列のxが等差数列)
参考 : https://ferin-tech.hatenablog.com/entry/2019/08/11/%E3%83%A9%E3%82%B0%E3%83%A9%E3%83%B3%E3%82%B8%E3%83%A5%E8%A3%9C%E9%96%93
"""

mod = 1000000007

"""
(1) f(x)のxの係数の取得 : O(N^2) (f(t)の取得は係数をもとにO(N)でできる)
"""
def lagrange_interpolation(x,y,mod=mod):
    n = len(x)-1
    dp = [0]*(n+2)
    dp[0] = x[0]
    dp[1] = 1
    for i in range(n):
        nd = [0]*(n+2)
        ni = i+1
        for j in range(n+2):
            nj = j
            nd[nj] += -x[ni]*dp[j]
            nd[nj] %= mod
            if j <= n:
                nj = j+1
                nd[nj] += dp[j]
                nd[nj] %= mod
        for j in range(n+2):
            dp[j] = nd[j]

    f = [0]*(n+1)
    for i in range(n+1):
        if y[i] == 0:
            continue
        fi = 1
        for j in range(n+1):
            if i == j:
                continue
            fi *= x[i]-x[j]
            fi %= mod
        fi = pow(fi,mod-2,mod)
        p = [0]*(n+1)
        if x[i] == 0:
            for j in range(n+1):
                p[j] = dp[j+1]
        else:
            inv = pow(x[i],mod-2,mod)
            p[0] = -dp[0]*inv%mod
            for j in range(1,n+1):
                p[j] = (p[j-1]-dp[j])*inv%mod
        for j in range(n+1):
            f[j] += y[i]*fi*p[j]
            f[j] %= mod
    return f


"""
(2) f(t)の取得 : O(N) (条件 : 与えられる点列のxが等差数列)
"""

def lagrange_interpolation(xs, ys, x, mod=mod):
    x %= mod
    if x in xs:
        return ys[xs.index(x)]

    m = len(xs)-1

    inv = [1]*(m+1)
    fact = 1
    for i in range(2,m+1):
        fact *= i
        if fact >= mod:
            fact %= mod
    inv[m] = pow(fact,mod-2,mod)
    for i in range(m)[::-1]:
        inv[i] = inv[i+1]*(i+1)%mod

    right = [1]*(m+1)
    for i in range(m)[::-1]:
        right[i] = right[i+1]*(x-xs[i+1])%mod
    
    left = [1]*(m+1)
    for i in range(m):
        left[i+1] = left[i]*(x-xs[i])%mod

    res = 0
    for i,yi in enumerate(ys):
        tmp = yi*right[i]%mod*left[i]%mod*inv[i]%mod*inv[m-i]%mod
        if (m^i)&1:
            res -= tmp
        else:
            res += tmp
        if res < 0 or mod <= res:
            res %= mod
    return res*pow(xs[1]-xs[0],m*(mod-2)%(mod-1),mod)%mod
