#!/bin/python3

val_input = "input"

val = [sum(int(line.strip()) for line in lines.strip().split("\n")) for lines in open(val_input).read().split("\n\n")]

res1 = max(val)
res2 = sorted(val)[-3:]

print(res1)
print(sum(res2))
