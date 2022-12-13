#!/usr/bin/env python
import itertools
import math
from functools import reduce


def magnitude(x):
    if isinstance(x, int):
        return x

    return 3 * magnitude(x[0]) + 2 * magnitude(x[1])


def add_left(x, n):
    if n is None:
        return x

    if isinstance(x, int):
        return x + n

    return [add_left(x[0], n), x[1]]


def add_right(x, n):
    if n is None:
        return x

    if isinstance(x, int):
        return x + n

    return [x[0], add_right(x[1], n)]


def explode(x, n=4):
    if isinstance(x, int):
        return False, None, x, None

    old_left, old_right = x
    if n == 0:
        return True, old_left, 0, old_right

    has_explode, left, new_left, right = explode(old_left, n - 1)
    if has_explode:
        return True, left, [new_left, add_left(old_right, right)], None

    has_explode, left, new_right, right = explode(old_right, n - 1)
    if has_explode:
        return True, None, [add_right(new_left, left), new_right], right

    return False, None, x, None


def split(x):
    if isinstance(x, int):
        if x >= 10:
            return True, [x // 2, math.ceil(x / 2)]
        return False, x

    a, b = x
    change, a = split(a)
    if change:
        return True, [a, b]

    change, b = split(b)
    return change, [a, b]


def add(a, b):
    x = [a, b]
    while True:
        change, _, x, _ = explode(x)
        if change:
            continue

        change, x = split(x)
        if not change:
            break
    return x


lines = list(map(eval, open("input", "r").read().splitlines()))
print("Part 1:", magnitude(reduce(add, lines)))
print(
    "Part 2:",
    max(magnitude(add(a, b)) for a, b in itertools.permutations(lines, 2)),
)
