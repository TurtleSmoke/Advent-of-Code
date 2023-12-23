#!/usr/bin/env python

input_file = "input"

input_grid = {(y, x): c for y, line in enumerate(open(input_file)) for x, c in enumerate(line.strip()) if c != "#"}
input_size = int(next(reversed(input_grid))[0] + 1)


def walking(sparse, size, remainder):
    modp = lambda x: (x[0] % size, x[1] % size)
    addp = lambda x, y: ((x[0] + y[0]), (x[1] + y[1]))

    visited = {next(k for k, v in sparse.items() if v == "S")}
    new = visited.copy()
    cache = {-1: 0, 0: 1}

    new_dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for i in range(1, 2 * size + remainder + 1):
        visited, new = new, {
            new_pos
            for pos in new
            for direction in new_dirs
            for new_pos in [addp(pos, direction)]
            if new_pos not in visited and modp(new_pos) in sparse
        }
        cache[i] = len(new) + cache[i - 2]

    return cache


steps = 26501365
n, r = steps // input_size, steps % input_size
reachable_plots = walking(input_grid, input_size, r)

a = reachable_plots[r]
b = reachable_plots[input_size + r]
c = reachable_plots[input_size * 2 + r]

print(reachable_plots[64])
print(a + n * (b - a + (n - 1) * (c - b - b + a) // 2))

# 632257949158206
