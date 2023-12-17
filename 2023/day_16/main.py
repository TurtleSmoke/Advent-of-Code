#!/usr/bin/env python

input_file = "test_input"

input_mirrors = {(y + x * 1j): m for y, line in enumerate(open(input_file)) for x, m in enumerate(line.strip())}
map_dir = {"|": lambda _: 1, "-": lambda _: -1j, "\\": lambda x: 1j / x, "/": lambda x: -1j / x, ".": lambda x: x}


def energized_grid(mirrors, start_pos, start_dir):
    rays = [(start_pos, start_dir)]
    cache = set()

    while rays:
        cur_pos, cur_dir = rays.pop()

        while not (cur_pos, cur_dir) in cache:
            cache.add((cur_pos, cur_dir))
            cur_pos += cur_dir
            if cur_pos not in mirrors:
                break

            cur_dir = map_dir[mirrors[cur_pos]](cur_dir)
            if mirrors[cur_pos] in "|-":
                rays.append((cur_pos, -cur_dir))

    return len(set(pos for pos, _ in cache)) - 1


print(energized_grid(input_mirrors, -1j, 1j))
print(
    max(
        energized_grid(input_mirrors, pos - d, d)
        for d in (1, 1j, -1, -1j)
        for pos in input_mirrors
        if pos - d not in input_mirrors
    )
)
