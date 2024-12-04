#!/usr/bin/env python
from collections import defaultdict

input_file = "input"

data = defaultdict(
    str,
    {x + 1j * y: c for y, r in enumerate(open(input_file)) for x, c in enumerate(r.strip())},
)

res1 = 0
res2 = 0

for c in data.copy():
    for d in [1, 1j, 1 + 1j, 1 - 1j, -1, -1j, -1 + 1j, -1 - 1j]:
        res1 += data[c] + data[c + d] + data[c + d * 2] + data[c + d * 3] == "XMAS"
        if d.imag and d.real:
            res2 += data[c + d] + data[c] + data[c - d] == "MAS" and data[c + d * 1j] + data[c - d * 1j] == "MS"

print(res1)
print(res2)
