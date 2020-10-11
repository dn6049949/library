"""
S(n,k) = 1^k + 2^k + .. + n^kを求める : O(KlogMOD)

(1) n <= k+1
 O(nlogk)で普通に求められる.

(2) n > k+1
 S(n,k) = Sigma(i = 0 -> k+1)S(i,k)fi(n)/fi(xi)
 (ラグランジュ補間, fi(x) = Pi(j = 0 -> k+1 & j != i)(x-xj), xj = j)
 fi(xi) = fi(i) = Pi(j = 0 -> k+1 & j != i)(i-xj)
        = Pi(j = 0 -> k+1 & j != i)(i-j)
        = (i-0)(i-1)..(i-(i-1))(i-(i+1))(i-(i+2))..(i-(k+1))
        = i!(k+1)!(-1)^(k+2-i) (負の数がk+1-i個)
 →
 S(n,k) = Sigma(i = 0 -> k+1)S(i,k)fi(n)/i!(k+1)!(-1)^(k+2-i)
        = Sigma(i = 0 -> k+1)S(i,k)f/(n-i)i!(k+1)!(-1)^(k+2-i) (f = Pi(j = 0 -> k+1)(n-xj))
 →
 階乗を持っておけばO(logK)でS(i,k)f/(n-i)i!(k+1)!(-1)^(k+2-i)を求められる。
 (S(i,k)がボトルネック, S(i,k) = S(i-1,k)+i^k)
 合計(O(KlogK))
"""

mod = 1000000007

def sum_of_powers(n,k):
    if n <= k+1:
        res = 0
        for i in range(1,n+1):
            res += pow(i,k,mod)
            res %= mod
        return res

    fact = 1
    for i in range(2,k+1):
        fact *= i
        if fact >= mod:
            fact %= mod

    inv = [None]*(k+2)
    inv[-1] = pow(fact, mod-2, mod)
    for i in range(k+1)[::-1]:
        inv[i] = inv[i+1]*(i+1)%mod

    f = 1
    for i in range(k+2):
        f *= n-i
        f %= mod

    si = 0
    res = 0
    for i in range(1,k+2):
        fi = inv[i]*inv[k+1-i]
        if not (k+2-i)&1:
            fi *= -1
        fi %= mod
        si += pow(i,k,mod)
        si %= mod
        res += si*f*fi*pow(n-i,mod-2,mod)%mod
        res %= mod
    return res
