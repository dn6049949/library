# SlidingWindowAggretgation
"""
任意のモノイド(f(a,b))を載せられる
1. append
2. popleft
3. f(a_i, a_(i+1), … a_j) (a_i, a_(i+1), … a_j in stack)
の3つがすべてO(1)で計算、処理可能、空間はO(N)
"""

from collections import deque
class SlidingWindowAggretgation:
    def __init__(self, f = min, default = float("inf")):
        self.default = default
        self.f = f
        self.front_stack = deque()
        self.back_stack = deque()

    def get(self):
        res = self.default
        if self.front_stack:
            res = self.f(res, self.front_stack[-1][1])
        if self.back_stack:
            res = self.f(res, self.back_stack[-1][1])
        return res

    def append(self, x):
        fx = x
        if self.back_stack:
            fx = self.f(self.back_stack[-1][1], x)
        self.back_stack.append((x, fx))

    def popleft(self):
        if not self.front_stack:
            x, fx = self.back_stack.pop()
            self.front_stack.append((x, x))
            while self.back_stack:
                x, fx = self.back_stack.pop()
                fx = self.f(x, self.front_stack[-1][1])
                self.front_stack.append((x, fx))
        self.front_stack.pop()
