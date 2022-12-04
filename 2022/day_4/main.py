#!/bin/python3

input = 'input'

val = [[set(range(int(a), int(b) + 1)) for v in lines.split(',') for a,b in [v.split('-')]] for lines in open(input).read().splitlines()]
res1 = [len(a.union(b)) in [len(a), len(b)] for a,b in val]
res2 = [len(a.intersection(b)) != 0 for a,b in val]

print(sum(res1))
print(sum(res2))
