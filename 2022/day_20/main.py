#!/usr/bin/env python

val_input = "input"

coordinates = [(i, int(v)) for i, v in enumerate(open(val_input).read().splitlines())]


def solve(n, values):
    original = values.copy()
    for _ in range(n):
        for (i, v) in original:
            current = values.index((i, v))
            values.insert((current + v) % (len(values) - 1), values.pop(current))
    idx_zero = next(i for i, v in enumerate(values) if v[1] == 0)
    return sum(values[(idx_zero + offset) % len(values)][1] for offset in (1000, 2000, 3000))


print(solve(1, coordinates.copy()))
print(solve(10, [(i, v * 811589153) for i, v in coordinates]))
