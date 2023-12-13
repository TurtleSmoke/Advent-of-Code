#!/usr/bin/env python

input_file = "input"

input_grid = [
    {(y, x) for y, line in enumerate(block.split("\n")) for x, c in enumerate(line) if c == "#"}
    for block in open(input_file).read().split("\n\n")
]

input_rotated_grid = [{(x, y) for y, x in grid} for grid in input_grid]


def find_reflection(grid, smudges=0):
    max_x = max(x for y, x in grid)
    for reflection_line in range(1, max_x + 1):
        reflection = {(y, 2 * reflection_line - x - 1) for y, x in grid}
        reflection_len = min(reflection_line, max_x - reflection_line + 1)
        remaining = {(y, x) for y, x in (grid - reflection) if -reflection_len <= x - reflection_line < reflection_len}

        if len(remaining) == smudges:
            return reflection_line

    return 0


res = lambda grid, rotated_grid, smudges: 100 * find_reflection(rotated_grid, smudges) + find_reflection(grid, smudges)
print(sum(res(grid, rotated_grid, 0) for grid, rotated_grid in zip(input_grid, input_rotated_grid)))
print(sum(res(grid, rotated_grid, 1) for grid, rotated_grid in zip(input_grid, input_rotated_grid)))
