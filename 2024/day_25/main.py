#!/usr/bin/env python
import itertools

input_file = "input"

data = [
    [
        (
            max(height for height, c in enumerate(row) if c == "#"),
            max(height for height, c in enumerate(row) if c == "."),
        )
        for row in blueprint
    ]
    for blueprint in [zip(*blueprint.split("\n")) for blueprint in open(input_file).read().strip().split("\n\n")]
]

locks = list(filter(None, [[x for x, y in blueprint if y == 6] for blueprint in data]))
keys = list(filter(None, [[y for x, y in blueprint if x == 6] for blueprint in data]))

print(sum(all(hk >= hl for hl, hk in zip(lock, key)) for lock, key in itertools.product(locks, keys)))
