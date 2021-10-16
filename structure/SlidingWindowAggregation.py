from collections import deque

class SlidingWindowAggretgation:
    """
    f : モノイド
    swag.append(x) : xを追加 O(1)
    swag.popleft() : 左端を削除 O(1) amortized
    swag.get() : f(swag) を取得　O(1)，空のとき None を返す
    """
    __slots__ = ["f", "front_stack", "back_stack"]

    def __init__(self, f=min):
        self.f = f
        self.front_stack = deque()
        self.back_stack = deque()

    def __len__(self):
        return len(self.back_stack) + len(self.front_stack)

    def __bool__(self):
        return len(self) > 0

    def __str__(self):
        data = [x for x,_ in self.front_stack][::-1] + [x for x,_ in self.back_stack]
        return str(data)

    def append(self, x):
        fx = x
        if self.back_stack:
            fx = self.f(self.back_stack[-1][1], x)
        self.back_stack.append((x, fx))

    def popleft(self):
        if not self.front_stack:
            x = fx = self.back_stack.pop()[0]
            self.front_stack.append((x, fx))
            while self.back_stack:
                x = self.back_stack.pop()[0]
                fx = self.f(x, fx)
                self.front_stack.append((x, fx))
        self.front_stack.pop()

    def get(self):
        res = None
        if self.front_stack:
            res = self.front_stack[-1][1]
        if self.back_stack:
            if res is None:
                res = self.back_stack[-1][1]
            else:
                res = self.f(res, self.back_stack[-1][1])
        return res
