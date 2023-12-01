# !/usr/bin/env python
import re

text = "input"

values = open(text).read().split("\n")

mappings = {str(i): i for i in range(10)} | {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

res1 = [re.findall(r"\d", line) for line in values]
res2 = [re.findall(r"(?=(" + "|".join(mappings) + "))", line) for line in values]
get_res = lambda res: sum(mappings[line[0]] * 10 + mappings[line[-1]] for line in res)

print(get_res(res1))
print(get_res(res2))
