#!/bin/python3

file_input = "input"

t = lambda x: (ord(x) % 65 + 27) % 58

val = [(line[: len(line) // 2], line[len(line) // 2 :]) for line in open(file_input).read().splitlines()]
res1 = [set(a).intersection(set(b)) for a, b in val]

val = open(file_input).read().splitlines()
res2 = [set(a).intersection(set(b)).intersection(set(c)) for a, b, c in zip(val[::3], val[1::3], val[2::3])]

print(sum(t(list(x)[0]) for x in res1))
print(sum(t(list(x)[0]) for x in res2))
