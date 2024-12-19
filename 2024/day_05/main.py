#!/usr/bin/env python
from collections import defaultdict

input_file = "input"

rules, updates = open(input_file).read().strip().split("\n\n")
rules = set(tuple(map(int, line.split("|"))) for line in rules.split("\n"))
updates = [tuple(map(int, line.split(","))) for line in updates.split("\n")]

incorrect_update = lambda update: any((y, x) in rules for i, x in enumerate(update) for y in update[i + 1 :])

res1 = sum(update[len(update) // 2] for update in updates if not incorrect_update(update))

graph = defaultdict(set)
for src, dst in rules:
    graph[src].add(dst)

res2 = 0
for update in updates:
    if incorrect_update(update):
        rule = set(update)
        valid_update = {page: graph[page] & rule for page in update}
        valid_update = sorted(valid_update, key=lambda j: len(valid_update[j]), reverse=True)
        res2 += int(valid_update[len(valid_update) // 2])

print(res1)
print(res2)
