#!/usr/bin/env python
from collections import defaultdict
from itertools import pairwise

input_file = "input"

data = list(map(int, open(input_file).read().strip().split("\n")))


def next_pseudo_random(x):
    x ^= x << 6 & 0xFFFFFF
    x ^= x >> 5 & 0xFFFFFF
    return x ^ x << 11 & 0xFFFFFF


def solve1(x):
    return max(enumerate(x := next_pseudo_random(x) for _ in range(2000)))[1]


def solve2(xs):
    res = defaultdict(int)
    for x in xs:
        sequence = [x] + [x := next_pseudo_random(x) for _ in range(2000)]
        deltas = [b % 10 - a % 10 for a, b in pairwise(sequence)]

        used = set()
        for i in range(len(sequence) - 4):
            pattern = tuple(deltas[i : i + 4])
            if pattern not in used:
                res[pattern] += sequence[i + 4] % 10
                used.add(pattern)

    return res.values()


print(sum(map(solve1, data)))
print(max(solve2(data)))
