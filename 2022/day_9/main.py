#!/bin/python3

import numpy as np
from itertools import pairwise

val_input = "input"

moves = np.genfromtxt(val_input, dtype=["U1", int], delimiter=" ")

# Using numpy array to represent the direction
dir_map = {"U": np.array([1, 0]), "D": np.array([-1, 0]), "R": np.array([0, 1]), "L": np.array([0, -1])}
ropes = np.zeros((10, 2), dtype=int)
visited1 = set()
visited2 = set()

for direction, distance in moves:
    for _ in range(distance):
        ropes[0] += dir_map[direction]
        for H, T in pairwise(range(len(ropes))):
            delta = ropes[H] - ropes[T]
            if np.linalg.norm(delta, np.inf) > 1:
                ropes[T] += delta.clip(-1, 1)
        visited1.add(tuple(ropes[1]))
        visited2.add(tuple(ropes[-1]))

print(len(visited1))
print(len(visited2))

# Using imaginary numbers to represent the direction, actually faster
dir_map = {"U": 1j, "D": -1j, "R": 1, "L": -1}
ropes = [0] * 10
visited1 = set()
visited2 = set()

sign = lambda x: (x > 0) - (x < 0)

for direction, distance in moves:
    for _ in range(distance):
        ropes[0] += dir_map[direction]
        for H, T in pairwise(range(len(ropes))):
            delta = ropes[H] - ropes[T]
            if abs(delta) >= 2:
                ropes[T] += sign(delta.real) + 1j * sign(delta.imag)
        visited1.add(ropes[1])
        visited2.add(ropes[-1])

print(len(visited1))
print(len(visited2))
