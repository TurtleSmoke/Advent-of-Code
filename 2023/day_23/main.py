#!/usr/bin/env python
from collections import defaultdict

input_file = "input"

input_grid = {i + j * 1j: c for i, line in enumerate(open(input_file)) for j, c in enumerate(line.strip()) if c != "#"}
input_start = next(iter(input_grid))
input_end = next(reversed(input_grid))
forced_directions = [("v", 1), ("<", -1j), ("^", -1), (">", 1j)]
input_graph_slopes = {
    p: {(p + d, 1) for fd, d in forced_directions if c in (".", fd) and p + d in input_grid}
    for p, c in input_grid.items()
}
input_graph = {p: {p + d for _, d in forced_directions if p + d in input_grid} for p, c in input_grid.items()}


def dfs(graph, start, end):
    queue = [(0, start, {start})]
    res = []
    while queue:
        cost, current, visited = queue.pop()
        if current == end:
            res.append(cost)

        visited.add(current)
        for neighbor, path_cost in graph[current]:
            if neighbor not in visited:
                queue.append((cost + path_cost, neighbor, visited | {current}))

    return max(res)


def edges_contraction(graph, start):
    clusters_stack = [start]
    visited = set()
    clusters_graph = defaultdict(set)

    while clusters_stack:
        current = clusters_stack.pop()
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                next_cluster, segments_size = neighbor, 1
                while next_cluster not in visited and len(graph[next_cluster]) == 2:
                    visited.add(next_cluster)
                    next_cluster = next(n for n in graph[next_cluster] if n not in visited)
                    segments_size += 1

                clusters_stack.append(next_cluster)
                clusters_graph[current].add((next_cluster, segments_size))
                clusters_graph[next_cluster].add((current, segments_size))

    return clusters_graph


input_clusters_graph = edges_contraction(input_graph, input_start)
print(dfs(input_graph_slopes, input_start, input_end))
print(dfs(input_clusters_graph, input_start, input_end))
