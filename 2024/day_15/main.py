#!/usr/bin/env python

input_file = "input"

initial_grid, moves = open(input_file).read().split("\n\n")

grid1 = {x + y * 1j: c for y, row in enumerate(initial_grid.splitlines()) for x, c in enumerate(row)}
grid2 = {
    x + y * 1j: c
    for y, row in enumerate(initial_grid.splitlines())
    for x, c in enumerate(row.translate(str.maketrans({"#": "##", ".": "..", "O": "[]", "@": "@."})))
}
moves = [{"<": -1, ">": 1, "^": -1j, "v": 1j}[d] for d in moves.replace("\n", "")]


def move(grid, p, d):
    p += d
    if all(
        [
            grid[p] != "[" or move(grid, p + 1, d) and move(grid, p, d),
            grid[p] != "]" or move(grid, p - 1, d) and move(grid, p, d),
            grid[p] != "O" or move(grid, p, d),
            grid[p] != "#",
        ]
    ):
        grid[p], grid[p - d] = grid[p - d], grid[p]
        return True
    return False


def solve(grid, moves):
    pos = next(k for k, v in grid.items() if v == "@")
    for m in moves:
        copy = grid.copy()
        if move(grid, pos, m):
            pos += m
        else:
            grid = copy
    return [p for p in grid if grid[p] in "O["]


print(int(sum(res.real + res.imag * 100 for res in solve(grid1, moves))))
print(int(sum(res.real + res.imag * 100 for res in solve(grid2, moves))))
