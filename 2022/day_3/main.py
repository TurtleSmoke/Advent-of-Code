#!/usr/bin/env python
input_file = "input"

val = open(input_file).read().splitlines()

res1 = [set(line[: len(line) // 2]) & set(line[len(line) // 2 :]) for line in val]
res2 = [set(a) & set(b) & set(c) for a, b, c in zip(val[::3], val[1::3], val[2::3])]

print(sum((ord(max(x)) - 96) % 58 for x in res1))
print(sum((ord(max(x)) - 96) % 58 for x in res2))
