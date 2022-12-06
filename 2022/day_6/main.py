#!/bin/python3

input = 'input'

val = open(input).read().strip()
res1 = next(i + 4 for i in range(len(val) - 4) if len(set(val[i: i + 4])) == 4)
res2 = next(i + 14 for i in range(len(val) - 14) if len(set(val[i: i + 14])) == 14)

print(res1)
print(res2)
