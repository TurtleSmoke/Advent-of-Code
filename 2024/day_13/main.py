#!/usr/bin/env python
import re
import numpy as np

input_file = "input"

data = [list(map(int, re.findall(r"\d+", chunk))) for chunk in open(input_file).read().split("\n\n")]


def solve(chunk, part2):
    shift = 1e13 if part2 else 0
    for a, b, c, d, x, y in data:
        M = np.array([[a, c], [b, d]])
        P = np.array([x, y]) + shift
        R = np.linalg.solve(M, P).round()

        yield R @ [3, 1] if np.all(M @ R == P) else 0


print(int(sum(solve(data, False))))
print(int(sum(solve(data, True))))
