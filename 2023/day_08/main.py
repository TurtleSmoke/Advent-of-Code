#!/usr/bin/env python
import itertools
import math
import re
from sympy.ntheory.modular import crt

input_file = "input"

input_directions, input_graph = open(input_file).read().split("\n\n")
input_directions = [dir == "R" for dir in input_directions]
input_nodes = {
    src: (left, right) for nodes in input_graph.split("\n") for src, left, right in [re.findall(r"[A-Z0-9]{3}", nodes)]
}


def walk_graph(nodes, directions):
    current = "AAA"
    for num_steps, direction in enumerate(itertools.cycle(directions)):
        if current == "ZZZ":
            return num_steps
        current = nodes[current][direction]


# Proper solution, without following assumptions:
# - Cycle contains only one ending state
# - Path length to ending node from start is equal to cycle length
def walk_ghost_graph(nodes, directions):
    sources = [node for node in nodes if node[-1] == "A"]
    all_start_to_end_length = {node: {} for node in sources}
    loop_length = {node: 0 for node in sources}
    for src in sources:
        current = src
        for num_steps, direction in enumerate(itertools.cycle(directions)):
            state = (current, direction)
            if state in all_start_to_end_length[src]:
                loop_length[src] = num_steps - all_start_to_end_length[src][state]
                break

            if current[-1] == "Z":
                all_start_to_end_length[src][state] = num_steps

            current = nodes[current][direction]

    # Costly operation because all combinations must be computed... Surely there is a better way
    moduli = loop_length.values()
    remainders = [v.values() for v in all_start_to_end_length.values()]
    remainders_combinations = list(itertools.product(*remainders))

    crt_solutions = [crt(moduli, remainder) for remainder in remainders_combinations]
    res = [r[0] for r in crt_solutions if r is not None]
    if res == []:
        return None

    res = min(res)
    # By definition, if a solution exists it will be unique modulo the LCM of all moduli, thus:
    # - If min(res) != 0, its the solution by definition
    # - If res == 0, the solution is the LCM of all moduli.
    return res if res != 0 else math.lcm(*moduli)


print(walk_graph(input_nodes, input_directions))
print(walk_ghost_graph(input_nodes, input_directions))
