#!/bin/python3

val_input = "input"

t = lambda x: ord(x) % 65 % 23
val = [tuple(t(x) for x in lines.split(" ")) for lines in open(val_input).read().splitlines()]
res1 = [(b + 1 + (b - a + 1) % 3 * 3) for a, b in val]

t = lambda x: ord(x) % 65 % 23
val = [tuple(t(x) for x in lines.split(" ")) for lines in open(val_input).read().splitlines()]
res2 = [(b * 3 + (b + a - 1) % 3 + 1) for a, b in val]

print(sum(res1))
print(sum(res2))
