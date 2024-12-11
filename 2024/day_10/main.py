#!/usr/bin/env python

from collections import deque

input_file = "input"

data = {y + x * 1j: int(v) for x, row in enumerate(open(input_file)) for y, v in enumerate(row.strip())}

starts = [pos for pos in data if data[pos] == 0]


def dfs(start):
    visited = [start]
    queue = deque([start])
    while queue:
        current = queue.popleft()
        for neighbor in [current + 1, current - 1, current + 1j, current - 1j]:
            if neighbor in data and data[current] == data[neighbor] - 1:
                visited.append(neighbor)
                queue.append(neighbor)

    return visited


print(sum(len(set(x for x in dfs(start) if data[x] == 9)) for start in starts))
print(sum(sum(1 for x in dfs(start) if data[x] == 9) for start in starts))
