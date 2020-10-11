"""
行列累乗 : O(H^3logN) (H : matri A の次元)
"""

# 行列演算に用いる演算add,mulおよびmulの単位元,零元
mod = 1000000007
def add(x,y):
    res = x+y
    if res >= mod:
        res %= mod
    return res

def mul(x,y):
    res = x*y
    if res >= mod:
        res %= mod
    return res

e = 1
zero = 0

# 内積
def product(a, b):
    res = zero
    for i in range(len(a)):
        res = add(res,mul(a[i],b[i]))
    return res

# 行列積
def _mul(a, b):
    bt = [list(v) for v in zip(*b)]
    return [[product(ai,bj) for bj in bt] for ai in a]

# 行列累乗
def _pow(a, n):
    res = [[e if i == j else zero for j in range(len(a))] for i in range(len(a))]
    while n:
        if n&1:
            res = _mul(res, a)
        a = _mul(a, a)
        n >>= 1
    return res
