#!/usr/bin/env python
from functools import reduce

val_input = "test_input"

data = open(val_input).read().splitlines()
converted = sum(reduce(lambda x, y: x * 5 + "=-012".index(y) - 2, line, 0) for line in data)
res = ""
while converted != 0:
    converted, rem = divmod(converted + 2, 5)
    res += "=-012"[rem]

print(res[::-1])
