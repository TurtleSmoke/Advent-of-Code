#!/usr/bin/env python

input_file = "input"

graph = {x + 1j * y: c for x, row in enumerate(open(input_file)) for y, c in enumerate(row)}
start = next(k for k, v in graph.items() if v == "^")


def walk(graph, start, part2):
    pos = start
    dir = -1
    visited = set()
    while pos + dir in graph and (pos, dir) not in visited:
        visited.add((pos, dir))
        while graph[pos + dir] == "#":
            dir *= -1j
        pos += dir

    if part2:
        return (pos, dir) in visited
    else:
        visited.add((pos, dir))
        return {pos for pos, _ in visited}


path = walk(graph, start, False)
print(len(path))
print(sum(walk(graph | {o: "#"}, start, True) for o in path))
