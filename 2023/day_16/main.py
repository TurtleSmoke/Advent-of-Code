#!/usr/bin/env python
import itertools
from collections import defaultdict

input_file = "input"

input_data = open(input_file).readlines()
input_size = len(input_data)
input_mirrors = defaultdict(
    lambda: ".",
    {(y + x * 1j): m for y, line in enumerate(input_data) for x, m in enumerate(line.strip()) if m in r"/|\|-"},
)


def energized_grid(mirrors, start_pos, start_dir, size):
    rays = [(start_pos, start_dir)]
    cache = defaultdict(set)

    while rays:
        p, d = rays.pop()

        if (not (0 <= p.real < size and 0 <= p.imag < size)) or d in cache[p]:
            continue

        cache[p].add(d)

        if mirrors[p] == "-" and d.real != 0:
            rays.append((p - 1j, -1j))
            rays.append((p + 1j, 1j))
        elif mirrors[p] == "|" and d.imag != 0:
            rays.append((p + 1, 1))
            rays.append((p - 1, -1))
        else:
            new_dir = {"/": lambda x: -complex(x.imag, x.real), "\\": lambda x: complex(x.imag, x.real)}.get(
                mirrors[p], lambda x: x
            )(d)

            rays.append((p + new_dir, new_dir))

    return len(cache)


print(energized_grid(input_mirrors, 0 + 0j, 0 + 1j, input_size))
print(
    max(
        energized_grid(input_mirrors, complex(*pos), d, input_size)
        for pos, d in itertools.chain(
            *(
                (((0, k), 1), ((input_size - 1, k), -1), ((k, 0), 1j), ((k, input_size - 1), -1j))
                for k in range(input_size)
            )
        )
    )
)
