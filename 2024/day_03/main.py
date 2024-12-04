#!/usr/bin/env python
import re

input_file = "input"

get_numbers = lambda data: re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data)
res1 = get_numbers(open(input_file).read())
res2 = get_numbers("".join(re.findall(r"do\(\)(?:(?!don't\(\)).)*", 'do()' + open(input_file).read() + "don't()", re.DOTALL)))

print(sum(int(x) * int(y) for x, y in res1))
print(sum(int(x) * int(y) for x, y in res2))

