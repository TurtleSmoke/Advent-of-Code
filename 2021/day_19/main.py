#!/usr/bin/env python
from itertools import combinations

import numpy as np


def rotations():
    vectors = [
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    ]
    vectors = list(map(np.array, vectors))
    for vi in vectors:
        for vj in vectors:
            if vi.dot(vj) == 0:
                vk = np.cross(vi, vj)
                yield np.array([vi, vj, vk])


def common_beacon(x, y, common_dist):
    s1, s2 = scanners[x], scanners[y]
    s1_beacon = hashes[x][common_dist][0]
    for r in rotations():
        s2_rotated = s2 @ r
        for s2_beacon in hashes[y][common_dist]:
            diff = s1[s1_beacon] - s2_rotated[s2_beacon]
            s2_in_s1 = set(map(tuple, s2_rotated + diff))
            if len(set(map(tuple, s1)) & s2_in_s1) >= 12:
                return diff, s2_in_s1, r


scanners = [
    np.array(list(tuple(map(int, coords.split(","))) for coords in scanner.splitlines()[1:]))
    for scanner in open("input", "r").read().split("\n\n")
]

hashes = [
    {tuple(sorted(abs(coords[i, :] - coords[j, :]))): (i, j) for i, j in combinations(range(len(coords)), 2)}
    for coords in scanners
]

positions = {0: np.array((0, 0, 0))}
common_beacons = set(map(tuple, scanners[0]))
while len(positions) < len(scanners):
    for i in range(len(scanners)):
        for j in range(len(scanners)):
            if i == j or not (i in positions) ^ (j in positions):
                continue
            elif j in positions:
                i, j = j, i

            s12 = list(set(hashes[i]) & set(hashes[j]))
            if len(s12) < 66:
                continue

            positions[j], new_common_beacons, rot = common_beacon(i, j, s12[0])
            scanners[j] = scanners[j] @ rot + positions[j]
            common_beacons |= new_common_beacons

positions = list(positions.values())
print(len(common_beacons))
print(max(np.abs(x - y).sum() for x, y in combinations(positions, 2)))
