class SegmentTree:
    """
    f : モノイド
    zero : 零元
    seg.update(i,x) : a[i] = x に更新 O(logN)
    seg.get(l,r) : f(a[l:r]) を取得　O(logN)
    """
    def __init__(self, size, f=lambda x,y : x+y, zero=0):
        self.size = 2**(size-1).bit_length()
        self.zero = zero
        self.dat = [zero]*(self.size*2)
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
        lres, rres = self.zero, self.zero
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
