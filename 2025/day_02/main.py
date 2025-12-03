#!/usr/bin/env python

input_file = "input"

ranges = [tuple(map(int, r.split("-"))) for r in open(input_file).read().split(",")]

print(
    sum(
        int(v)
        for start, end in ranges
        for v in map(str, range(start, end + 1))
        if (size := len(v) // 2) and len(v) % 2 == 0 and v[:size] == v[size:]
    )
)

print(
    sum(
        int(s)
        for start, end in ranges
        for s in map(str, range(start, end + 1))
        if any(len(s) % l == 0 and s == s[:l] * (len(s) // l) for l in range(1, len(s) // 2 + 1))
    )
)
