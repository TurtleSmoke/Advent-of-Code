#!/usr/bin/env python
from collections import defaultdict
from itertools import accumulate

input_file = "input"

val = list(map(str.split, open(input_file).read().splitlines()))
dirs = defaultdict(int)
path = []

for v in val:
    if v[0] == "$":
        if v[1] == "cd":
            path.pop() if v[2] == ".." else path.append(v[2])
    elif v[0] != "dir":
        for p in accumulate(path, lambda x, y: x + "/" + y):
            dirs[p] += int(v[0])

print(sum(size for size in dirs.values() if size <= 100_000))
print(min(size for size in dirs.values() if size > dirs["/"] - 40_000_000))
