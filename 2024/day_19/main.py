#!/usr/bin/env python
from functools import lru_cache

input_file = "input"

patterns, _, *objectives = open(input_file).read().strip().split("\n")
patterns = patterns.split(", ")


@lru_cache()
def dfs(objective):
    return objective == "" or sum(dfs(objective.removeprefix(p)) for p in patterns if objective.startswith(p))


res = [dfs(objective) for objective in objectives]
print(len(res))
print(sum(res))
