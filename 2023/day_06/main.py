#!/usr/bin/env python

import re
from math import floor, ceil, prod

input_file = "input"

data = [re.findall(r"\d+", line) for line in open(input_file).read().splitlines()]
print(list(zip(*((map(int, line)) for line in data))))
races1 = list(zip(*((map(int, line)) for line in data)))
race2 = tuple(int("".join(line)) for line in data)


def find_ways_record(time, distance):
    delta = time**2 - 4 * distance
    low = floor((time - delta**0.5) / 2 + 1)
    high = ceil((time + delta**0.5) / 2 - 1)
    return high - low + 1


print(prod(find_ways_record(*race) for race in races1))
print(find_ways_record(*race2))
