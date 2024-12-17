#!/usr/bin/env python

import heapq
from collections import defaultdict

input_file = "input"

data = {x + y * 1j: c for y, row in enumerate(open(input_file)) for x, c in enumerate(row.strip())}

start = next(k for k, v in data.items() if v == "S")
end = next(k for k, v in data.items() if v == "E")

pq = [(0, prio := 0, start, 1, [start])]
dist = defaultdict(lambda: float("inf"))
paths = set()
min_cost = float("inf")

while pq:
    cost, _, pos, d, path = heapq.heappop(pq)
    if cost > dist[pos, d]:
        continue
    else:
        dist[pos, d] = cost

    if data[pos] == "E" and cost <= min_cost:
        paths |= set(path)
        min_cost = cost

    for nd in (1, 1j, -1, -1j):
        npos = pos + nd
        if npos in dist or npos not in data or data[npos] == "#":
            continue

        heapq.heappush(
            pq,
            (cost + 1 + max(abs((d - nd).real), abs((d - nd).imag)) * 1000, prio := prio + 1, npos, nd, path + [npos]),
        )

print(int(min_cost))
print(len(paths))
