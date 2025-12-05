#!/usr/bin/env python
from functools import reduce

input_file = "test_input"

ranges, _, items = open(input_file).read().strip().partition("\n\n")
ranges = list(sorted(tuple(map(int, line.split("-"))) for line in ranges.splitlines()))
items = list(map(int, items.splitlines()))

print(sum(any(x <= item <= y for x, y in ranges) for item in items))
print(
    reduce(
        lambda res, bounds: (max(res[0], bounds[1]), res[1] + max(0, bounds[1] - max(bounds[0] - 1, res[0]))),
        ranges,
        (-1, 0),
    )[1]
)
