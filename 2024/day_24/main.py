#!/usr/bin/env python
import re
from collections import defaultdict
import networkx as nx

input_file = "input"

variables, operations = open(input_file).read().split("\n\n")
variables = defaultdict(int, {v: int(x) for v, x in [s.split(":") for s in variables.split("\n")]})
operations = re.findall(r"(\w+) ([A-Z]+) (\w+) -> (\w+)", operations)
dependencies = {v: (x, y, op) for x, op, y, v in operations}
logical_gate = {
    "AND": lambda x, y: x & y,
    "OR": lambda x, y: x | y,
    "XOR": lambda x, y: x ^ y,
}

graph = nx.DiGraph({dst: [src1, src2] for dst, (src1, src2, _) in dependencies.items()})
topological_order = list(nx.topological_sort(graph))[::-1]
for node in topological_order:
    if node in dependencies:
        src1, src2, op = dependencies[node]
        variables[node] = logical_gate[op](variables[src1], variables[src2])


# Largely inspired by https://www.reddit.com/r/adventofcode/comments/1hl698z/comment/m3kt1je
op_per_var = defaultdict(set)
for var1, op, var2, _ in operations:
    op_per_var[var1].add(op)
    op_per_var[var2].add(op)

wrong = set()
for var1, op, var2, res in operations:
    if res.startswith("z") and op != "XOR":
        wrong.add(res)
    elif op == "XOR" and all(x[0] not in ("x", "y", "z") for x in (res[0], var1[0], var2[0])):
        wrong.add(res)
    elif op != "OR":
        if (op == "AND") == ("OR" not in op_per_var[res]):
            wrong.add(res)


print(int("".join(str(v) for _, v in sorted(filter(lambda x: x[0].startswith("z"), variables.items())))[::-1], 2))
print(",".join(sorted(wrong - {next(out for var1, op, var2, out in operations if "x00" in (var1, var2)), "z45"})))
