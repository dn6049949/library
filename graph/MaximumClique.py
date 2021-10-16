"""
Maximum Clique: O(1.??^N) (C++, N <= 111 : OK)
ref: https://atcoder.jp/contests/code-thanks-festival-2017-open/submissions/2691674
cograph: Maximum Independent Set
"""

class MaximumClique:

    __slots__ = ["n", "max_bit", "v", "v_", "stk", "ans", "cans", "index"]


    def __init__(self, v):
        self.n = len(v)
        self.max_bit = ~-(1<<self.n)
        self.v = v[:]


    def _dfs(self, elem_num, candi):
        stk = self.stk
        if self.ans < elem_num:
            self.ans = elem_num
            cans = 0
            index = self.index
            for x in stk[:elem_num]:
                cans |= 1 << index[x]
            self.cans = cans

        potential = elem_num + bin(candi).count("1")
        if potential <= self.ans:
            return
        v_ = self.v_
        pivot = candi & -candi
        smaller_candi = candi & ~v_[pivot.bit_length() - 1]
        while smaller_candi and potential > self.ans:
            next_ = smaller_candi & -smaller_candi
            candi ^= next_
            smaller_candi ^= next_
            potential -= 1
            next__ = next_.bit_length() - 1
            if next_ == pivot or smaller_candi & v_[next__]:
                stk[elem_num] = next__
                self._dfs(elem_num + 1, candi & v_[next__])


    def _solve(self):
        self.stk = [0]*self.n
        self.cans = 1
        self.ans = 1
        self._dfs(0, self.max_bit)
        return self.ans


    def maximum_clique(self):
        v = self.v
        deg = [len(vx) for vx in v]
        lis = list(range(self.n))
        lis.sort(key = lambda x: -deg[x])
        index = self.index = {x: i for i, x in enumerate(lis)}

        self.v_ = [None]*self.n
        for i, x in enumerate(lis):
            b = 0
            for y in v[x]:
                b |= 1 << index[y]
            self.v_[i] = b
        return self._solve()


    def maximum_independent_set(self):
        v = self.v
        deg = [len(vx) for vx in v]
        lis = list(range(self.n))
        lis.sort(key = lambda x: deg[x])
        index = self.index = {x: i for i, x in enumerate(lis)}

        max_bit = self.max_bit
        self.v_ = [None]*self.n
        for i, x in enumerate(lis):
            b = max_bit ^ (1 << i)
            for y in v[x]:
                b ^= 1 << index[y]
            self.v_[i] = b
        return self._solve()
