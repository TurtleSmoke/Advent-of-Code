#!/usr/bin/env python
from collections import defaultdict

file_input = "input"

val = [line.split() for line in open(file_input).read().splitlines()]
sizes = defaultdict(int)
path = []

for v in val:
    if v[0] == "$":
        if v[1] == "cd":
            path.pop() if v[2] == ".." else path.append(v[2])
    elif v[0] != "dir":
        for i in range(len(path)):
            sizes["/".join(path[: i + 1])] += int(v[0])

print(sum(size for size in sizes.values() if size <= 100000))
print(min(size for size in sizes.values() if size > (30000000 - (70000000 - sizes["/"]))))
