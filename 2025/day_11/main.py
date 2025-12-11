#!/usr/bin/env python
import functools
import re
from itertools import permutations

input_file = "input"

devices = {src: dst for line in open(input_file) for src, *dst in [re.findall(r"\w+", line)]}


# Without the '@cache', which makes things much easier...
# def dfs(current, end):
#     cache = {}
#
#     def dfs(current, end):
#         if current not in cache:
#             cache[current] = 1 if current == end else sum(dfs(neighbor, end) for neighbor in devices.get(current, []))
#         return cache[current]
#
#     return dfs(current, end)


@functools.cache
def dfs(curr, end):
    return 1 if curr == end else sum(dfs(n, end) for n in devices.get(curr, []))


print(dfs("you", "out"))
print(sum(dfs("svr", a) * dfs(a, b) * dfs(b, "out") for a, b in permutations(["dac", "fft"])))
