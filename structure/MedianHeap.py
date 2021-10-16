from heapq import heappush, heappop

class MedianHeap:

    __slots__ = ["left", "right"]

    def __init__(self):
        self.left = [float("inf")]
        self.right = [float("inf")]

    def append(self, val):
        left = self.left
        right = self.right
        if len(left) == len(right):
            if val > right[0]:
                heappush(left, -heappop(right))
                heappush(right, val)
            else:
                heappush(left, -val)
        else:
            if val < -left[0]:
                heappush(right, -heappop(left))
                heappush(left, -val)
            else:
                heappush(right, val)

    def median(self):
        return -self.left[0]