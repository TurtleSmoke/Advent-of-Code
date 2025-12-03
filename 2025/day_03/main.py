#!/usr/bin/env python
from functools import reduce
from itertools import combinations


input_file = "input"

banks = open(input_file).read().splitlines()

print(sum([max(int(a) * 10 + int(b) for a, b in combinations(s, 2)) for s in banks]))
print(
    sum(
        [
            int(
                reduce(
                    lambda acc, i: (acc[0] + s[m := max(range(acc[1], len(s) - 11 + i), key=lambda j: s[j])], m + 1),
                    range(12),
                    ("", 0),
                )[0]
            )
            for s in banks
        ]
    )
)
