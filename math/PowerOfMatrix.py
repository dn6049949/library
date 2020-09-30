# 行列累乗 O(H^3logN) (H := matrix Aの次元)

# 行列演算に用いる演算add,mulおよびmulの単位元
add = lambda x,y:x+y
mul = lambda x,y:x*y
default = 1

# 内積
def product(a, b, mod=None):
    if mod is None:
        res = 0
        for i in range(len(a)):
            res = add(res,mul(a[i],b[i]))
        return res
    else:
        res = 0
        for i in range(len(a)):
            res = add(res,mul(a[i],b[i])%mod)
            if res >= mod:
                res %= mod
        return res

# 行列積
def mul_of_matrix(a, b, mod=None):
    bt = [[b[i][j] for i in range(len(b))] for j in range(len(b[0]))]
    return [[product(ai,bj,mod) for bj in bt] for ai in a]

# 行列累乗
def pow_of_matrix(a, n, mod=None):
    res = [[default if i == j else 0 for j in range(len(a))] for i in range(len(a))]
    while n:
        if n&1:
            res = mul_of_matrix(res,a,mod)
        a = mul_of_matrix(a,a,mod)
        n >>= 1
    return res

n,m = map(int, input().split())
mat = pow_of_matrix([[1,1],[1,0]],n-1,m)
print(mat[1][0])
