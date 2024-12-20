#!/usr/bin/env python
import itertools
from collections import deque

input_file = "input"
threshold = 1 if input_file == "test_input" else 100

data = {x + y * 1j: c for y, row in enumerate(open(input_file)) for x, c in enumerate(row.strip())}

start = next(p for p in data if data[p] == "S")


distances = {start: 0}
queue = deque([start])
while queue:
    pos = queue.popleft()
    for npos in pos - 1, pos + 1, pos - 1j, pos + 1j:
        if npos in data and npos not in distances and data[npos] != "#":
            distances[npos] = distances[pos] + 1
            queue.append(npos)


def solve(cheat_distance):
    for (pos1, dist1), (pos2, dist2) in itertools.combinations(distances.items(), 2):
        dist = abs((pos1 - pos2).real) + abs((pos1 - pos2).imag)
        if cheat_distance(dist) and dist2 - dist1 - dist >= threshold:
            yield 1


print(sum(solve(lambda x: x == 2)))
print(sum(solve(lambda x: x <= 20)))
