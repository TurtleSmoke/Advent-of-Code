#!/usr/bin/env python
import itertools


input_file = "input"

data = open(input_file).read().strip().split("\n")

directional_keypad = {c: (x, y) for y, row in enumerate([" ^A", "<v>"]) for x, c in enumerate(row)}
numeric_keypad = {c: (x, y) for y, row in enumerate(["789", "456", "123", " 0A"]) for x, c in enumerate(row)}


def solve(code, robots):
    keypad = directional_keypad
    shortest_path = lambda p: sum(dp[(i, j)] for i, j in itertools.pairwise(p))
    dp = {(i, j): 1 for i in keypad for j in keypad}
    for layer in range(1, robots + 1):
        new_dp = {}
        if layer == robots:
            keypad = numeric_keypad
        for ki, (xi, yi) in keypad.items():
            for kj, (xj, yj) in keypad.items():
                path = "A" + (">" if xj > xi else "<") * abs(xj - xi) + ("^" if yj < yi else "v") * abs(yj - yi) + "A"

                new_dp[(ki, kj)] = min(
                    shortest_path(path) if (xj, yi) != keypad[" "] else float("inf"),
                    shortest_path(path[::-1]) if (xi, yj) != keypad[" "] else float("inf"),
                )
        dp = new_dp

    return shortest_path("A" + code)


print(sum(solve(code, 3) * int(code[:-1]) for code in data))
print(sum(solve(code, 26) * int(code[:-1]) for code in data))
