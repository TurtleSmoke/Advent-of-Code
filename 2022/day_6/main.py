#!/usr/bin/env python
input_file = "input"

val = open(input_file).read().strip()

print(next(i + 4 for i in range(len(val)) if len(set(val[i : i + 4])) == 4))
print(next(i + 14 for i in range(len(val)) if len(set(val[i : i + 14])) == 14))
