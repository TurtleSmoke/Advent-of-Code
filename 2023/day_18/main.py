#!/usr/bin/env python

input_file = "input"

input_grid = list(line.split() for line in open(input_file).readlines())

directions = {
    "R": (1, 0),
    "L": (-1, 0),
    "D": (0, 1),
    "U": (0, -1),
    "0": (1, 0),
    "1": (0, 1),
    "2": (-1, 0),
    "3": (0, -1),
}


def shoelace(steps):
    x = 0
    res = 1
    for (dx, dy), step in steps:
        x += dx * step
        res += dy * step * x + step / 2

    return int(res)


print(shoelace(((directions[d], int(step)) for d, step, _ in input_grid)))
print(shoelace(((directions[hexa[7]], int(hexa[2:7], 16)) for _, _, hexa in input_grid)))
