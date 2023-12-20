#!/usr/bin/env python
import operator
import re
from functools import reduce

input_file = "input"

input_workflows, input_ratings = (line for line in open(input_file).read().split("\n\n"))
input_workflows = {
    name: re.findall(r"([xmas])([<>])(\d*):(\w+)", rules) + [("", "", "", rules.split(",")[-1])]
    for workflow in input_workflows.split("\n")
    for name, rules in re.findall(r"([^{]+){([^}]+)}", workflow)
}
input_ratings = [{x: int(val) for x, val in re.findall(r"([xmas])=(\d+)", line)} for line in input_ratings.split("\n")]


def execute_workflow(workflows, rating):
    cur_workflow = "in"
    while cur_workflow not in "AR":
        for c, cond, value, next_workflow in workflows[cur_workflow]:
            if cond == "<" and rating[c] < int(value) or cond == ">" and rating[c] > int(value) or cond == "":
                cur_workflow = next_workflow
                break

    return 0 if cur_workflow == "R" else sum(rating.values())


def execute_workflow_range(workflows, cur_workflow, rating):
    if cur_workflow == "A":
        return reduce(operator.mul, (b - a + 1 for a, b in rating.values()))

    if cur_workflow == "R":
        return 0

    res = 0
    for c, cond, value, next_workflow in workflows[cur_workflow]:
        if cond == "":
            res += execute_workflow_range(workflows, next_workflow, rating)
            continue

        low, high, value = rating[c][0], rating[c][1], int(value)
        if cond == "<" and low < value:
            res += execute_workflow_range(workflows, next_workflow, {**rating, c: (low, value - 1)})
            rating = {**rating, c: (value, high)}
        elif cond == ">" and high > value:
            res += execute_workflow_range(workflows, next_workflow, {**rating, c: (value + 1, high)})
            rating = {**rating, c: (low, value)}

    return res


print(sum(execute_workflow(input_workflows, rating) for rating in input_ratings))
print(execute_workflow_range(input_workflows, "in", {c: (1, 4000) for c in "xmas"}))
