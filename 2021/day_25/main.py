#!/usr/bin/env python
from itertools import count
import numpy as np


def move(grid, c, f, moved):
    moved_grid = np.copy(grid)
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            x_, y_ = f(x, y)
            if grid[x, y] == c and grid[x_, y_] == ".":
                moved_grid[x, y] = "."
                moved_grid[x_, y_] = c
                moved = True

    return moved_grid, moved


data = np.array([list(line) for line in open("input", "r").read().splitlines()])

X = len(data)
Y = len(data[0])
for step in count(1):
    data, has_moved = move(data, ">", lambda x, y: (x, (y + 1) % Y), False)
    data, has_moved = move(data, "v", lambda x, y: ((x + 1) % X, y), has_moved)
    print(step)
    if not has_moved:
        print(step)
        break
