#!/usr/bin/env python
import itertools

import numpy as np

values = np.array([[int(x) for x in line] for line in open("input", "r").read().splitlines()])

lx = len(values)
ly = len(values[0])
res = 0
for _ in range(100):
    stack = []
    for x in range(lx):
        for y in range(ly):
            values[x][y] += 1
            if values[x][y] > 9:
                values[x][y] = 0
                stack.append((x, y))

    while stack:
        x, y = stack.pop()
        for i, j in [(1, 1), (1, 0), (1, -1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]:
            cx, cy = x + i, y + j
            if 0 <= cx < lx and 0 <= cy < ly and values[cx][cy] != 0:
                values[cx][cy] = (values[cx][cy] + 1) % 10
                if values[cx][cy] == 0:
                    stack.append((cx, cy))

    res += np.sum(values == 0)

print(res)

values = np.array([[int(x) for x in line] for line in open("input", "r").read().splitlines()])

for r in itertools.count(0):
    if np.sum(values == 0) == np.size(values):
        print(r)
        break
    values += 1

    stack = []
    for x in range(lx):
        for y in range(ly):
            if values[x][y] > 9:
                values[x][y] = 0
                stack.append((x, y))

    while stack:
        x, y = stack.pop()
        for i, j in [(1, 1), (1, 0), (1, -1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]:
            cx, cy = x + i, y + j
            if 0 <= cx < lx and 0 <= cy < ly and values[cx][cy] != 0:
                values[cx][cy] = (values[cx][cy] + 1) % 10
                if values[cx][cy] == 0:
                    stack.append((cx, cy))

    res += np.sum(values == 0)
