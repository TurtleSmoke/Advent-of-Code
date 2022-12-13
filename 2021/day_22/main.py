#!/usr/bin/env python
import re
from collections import Counter

import numpy as np


def solve_part1(f):
    coords = [
        (line[0], *((int(x) + 50) for x in line[1:]))
        for line in re.findall(
            r"(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)", open(f, "r").read()
        )
    ]

    coords = [line for line in coords if all(0 <= x <= 100 for x in line[1:])]
    cube = np.zeros(101 * 101 * 101).reshape((101, 101, 101))

    for (v, x1, x2, y1, y2, z1, z2) in coords:
        sub_cube = np.full((x2 - x1 + 1, y2 - y1 + 1, z2 - z1 + 1), "on" == v)
        cube[x1 : x2 + 1, y1 : y2 + 1, z1 : z2 + 1] = sub_cube

    print(np.sum(cube))


def get_intersection(cube1, cube2):
    x1, x2, y1, y2, z1, z2 = cube1
    x3, x4, y3, y4, z3, z4 = cube2
    ox1 = max(x1, x3)
    ox2 = min(x2, x4)
    oy1 = max(y1, y3)
    oy2 = min(y2, y4)
    oz1 = max(z1, z3)
    oz2 = min(z2, z4)
    if ox1 <= ox2 and oy1 <= oy2 and oz1 <= oz2:
        return ox1, ox2, oy1, oy2, oz1, oz2


def get_area(cube):
    x1, x2, y1, y2, z1, z2 = cube
    return (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)


def solve_part2(f):
    coords = [
        (line[0], *((int(x) + 50) for x in line[1:]))
        for line in re.findall(
            r"(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)", open(f, "r").read()
        )
    ]

    coords = [(1 if line[0] == "on" else -1, *line[1:]) for line in coords]

    cubes = Counter()
    for setting, *cube in coords:
        temp = Counter()
        if setting > 0:
            temp[tuple(cube)] = setting
        for other_cube, other_setting in cubes.items():
            intersection = get_intersection(cube, other_cube)
            if intersection:
                temp[intersection] -= other_setting
        cubes.update(temp)
    print(sum(get_area(cube) * setting for cube, setting in cubes.items()))


solve_part1("input")
solve_part2("input")
