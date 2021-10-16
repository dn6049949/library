"""
行列累乗 : O(H^3logN) (H : matri A の次元)
"""

def product(a,b):
    res = 0
    for ai,bi in zip(a,b):
        res += ai*bi
    return res


def _mul(a,b):
    bt = [tuple(v) for v in zip(*b)]
    return [[product(ai,bj) for bj in bt] for ai in a]


def _pow(a,n):
    res = [[1 if i == j else 0 for j in range(len(a))] for i in range(len(a))]
    while n:
        if n&1:
            res = _mul(res, a)
        a = _mul(a, a)
        n >>= 1
    return res
