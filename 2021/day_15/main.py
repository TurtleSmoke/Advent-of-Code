#!/usr/bin/env python
from heapq import heappop, heappush

data = [[int(x) for x in line] for line in open("test_input", "r").read().splitlines()]

print(data)


def shortest_path(t):
    heap = [(0, 0, 0)]
    seen = {(0, 0)}
    while heap:
        d, x, y = heappop(heap)
        if x == t * len(data) - 1 and y == t * len(data[0]) - 1:
            return d

        for dx, dy in ((0, 1), (1, 0), (1, 0), (-1, 0)):
            x_, y_ = x + dx, y + dy

            if x_ < 0 or x_ >= t * len(data) or y_ < 0 or y_ >= t * len(data[0]) or (x_, y_) in seen:
                continue

            a, am = divmod(x_, len(data))
            b, bm = divmod(y_, len(data[0]))
            n = ((data[am][bm] + a + b) - 1) % 9 + 1

            seen.add((x_, y_))
            heappush(heap, (d + n, x_, y_))


print(shortest_path(1))
print(shortest_path(5))
