# 1-indexedSegmentTree
"""
任意のモノイド(f(a,b))を載せられる
1. a_i = f(a_i,b)
2. a_i = b
3. f(a_i, a_(i+1), … a_j)
の3つがすべてO(logN)で計算、処理可能、空間はO(N)
子は i*2, i*2+1
親は i>>1
左からi番目の葉 i+N
"""

class SegmentTree:
    def __init__(self, size, f=lambda x,y : x+y, default=0):
        self.size = 2**(size-1).bit_length()
        self.default = default
        self.dat = [default]*(self.size*2)
        self.f = f

    def update(self, i, x):
        i += self.size
        self.dat[i] = x
        while i > 0:
            i >>= 1
            self.dat[i] = self.f(self.dat[i*2], self.dat[i*2+1])

    def get(self, a, b=None):
        if b is None:
            b = a + 1
        l, r = a + self.size, b + self.size
        lres, rres = self.default, self.default
        while l < r:
            if l & 1:
                lres = self.f(lres, self.dat[l])
                l += 1

            if r & 1:
                r -= 1
                rres = self.f(self.dat[r], rres)
            l >>= 1
            r >>= 1
        res = self.f(lres, rres)
        return res

n,L = map(int, input().split())
light = [list(map(int, input().split())) for i in range(n)]
light.sort()
dp = SegmentTree(L+1,float("inf"),min)
dp.update(0,0)
for l, r, c in light:
    mi = dp.get(l,r)
    dp.update(r,min(dp.get(r),mi+c))
print(dp.get(L))
