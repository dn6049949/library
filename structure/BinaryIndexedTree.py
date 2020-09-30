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
