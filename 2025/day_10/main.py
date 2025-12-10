#!/usr/bin/env python
import re
from functools import reduce
from itertools import combinations
from operator import xor
from scipy.optimize import linprog

input_file = "input"

machines = [
    (
        int((re.search(r"\[(.*)]", line)[1].replace(".", "0").replace("#", "1"))[::-1], 2),
        [sum(1 << x for x in (map(int, s.split(",")))) for s in re.findall(r"\(([^)]*)\)", line)],
        list(map(int, re.search(r"{(.*)}", line)[1].split(","))),
    )
    for line in open(input_file).read().splitlines()
]

print(
    sum(
        next(i for i in range(1, len(buttons)) for x in combinations(buttons, i) if reduce(xor, x, 0) == diagram)
        for diagram, buttons, _ in machines
    )
)


print(
    sum(
        int(
            linprog(
                [1] * len(buttons),
                A_eq=[[(buttons[j] >> i) & 1 for j in range(len(buttons))] for i in range(len(joltage))],
                b_eq=joltage,
                integrality=True,
            ).fun
        )
        for _, buttons, joltage in machines
    )
)
