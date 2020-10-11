from collections import deque
class SlidingWindowAggretgation:
    """
    f : モノイド
    swag.append(x) : xを追加 O(1)
    swag.popleft() : 左端を削除 O(1)
    swag.get() : f(swag) を取得 O(1)
    """
    def __init__(self, f = min, e = float("inf")):
        self.e = e
        self.f = f
        self.front_stack = deque()
        self.back_stack = deque()

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

    def get(self):
        res = self.e
        if self.front_stack:
            res = self.f(res, self.front_stack[-1][1])
        if self.back_stack:
            res = self.f(res, self.back_stack[-1][1])
        return res
