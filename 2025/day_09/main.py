#!/usr/bin/env python
from itertools import chain, combinations


input_file = "input"

points = [tuple(map(int, line.split(","))) for line in open(input_file)]

dist = lambda x1, y1, x2, y2: (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

print(sorted(dist(x1, y1, x2, y2) for (x1, y1), (x2, y2) in combinations(points, 2))[-1])

# Works but slow
# from shapely import Polygon, box
# print(
#     max(
#         (
#             dist(x1, y1, x2, y2)
#             for (x1, y1), (x2, y2) in combinations(points, 2)
#             if Polygon(points).covers(box(min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)))
#         )
#     )
# )

print(
    max(
        dist(x1, y1, x2, y2)
        for (x1, y1), (x2, y2) in combinations(points, 2)
        if all(
            max(x3, x4) <= min(x1, x2)
            or max(x1, x2) <= min(x3, x4)
            or max(y3, y4) <= min(y1, y2)
            or max(y1, y2) <= min(y3, y4)
            for (x3, y3), (x4, y4) in zip(points, chain(points[1:], points[:1]))
        )
    )
)
