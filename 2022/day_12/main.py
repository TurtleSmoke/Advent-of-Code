#!/usr/bin/env python
from heapq import heappop, heappush
import numpy as np

val_input = "input"

grid = np.array([list(map(ord, line)) for line in open(val_input).read().splitlines()])
source, target = np.where(grid == ord("S")), np.where(grid == ord("E"))
grid[source] = ord("a")
grid[target] = ord("z")


def shortest_path(starts, end):
    heap = [(0, *start) for start in starts]
    seen = {*starts}
    while heap:
        d, x, y = heappop(heap)
        if (x, y) == end:
            return d

        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            x_, y_ = x + dx, y + dy

            if (
                0 <= x_ < len(grid)
                and 0 <= y_ < len(grid[0])
                and (x_, y_) not in seen
                and grid[x_, y_] <= grid[x, y] + 1
            ):
                seen.add((x_, y_))
                heappush(heap, (d + 1, x_, y_))


print(shortest_path(list(zip(*source)), *zip(*target)))
print(shortest_path(list(zip(*np.where(grid == ord("a")))), *zip(*target)))
