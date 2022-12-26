#!/usr/bin/env python
from functools import reduce

input_file = "test_input"

data = open(input_file).read().splitlines()
converted = sum(reduce(lambda x, y: x * 5 + "=-012".index(y) - 2, line, 0) for line in data)

res = ""
while converted != 0:
    converted, rem = divmod(converted + 2, 5)
    res = "=-012"[rem] + res

print(res)
