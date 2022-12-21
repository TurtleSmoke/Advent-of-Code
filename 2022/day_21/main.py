#!/usr/bin/env python
from operator import add, mul, truediv, sub

val_input = "test_input"

fun = {"+": add, "-": sub, "*": mul, "/": truediv}

init_values = {k: v.strip().split(" ") for line in open(val_input).read().splitlines() for k, v in [line.split(":")]}
known_init = {k: int(v[0]) for k, v in init_values.items() if v[0].isdigit()}
unknown_init = {k: v for k, v in init_values.items() if k not in known_init}


def solve(unknown, known):
    while "root" not in known:
        for key, value in unknown.items():
            a, op, b = value
            if a in known and b in known:
                known[key] = fun[op](known[a], known[b])
        unknown = {key: value for key, value in unknown.items() if key not in known}
    return known


print(round((solve(unknown_init.copy(), known_init.copy())["root"])))

unknown_init["root"] = [unknown_init["root"][0], "-", unknown_init["root"][2]]
known_init["humn"] = -1j
root = solve(unknown_init.copy(), known_init.copy())["root"]
print(round(root.real / root.imag))
