#!/usr/bin/env python

input_file = "input"


def parse_grid(data):
    grid = {}
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            match char:
                case "|":
                    grid[(y, x)] = {(y - 1, x), (y + 1, x)}
                case "-":
                    grid[(y, x)] = {(y, x - 1), (y, x + 1)}
                case "L":
                    grid[(y, x)] = {(y - 1, x), (y, x + 1)}
                case "J":
                    grid[(y, x)] = {(y, x - 1), (y - 1, x)}
                case "7":
                    grid[(y, x)] = {(y, x - 1), (y + 1, x)}
                case "F":
                    grid[(y, x)] = {(y + 1, x), (y, x + 1)}
                case "S":
                    start = (y, x)
                    grid[(y, x)] = {
                        (y, x - 1),
                        (y, x + 1),
                        (y - 1, x),
                        (y + 1, x),
                    }
                case _:
                    pass

    grid[start] = {dst for dst in grid[start] if start in grid.get(dst, set())}
    return grid, start


def find_cycle(grid, start):
    seen = {start}
    queue = [start]
    while queue:
        current = queue.pop(0)
        for dst in grid[current]:
            if dst not in seen:
                seen.add(dst)
                queue.append(dst)

    return seen


def find_inside(grid, cycle):
    max_y = max(y for y, _ in grid.keys())
    max_x = max(x for _, x in grid.keys())

    inside = set()
    for y in range(max_y):
        pipe = 0
        for x in range(max_x):
            pos = (y, x)
            if pos in cycle:
                if (y - 1, x) in grid[pos]:
                    pipe += 1
            elif pipe % 2 == 1:
                inside.add(pos)

    return len(inside)


input_grid, input_start = parse_grid(open(input_file).read().splitlines())
print(len(find_cycle(input_grid, input_start)) // 2)
print(find_inside(input_grid, find_cycle(input_grid, input_start)))
