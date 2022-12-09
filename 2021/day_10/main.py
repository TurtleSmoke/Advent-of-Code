#!/usr/bin/env python
from functools import reduce

values = [list(line) for line in open("input", "r").read().splitlines()]

match = {"[": "]", "{": "}", "(": ")", "<": ">"}
val = {")": 3, "]": 57, "}": 1197, ">": 25137}
non_corrupted = []
res = 0


def is_corrupted(current_line):
    stack = []
    for c in current_line:
        if c in match:
            stack.append(c)
        elif stack and c != match[stack.pop()]:
            return True, c

    return False, stack


for line in values:
    corrupted, v = is_corrupted(line)
    if corrupted:
        res += val[v]
    else:
        non_corrupted.append(v)

val2 = {"(": 1, "[": 2, "{": 3, "<": 4}

score = sorted([reduce(lambda a, x: a * 5 + val2[x], reversed(non_corrup), 0) for non_corrup in non_corrupted])

print(res)
print(score[len(score) // 2])
