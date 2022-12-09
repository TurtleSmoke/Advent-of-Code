#!/usr/bin/env python
import operator
from functools import reduce

values = [[int(x) for x in line] for line in open("input", "r").read().splitlines()]

min_val = 0
lx = len(values)
ly = len(values[0])
for x in range(lx):
    for y in range(ly):
        m = values[x][y]
        if not any(
            0 <= x + i < lx and 0 <= y + j < ly and values[x + i][y + j] <= m
            for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ):
            min_val += m + 1

print(min_val)

values = [[[int(x), False] for x in line] for line in open("input", "r").read().splitlines()]

low_point = []
lx = len(values)
ly = len(values[0])
for x in range(lx):
    for y in range(ly):
        m = values[x][y]
        if not any(
            0 <= x + i < lx and 0 <= y + j < ly and values[x + i][y + j] <= m
            for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ):
            low_point.append((x, y))

bassin = []
print(low_point)
for cell in low_point:
    current_bassin = [cell]
    values[cell[0]][cell[1]][1] = True
    size = 0

    while current_bassin:
        x, y = current_bassin.pop(0)

        size += 1

        for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= x + i < lx and 0 <= y + j < ly and values[x + i][y + j][0] < 9 and not values[x + i][y + j][1]:
                values[x + i][y + j][1] = True
                current_bassin.append((x + i, y + j))

    bassin.append(size)

print(reduce(operator.mul, sorted(bassin)[-3:]))
