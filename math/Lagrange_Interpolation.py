# ラグランジュ補間O(N^2)またはO(N)
"""
N+1個の点列(xi,yi)を通るN次多項式を計算(%mod)
(1) f(x)のxの係数の取得 O(N^2) (f(t)の取得は係数をもとにO(N)でできる)
(2) f(t)の取得 O(N) (条件 : 与えられる点列のxが等差数列)
 ((2) のとき、fi(xi) = d^n*i!(n-i)!*(-1)^(n+1-i) (xi = x0+i*d, d : 公差))
https://ferin-tech.hatenablog.com/entry/2019/08/11/%E3%83%A9%E3%82%B0%E3%83%A9%E3%83%B3%E3%82%B8%E3%83%A5%E8%A3%9C%E9%96%93
"""

mod = 1000000007

"""
(1) f(x)のxの係数の取得 O(N^2) (f(t)の取得は係数をもとにO(N)でできる)
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

n = int(input())
a = list(map(int, input().split()))
t = int(input())
x = range(n+1)
f = lagrange_interpolation(x,a)
ans = 0
p = 1
for i in range(n+1):
    ans += f[i]*p
    ans %= mod
    p *= t
    p %= mod
print(ans)

"""
(2) f(t)の取得 O(N) (条件 : 与えられる点列のxが等差数列)
"""

N = 6*10**5
fact = [1]
for i in range(1,N+1):
    fact.append(fact[-1]*i%mod)

inv = [None]*(N+1)
inv[-1] = pow(fact[-1],mod-2,mod)
for i in range(N)[::-1]:
    inv[i] = inv[i+1]*(i+1)%mod

def lagrange_interpolation(x,y,t,mod=mod):
    n = len(x)-1
    d = x[1]-x[0]
    f = 1
    for i in range(n+1):
        f *= t-x[i]
        f %= mod
    res = 0
    for i in range(n+1):
        if x[i] == t:
            return y[i]
        fi = inv[i]*inv[n-i]
        if (n-i)&1:
            fi *= -1
        fi %= mod
        res += y[i]*f*fi*pow(t-x[i],mod-2,mod)%mod
        res %= mod
    return res*pow(d,mod-2,mod)%mod

n = int(input())
a = list(map(int, input().split()))
t = int(input())
x = range(n+1)
print(lagrange_interpolation(x,a,t))
