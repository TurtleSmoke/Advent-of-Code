#!/usr/bin/env python
import re
from itertools import zip_longest

input_file = "input"

operations = list(zip(*[s.split() for s in open(input_file).read().splitlines()]))
operations2 = [
    [x[0][:-1].strip(), *x[1:], x[0][-1]]
    # Ugly, but the list below is "just" the list of columns...
    for x in [
        s.split("|")
        for s in re.split(
            r"\|\s+\|",
            "|".join("".join(c) for c in zip_longest(*[line.rstrip("\n") for line in open(input_file)], fillvalue=" ")),
        )
    ]
]

solve = lambda data: sum(eval(op.join(nums)) for *nums, op in data)

print(solve(operations))
print(solve(operations2))
