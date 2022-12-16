#!/usr/bin/env python
import re
from functools import reduce

from shapely import Polygon, difference

val_input = "input"

sensors = [list(map(int, re.findall("-?\d+", line))) for line in open(val_input).read().splitlines()]

beacons = set()
empty = set()
for sx, sy, bx, by in sensors:
    beacons.add((bx, by))
    length = abs(sx - bx) + abs(sy - by) - abs(sy - 2_000_000)
    empty |= set((x, 2_000_000) for x in range(sx - length, sx + length + 1))

print(len(empty - beacons))

limit = 4_000_000
area = Polygon(((0, 0), (0, limit), (limit, limit), (limit, 0)))
zones = (
    Polygon(
        (
            (sx + abs(sx - bx) + abs(sy - by), sy),
            (sx, sy + abs(sx - bx) + abs(sy - by)),
            (sx - abs(sx - bx) - abs(sy - by), sy),
            (sx, sy - abs(sx - bx) - abs(sy - by)),
        )
    )
    for (sx, sy, bx, by) in sensors
)

beacon = reduce(difference, zones, area).centroid
print(int(beacon.x) * 4_000_000 + int(beacon.y))
