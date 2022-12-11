#!/usr/bin/env python
from functools import reduce
import operator
from math import lcm


class Monkey:
    def __init__(self, infos):
        infos = infos.split("\n")
        self.items = list(map(int, infos[1][18:].split(",")))
        self.op = eval(f"lambda old: {infos[2][19:]}")
        self.div = int(infos[3][20:])
        self.throw_to = [int(infos[4][28:]), int(infos[5][29:])]
        self.action = 0


def solve(part1):
    monkeys = list(map(Monkey, open(val_input).read().split("\n\n")))
    prod = lcm(*(monkey.div for monkey in monkeys))
    for i in range(20 if part1 else 10000):
        for monkey in monkeys:
            for item in monkey.items:
                item = monkey.op(item)
                item = item // 3 if part1 else item % prod
                monkeys[monkey.throw_to[bool(item % monkey.div)]].items.append(item)
                monkey.action += 1
            monkey.items = []
    return [monkey.action for monkey in monkeys]


val_input = "input"

print(reduce(operator.mul, sorted(solve(True))[-2:]))
print(reduce(operator.mul, sorted(solve(False))[-2:]))
