#!/usr/bin/env python
import numpy as np
from functools import reduce

input_file = "input"

rotations = [-int(s[1:]) if s[0] == "L" else int(s[1:]) for s in open(input_file).readlines()]

print(np.sum(np.cumsum(rotations) % 100 == 50))
print(
    reduce(
        lambda res, x: (
            (s := (res[0] + x)) % 100,
            res[1] + (res[0] > 0 >= s) + (res[0] < 0 <= s) + abs(s) // 100,
        ),
        rotations,
        (50, 0),
    )[1]
)
