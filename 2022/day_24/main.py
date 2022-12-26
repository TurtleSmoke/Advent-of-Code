#!/usr/bin/env python
from itertools import count

input_file = "input"

data = open(input_file).read().splitlines()
max_h, max_w = len(data) - 2, len(data[0]) - 2
dirs = {"<": -1, ">": 1, "^": -1j, "v": 1j, "X": 0}
init_blizzards = {(complex(x - 1, y - 1), dirs[c]) for y, l in enumerate(data) for x, c in enumerate(l) if c in "<>^v"}
walls = {complex(x - 1, y - 1) for y, l in enumerate(data) for x, c in enumerate(l) if c == "#"}
walls |= {complex(0, -2), complex(max_w - 1, max_h + 1)}

start, end = complex(0, -1), complex(max_w - 1, max_h)
positions = {start}
goals = [end, start, end]
for i in count(0):
    blizzards = {complex((p.real + i * d.real) % max_w, (p.imag + i * d.imag) % max_h) for p, d in init_blizzards}
    positions = {p + d for p in positions for d in dirs.values()} - walls - blizzards
    if goals[0] in positions:
        print(i)
        if len(goals) == 1:
            break
        positions = {goals.pop(0)}
