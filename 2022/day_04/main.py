#!/usr/bin/env python
input_file = "test_input"

val = [
    [set(range(int(a), int(b) + 1)) for v in lines.split(",") for a, b in [v.split("-")]]
    for lines in open(input_file).read().splitlines()
]

print(sum(a <= b or b <= a for a, b in val))
print(sum(any(a & b) for a, b in val))
