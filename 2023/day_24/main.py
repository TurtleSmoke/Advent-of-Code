#!/usr/bin/env python
import itertools
import re
import z3

input_file = "input"

input_hailstones = [list(map(int, re.findall(r"-?\d+", line))) for line in open(input_file).readlines()]


def count_intersected_path(hailstones, min_xy, max_xy):
    intersections = 0
    dot = lambda a, b: a[0] * b[1] - a[1] * b[0]
    for (x1, y1, _, dx1, dy1, _), (x2, y2, _, dx2, dy2, _) in itertools.combinations(hailstones, 2):
        c = dot((dy1, dy2), (dx1, dx2))
        if abs(c) < 1e-6:
            continue

        x3 = dot((x1, y1), (x1 + dx1, y1 + dy1))
        x4 = dot((x2, y2), (x2 + dx2, y2 + dy2))
        x = dot((x3, x4), (dx1, dx2)) / c
        y = dot((x3, x4), (dy1, dy2)) / c
        tx = (x - x1) / dx1
        ty = (x - x2) / dx2

        if tx >= 0 and ty >= 0 and min_xy <= x <= max_xy and min_xy <= y <= max_xy:
            intersections += 1

    return intersections


def intersect_all(hailstones):
    x, y, z, dx, dy, dz, t0, t1, t2 = z3.Reals("x y z dx dy dz t0 t1 t2")

    x0, y0, z0, dx0, dy0, dz0 = hailstones[0]
    x1, y1, z1, dx1, dy1, dz1 = hailstones[1]
    x2, y2, z2, dx2, dy2, dz2 = hailstones[2]

    equations = [
        x + t0 * dx == x0 + t0 * dx0,
        y + t0 * dy == y0 + t0 * dy0,
        z + t0 * dz == z0 + t0 * dz0,
        x + t1 * dx == x1 + t1 * dx1,
        y + t1 * dy == y1 + t1 * dy1,
        z + t1 * dz == z1 + t1 * dz1,
        x + t2 * dx == x2 + t2 * dx2,
        y + t2 * dy == y2 + t2 * dy2,
        z + t2 * dz == z2 + t2 * dz2,
    ]

    s = z3.Solver()
    s.add(equations)
    s.check()
    r = s.model()
    return sum(r[x].as_long() for x in [x, y, z])


print(count_intersected_path(input_hailstones, 200000000000000, 400000000000000))
print(intersect_all(input_hailstones))
