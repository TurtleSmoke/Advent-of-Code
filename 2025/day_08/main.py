#!/usr/bin/env python
import math

input_file = "input"

ITERATIONS = 10 if input_file == "test_input" else 1000

boxes = [tuple(map(int, pos.split(","))) for pos in open(input_file).read().strip().splitlines()]
pairs = sorted(
    [
        ((b1[0] - b2[0]) ** 2 + (b1[1] - b2[1]) ** 2 + (b1[2] - b2[2]) ** 2, b1, b2)
        for i, b1 in enumerate(boxes)
        for b2 in boxes[i + 1 :]
    ]
)


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, x, y):
    rx, ry = find(parent, x), find(parent, y)
    if rx != ry:
        parent[rx] = ry
    return rx != ry


def solve1(pairs):
    parents = {b: b for b in boxes}
    for _, b1, b2 in pairs[:ITERATIONS]:
        union(parents, b1, b2)
    circuits = {}
    for b in boxes:
        circuits[find(parents, b)] = circuits.get(find(parents, b), 0) + 1
    return math.prod(sorted(circuits.values(), reverse=True)[:3])


def solve2(pairs):
    parents = {b: b for b in boxes}
    missing_connections = len(boxes) - 1
    for _, b1, b2 in pairs:
        missing_connections -= union(parents, b1, b2)
        if missing_connections == 0:
            return b1[0] * b2[0]


print(solve1(pairs))
print(solve2(pairs))
