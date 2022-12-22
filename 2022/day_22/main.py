#!/usr/bin/env python
import re

val_input = "input"

data = open(val_input).read().split("\n\n")
grid = data[0].splitlines()
path = re.findall(r"\d+|[LR]", data[1])

max_width, max_height = max(map(len, grid)), len(grid)
objects = {i + j * 1j: c for i, line in enumerate(grid) for j, c in enumerate(line) if c in ".#"}
steps = list(map(int, path[::2]))
directions = path[1::2]

cubic_wrap = {
    (1j, 0): lambda x: (complex(149 - x, 99), -1j),
    (1j, 1): lambda x: (complex(49, x + 50), -1),
    (1j, 2): lambda x: (complex(149 - x, 149), -1j),
    (1j, 3): lambda x: (complex(149, x - 100), -1),
    (-1j, 0): lambda x: (complex(149 - x, 0), 1j),
    (-1j, 1): lambda x: (complex(100, x - 50), 1),
    (-1j, 2): lambda x: (complex(149 - x, 50), 1j),
    (-1j, 3): lambda x: (complex(0, x - 100), 1),
    (1, 0): lambda y: (complex(0, y + 100), 1),
    (1, 1): lambda y: (complex(100 + y, 49), -1j),
    (1, 2): lambda y: (complex(-50 + y, 99), -1j),
    (-1, 0): lambda y: (complex(50 + y, 50), 1j),
    (-1, 1): lambda y: (complex(100 + y, 0), 1j),
    (-1, 2): lambda y: (complex(199, y - 100), -1),
}


def wrap1(next_pos, next_dir):
    while next_pos not in objects:
        next_pos += next_dir
        next_pos = (next_pos.real + max_height) % max_height + 1j * ((next_pos.imag + max_width) % max_width)
    return next_pos, next_dir


def wrap2(next_pos, next_dir):
    if next_dir.real == 0:
        next_pos, next_dir = cubic_wrap[next_dir, next_pos.real // 50](next_pos.real)
    else:
        next_pos, next_dir = cubic_wrap[next_dir, next_pos.imag // 50](next_pos.imag)
    return next_pos, next_dir


def solve(wrap):
    cur_pos, cur_dir = grid[0].index(".") * 1j, 1j
    for i in range(len(steps)):
        for _ in range(steps[i]):
            next_pos, next_dir = cur_pos + cur_dir, cur_dir
            if next_pos not in objects:
                next_pos, next_dir = wrap(next_pos, next_dir)
            if objects[next_pos] == ".":
                cur_pos, cur_dir = next_pos, next_dir
        cur_dir *= {"R": -1j, "L": 1j, False: 1}[i < len(directions) and directions[i]]
    return int((cur_pos.real + 1) * 1000 + (cur_pos.imag + 1) * 4) + [1j, 1, -1j, -1].index(cur_dir)


print(solve(wrap1))
print(solve(wrap2))
