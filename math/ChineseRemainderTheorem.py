# 中国剰余定理 O(nlogmaxm)
"""
x ≡ b1 (mod m1)
x ≡ b2 (mod m2)
…
x ≡ bn (mod mn)
の解x ≡ r (mod m)をO(nlogmaxm)で求める
返り値:(r,m)
解がない場合は(0,-1)を返す
"""

def extgcd(a, b):
    p, q, pre_p, pre_q = 1, 0, 0, 1
    while b:
        m = a//b
        a, b = b, a%b
        p, q, pre_p, pre_q = pre_p, pre_q, p-m*pre_p, q-m*pre_q
    return a, p, q

def crt(equation):
    r, m = equation[0]
    for b, m2 in equation[1:]:
        g, p, q = extgcd(m, m2)
        if (b-r)%g != 0:
            return 0, -1
        m, r = m*(m2//g), r+m*((b-r)//g*p%(m2//g))
        r %= m
    return r, m

def solve():
    def f(n):
        yield 1
        i = 2
        while i**2 <= n:
            if n%i == 0:
                m = n//i
                yield i
                if m != i:
                    yield m
            i += 1

    n = int(inpt())
    N = 2*n
    k = float("inf")
    for x in f(N):
        eq = [[0,x],[-1,N//x]]
        r,m = crt(eq)
        if m >= 0 and r < k:
            k = r
    print(k)
    return

#Solve
if __name__ == "__main__":
    solve()
