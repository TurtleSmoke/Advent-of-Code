#!/usr/bin/env python
from collections import defaultdict

input_file = "test_input"

grid = defaultdict(int, {x + y * 1j: c == "@" for y, line in enumerate(open(input_file)) for x, c in enumerate(line)})
can_be_removed = lambda p: grid[p] and sum(grid[p + d] for d in [1, -1, 1j, -1j, 1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j]) < 4

print(sum(can_be_removed(p) for p in list(grid)))
print(len([p for _ in range(len(grid)) for p in list(grid) if can_be_removed(p) and not grid.__setitem__(p, 0)]))
