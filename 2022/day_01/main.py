#!/usr/bin/env python
input_file = "input"

data = [sum(map(int, lines.split("\n"))) for lines in open(input_file).read().strip().split("\n\n")]

print(max(data))
print(sorted(data)[-3:])
