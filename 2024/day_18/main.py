#!/usr/bin/env python
import re
from bisect import bisect
from collections import deque

input_file = "input"
data = [int(x) + int(y) * 1j for x, y in re.findall(r"(\d+),(\d+)", open(input_file).read())]


def dfs(grid, grid_size):
    queue = deque([(0, 0)])
    visited = set()
    while queue:
        pos, cost = queue.popleft()
        if pos in visited:
            continue
        if pos == grid_size + grid_size * 1j:
            return cost

        visited.add(pos)
        for d in [1, -1, 1j, -1j]:
            npos = pos + d
            if 0 <= npos.real <= grid_size and 0 <= npos.imag <= grid_size and npos not in grid:
                queue.append((npos, cost + 1))
    return float("inf")


print(dfs(set(data[:1024]), 6 if input_file == "test_input" else 70))
print(
    data[
        bisect(range(len(data)), 1e9 - 1, key=lambda x: dfs(set(data[:x]), 6 if input_file == "test_input" else 70)) - 1
    ]
)
