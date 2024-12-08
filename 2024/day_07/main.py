#!/usr/bin/env python
import re

input_file = "input"

data = [list(map(int, re.findall(r"\d+", line))) for line in open(input_file).readlines()]


def dfs(numbers, part2):
    if len(numbers) == 1:
        yield numbers[0]
        return

    for res in dfs(numbers[:-1], part2):
        yield numbers[-1] * res
        yield numbers[-1] + res
        if part2:
            yield int(str(res) + str(numbers[-1]))


res1 = sum(numbers[0] for numbers in data if any(numbers[0] == res for res in dfs(numbers[1:], False)))
res2 = sum(numbers[0] for numbers in data if any(numbers[0] == res for res in dfs(numbers[1:], True)))

print(res1)
print(res2)
