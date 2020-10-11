class BITSet:
    """
    set[i] : 集合のi番目に小さい要素を取得 O(logN)
    len(set) : 要素数 O(1)
    set.add(x) : xを追加 O(logN)
    set.remove(x) : xを削除 O(logN)
    set.mex() : 集合にない最小の非負整数を取得 O(logN)
    """
    def __init__(self, maxval):
        self.maxval = maxval+1
        self.bit = BIT(self.maxval)
        self.contain = [0]*self.maxval
        self.size = 0

    def __getitem__(self, key):
        return self.bit.bisect_left(key)

    def __len__(self):
        return self.size

    def add(self, key):
        if not self.contain[key]:
            self.size += 1
            self.contain[key] = 1
            self.bit.add(key)

    def remove(self, key):
        if self.contain[key]:
            self.size -= 1
            self.contain[key] = 0
            self.bit.add(key, -1)

    def mex(self):
        res = 0
        val = k = self.bit.maxbit
        while k:
            key = res + k
            if key <= self.maxval and self.bit.data[key] == k:
                val -= k
                res += k
            k >>= 1
        return res


class BIT:
    """
    bit.add(i, val) : s[i] += val O(logN)
    bit.sum(l, r) : s[l:r+1]の区間和、r指定なしのときs[:l]の区間和 O(logN)
    bit.bisect(val) : s[:i+1] >= valとなる最小のi O(logN)
    """
    def __init__(self, size):
        self.size = size + 1
        self.data = [0] * self.size
        self.maxbit = 1 << self.size.bit_length() - 1

    def add(self, key, val=1):
        key += 1
        while key < self.size:
            self.data[key] += val
            key += key & -key

    def sum(self, left, right=None):
        lres = 0
        while left:
            lres += self.data[left]
            left -= left & -left
        if right is None:
            return lres
        right += 1
        rres = 0
        while right:
            rres += self.data[right]
            right -= right & -right
        return rres - lres

    def bisect_left(self, val):
        res = 0
        k = self.maxbit
        while k:
            key = res + k
            if key < self.size and self.data[key] < val:
                val -= self.data[key]
                res += k
            k >>= 1
        return res
