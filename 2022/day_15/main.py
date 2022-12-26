#!/usr/bin/env python
import re
from functools import reduce

from shapely import Polygon, difference

input_file = "input"

data = [list(map(int, re.findall(r"-?\d+", line))) for line in open(input_file).read().splitlines()]

beacons = {complex(*sensor[2:]) for sensor in data}
sensors_cannot_radius = {complex(sx, sy): abs(sx - bx) + abs(sy - by) - abs(sy - 2_000_000) for sx, sy, bx, by in data}
cannot = {
    complex(x, 2_000_000) for s, d in sensors_cannot_radius.items() for x in range(int(s.real - d), int(s.real + d + 1))
}
print(len(cannot - beacons))

# Assuming that the positions the beacon can not be is a continuous line, just search for the left and right limit of
# the line, remove beacons that are already present on the line, and add 1 because limit are included.
print(
    int(
        max(s.real + d for s, d in sensors_cannot_radius.items())
        - min(s.real - d for s, d in sensors_cannot_radius.items())
        - sum(b.imag == 2_000_000 for b in beacons)
        + 1
    )
)

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
    for (sx, sy, bx, by) in data
)

beacon = reduce(difference, zones, area).centroid
print(int(beacon.x) * 4_000_000 + int(beacon.y))
