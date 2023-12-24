#!/usr/bin/env python

input_file = "input"

input_grid = {i + j * 1j: c for i, line in enumerate(open(input_file)) for j, c in enumerate(line.strip()) if c != "#"}
input_graph_slopes = {
    p: {
        p + d for fd, d in [("v", 1), ("<", -1j), ("^", -1), (">", 1j)] if (c == "." or fd == c) and p + d in input_grid
    }
    for p, c in input_grid.items()
}
input_graph = {
    p: {
        p + d for _, d in [("v", 1), ("<", -1j), ("^", -1), (">", 1j)] if p + d in input_grid
    }
    for p, c in input_grid.items()
}


def dijkstra(graph, start, end):
    queue = [(0, start, {start})]
    res = []
    while queue:
        cost, current, visited = queue.pop()
        if current == end:
            res.append(cost)

        visited.add(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append((cost + 1, neighbor, visited | {current}))

    return max(res)


def edges_contraction(graph):



print(dijkstra(input_graph_slopes, next(iter(input_graph_slopes)), next(reversed(input_graph_slopes))))
print(dijkstra(input_graph, next(iter(input_graph_slopes)), next(reversed(input_graph_slopes))))
