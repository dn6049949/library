"""
LinearRecurrenceSequence(g, mod): Class for sequences whose first few terms consist of g and satisfy a certain linear gradation formula
berlekamp_massey: Calculate the reduction formula
ref : https://de.wikipedia.org/wiki/Berlekamp-Massey-Algorithmus

bostan_mori: Calculate the N-th term of a linear recurrence sequence.
ref: http://q.c.titech.ac.jp/docs/progs/polynomial_division.html
"""


class LinearRecurrenceSequence:
    __slots__ = ["g", "mod"]
    def __init__(self, g, mod=None):
        assert(len(g) > 1)
        if mod is None:
            from fractions import Fraction
            self.g = list(map(Fraction, g))
        else:
            self.g = list(map(lambda x:x%mod, g))
        self.mod = mod

    def berlekamp_massey(self):
        mod = self.mod
        g = self.g
        n = len(g)
        c = [0]*n
        cl = [0]*n
        c[0] = cl[0] = 1
        L = 0
        l = dl = -1
        if mod is None:
            for i in range(n):
                d = sum([ci*gj for ci,gj in zip(c[:L+1],g[i-L:i+1][::-1])])
                while d != 0:
                    tmp = c[:]
                    coef = d/dl
                    for k in range(n-i+l):
                        c[i-l+k] -= coef*cl[k]
                    if 2*L <= i:
                        l = i
                        cl = tmp[:]
                        dl = d
                        L = i+1-L
                    d = sum([ci*gj for ci,gj in zip(c[:L+1],g[i-L:i+1][::-1])])
        else:
            for i in range(n):
                d = sum([ci*gj%mod for ci,gj in zip(c[:L+1],g[i-L:i+1][::-1])])%mod
                while d != 0:
                    tmp = c[:]
                    coef = d*dl
                    if coef >= mod:
                        coef %= mod
                    for k in range(n-i+l):
                        j = i-l+k
                        c[j] -= coef*cl[k]
                        if c[j] < 0:
                            c[j] %= mod
                    if 2*L <= i:
                        l = i
                        cl = tmp[:]
                        dl = pow(d,mod-2,mod)
                        L = i+1-L
                    d = sum([ci*gj%mod for ci,gj in zip(c[:L+1],g[i-L:i+1][::-1])])%mod
        for i in range(n)[::-1]:
            if c[i]:
                break
        return c[:i+1]


    def _mul(self, p, q):
        mod = self.mod
        res = [0]*(len(p)+len(q)-1)
        if mod is None:
            for i, pi in enumerate(p):
                for j, gj in enumerate(q):
                    res[i+j] += pi*gj
        else:
            for i, pi in enumerate(p):
                for j, gj in enumerate(q):
                    k = i+j
                    nr = res[k]+pi*gj
                    if nr < 0 or nr >= mod:
                        nr %= mod
                    res[k] = nr
        return res


    def _mul_even(self, p, q):
        mod = self.mod
        res = [0]*((len(p)+len(q))>>1)
        if mod is None:
            for i, pi in enumerate(p):
                for j, gj in enumerate(q):
                    k = i+j
                    if not k&1:
                        res[k>>1] += pi*gj
        else:
            for i, pi in enumerate(p):
                for j, gj in enumerate(q):
                    k = i+j
                    if not k&1:
                        k >>= 1
                        nr = res[k]+pi*gj
                        if nr < 0 or nr >= mod:
                            nr %= mod
                        res[k] = nr
        return res


    def _mul_odd(self, p, q):
        mod = self.mod
        res = [0]*((len(p)+len(q))>>1)
        if mod is None:
            for i, pi in enumerate(p):
                for j, gj in enumerate(q):
                    k = i+j
                    if k&1:
                        res[k>>1] += pi*gj
        else:
            for i, pi in enumerate(p):
                for j, gj in enumerate(q):
                    k = i+j
                    if k&1:
                        k >>= 1
                        nr = res[k]+pi*gj
                        if nr < 0 or nr >= mod:
                            nr %= mod
                        res[k] = nr
        return res


    def bostan_mori(self, n):
        q = self.berlekamp_massey()
        p = self._mul(self.g,q)[:len(q)-1]
        while n:
            q_ = [qi if not i&1 else -qi for i, qi in enumerate(q)]
            q = self._mul_even(q, q_)
            if not n&1:
                p = self._mul_even(p, q_)
            else:
                p = self._mul_odd(p, q_)
            n >>= 1
        return p[0]
