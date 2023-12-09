#!/usr/bin/env python
import re
from math import prod
from cpmpy import Model, cpm_array, intvar

input_file = "input"

blueprints = [tuple(map(int, re.findall(r"\d+", line)))[1:] for line in open(input_file).read().splitlines()]


def cp(step, available_blueprints):
    res = []
    for i in range(available_blueprints):
        a, b, c, d, e, f = blueprints[i]
        cost = cpm_array(
            [
                [a, 0, 0, 0],
                [b, 0, 0, 0],
                [c, d, 0, 0],
                [e, 0, f, 0],
                [0, 0, 0, 0],
            ]
        )

        model = Model()

        bots = intvar(0, 100, shape=(4, step + 1))
        resources = intvar(0, 100, shape=(4, step + 1))
        construct = intvar(0, 4, shape=step + 1)

        for r in range(4):
            model += bots[r, 0] == (1 if r == 0 else 0)
            model += resources[r, 0] == 0
            model += construct[0] == 4

            for s in range(1, step + 1):
                model += resources[r, s] == resources[r, s - 1] + bots[r, s - 1] - cost[construct[s], r]
                model += bots[r, s] == bots[r, s - 1] + (construct[s] == r)
                model += resources[r, s - 1] >= cost[construct[s], r]

        model.maximize(resources[3, step])
        model.solve()
        res.append(((i + 1), resources[3, step].value()))
    return res


print(sum(i * v for i, v in cp(24, len(blueprints))))
print(prod((v for _, v in cp(32, 3))))
