#!/usr/bin/env python
import re

import numpy as np

input_file = "input"

games = [
    len(set(winning.split()) & set(numbers.split()))
    for winning, numbers in re.findall(r": ([\d ]+) \| ([\d ]+)", open(input_file).read())
]

res1 = sum(2 ** (wins - 1) for wins in games if wins > 0)

res2 = np.array([1] * len(games))
for i, win in enumerate(games):
    res2[i + 1 : i + win + 1] += res2[i]

print(res1)
print(sum(res2))
