#!/usr/bin/env python
from copy import deepcopy

input_file = "input"

crates, moves = open(input_file).read().split("\n\n")
crates = [list("".join(x[:-1]).strip()) for x in zip(*crates.splitlines())][1::4]
moves = [list(map(int, x.split(" ")[1::2])) for x in moves.splitlines()]

res1, res2 = deepcopy(crates), deepcopy(crates)

for n, fro, to in moves:
    res1[to - 1][:0] = res1[fro - 1][:n][::-1]
    res2[to - 1][:0] = res2[fro - 1][:n]
    del res1[fro - 1][:n]
    del res2[fro - 1][:n]

print("".join(x[0] for x in res1))
print("".join(x[0] for x in res2))
