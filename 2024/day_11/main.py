#!/usr/bin/env python
import re
from collections import Counter, defaultdict

input_file = "input"

data = Counter(re.findall(r"\d+", open(input_file).read()))


def solve(stones, iterations):
    for _ in range(iterations):
        new_stones = defaultdict(int)
        for stone, occ in stones.items():
            if stone == "0":
                new_stones["1"] += occ
            elif len(stone) % 2 == 0:
                new_stones[stone[: len(stone) // 2]] += occ
                new_stones[str(int(stone[len(stone) // 2 :]))] += occ
            else:
                new_stones[str(int(stone) * 2024)] += occ

        stones = new_stones
    return stones


print(sum(solve(data, 25).values()))
print(sum(solve(data, 75).values()))
