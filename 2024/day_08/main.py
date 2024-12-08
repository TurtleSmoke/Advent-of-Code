#!/usr/bin/env python
import itertools

intput_file = "input"

data = {x + 1j * y: c for y, row in enumerate(open(intput_file)) for x, c in enumerate(row.strip())}

antennas_pos = [
    [pos for pos in data.keys() if data[pos] == antenna_type] for antenna_type in set(data.values()) - set(".")
]

res = lambda echos: len(
    set(
        x + d * (x - y)
        for d in echos
        for antenna_pos in antennas_pos
        for x, y in list(itertools.permutations(antenna_pos, 2))
        if x + d * (x - y) in data
    )
)

print(res([1]))
print(res(range(50)))
