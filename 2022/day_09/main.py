#!/usr/bin/env python

from itertools import pairwise
import numpy as np

input_file = "input"

moves = np.genfromtxt(input_file, dtype=["U1", int], delimiter=" ")

dirs = {"U": 1j, "D": -1j, "R": 1, "L": -1}
ropes = [0] * 10
visited1 = set()
visited2 = set()

sign = lambda x: (x > 0) - (x < 0)

for direction, distance in moves:
    for _ in range(distance):
        ropes[0] += dirs[direction]
        for head, tail in pairwise(range(len(ropes))):
            delta = ropes[head] - ropes[tail]
            if abs(delta) >= 2:
                ropes[tail] += complex(sign(delta.real), sign(delta.imag))
        visited1.add(ropes[1])
        visited2.add(ropes[-1])

print(len(visited1))
print(len(visited2))
