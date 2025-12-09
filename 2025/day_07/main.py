#!/usr/bin/env python
from functools import reduce

input_file = "input"

grid = [[c for c in line.strip()] for line in open(input_file)]

res1, res2 = reduce(
    lambda s, i: (
        s[0] + sum(1 for j in range(len(grid[0])) if s[1][j] and grid[i + 1][j] == "^"),
        [
            (s[1][j] if grid[i + 1][j] != "^" else 0)
            + (s[1][j - 1] if j > 0 and grid[i + 1][j - 1] == "^" else 0)
            + (s[1][j + 1] if j < len(grid[0]) - 1 and grid[i + 1][j + 1] == "^" else 0)
            for j in range(len(grid[0]))
        ],
    ),
    range(len(grid) - 1),
    (0, [int(j == grid[0].index("S")) for j in range(len(grid[0]))]),
)

print(res1)
print(sum(res2))
