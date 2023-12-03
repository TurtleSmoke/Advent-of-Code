#!/usr/bin/env python
import itertools
import re

input_file = "input"

symbols, numbers = {}, []

for i, line in enumerate(open(input_file).read().splitlines()):
    m = re.finditer(r"(\d+)|([^.])", line)
    for match in m:
        if match.group().isdigit():
            numbers.append((int(match.group()), set((i, j) for j in range(*match.span()))))
        else:
            symbols[(i, match.start())] = match.group()

get_neighbors = lambda x, y: {(x + i, y + j) for i, j in itertools.product((-1, 0, 1), repeat=2)}

gears = {coord for coord, symbol in symbols.items() if symbol == "*"}
gears_neighbors = [[n for n, coords in numbers if any(get_neighbors(*gear) & coords)] for gear in gears]

res1 = sum(n for n, coords in numbers if any(get_neighbors(*coord) & symbols.keys() for coord in coords))
res2 = sum(gears_ratio[0] * gears_ratio[1] for gears_ratio in gears_neighbors if len(gears_ratio) == 2)

print(res1)
print(res2)
