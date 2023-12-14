#!/usr/bin/env python

import numpy as np

input_file = "input"

input_grid = np.array([list(line.strip()) for line in open(input_file).readlines()])


def slide_north(grid):
    for j in range(len(grid[0])):
        empty_space = 0
        for i in range(len(grid)):
            if grid[i, j] == "#":
                empty_space = i + 1
            elif grid[i, j] == "O":
                grid[i, j], grid[empty_space, j] = grid[empty_space, j], grid[i, j]
                empty_space += 1

    return grid


def spin_cycle(grid):
    for _ in range(4):
        grid = slide_north(grid)
        grid = np.rot90(grid, -1)

    return grid


def spin_cycles(grid, n):
    cache = {}
    for i in range(n):
        grid_hash = grid.tobytes()

        if grid_hash in cache:
            cycle_start = cache[grid_hash]
            cycle_len = i - cycle_start
            for _ in range((n - cycle_start) % cycle_len):
                for _ in range(4):
                    grid = slide_north(grid)
                    grid = np.rot90(grid, -1)
            break

        cache[grid_hash] = i
        grid = spin_cycle(grid)

    return grid


total_load = lambda grid: np.sum(np.where(np.rot90(grid, 2) == "O")[0] + 1)
print(total_load(slide_north(input_grid)))
print(total_load(spin_cycles(input_grid, 1_000_000_000)))
