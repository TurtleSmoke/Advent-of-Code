#!/usr/bin/env python

import heapq

input_file = "input"

input_grid = {
    i + j * 1j: int(c) for i, line in enumerate(open(input_file).readlines()) for j, c in enumerate(line.strip())
}
input_end = [*input_grid][-1]


def dijksta(grid, min_d, max_d, end):
    heap = [(0, 0, 0, 1), (0, 0, 0, 1j)]
    seen = set()

    while heap:
        cur_val, _, cur_pos, cur_d = heapq.heappop(heap)

        if (cur_pos, cur_d) in seen:
            continue
        if cur_pos == end:
            return cur_val

        seen.add((cur_pos, cur_d))
        for d in (1j / cur_d, -1j / cur_d):
            new_pos = cur_pos + d * (min_d - 1)
            if new_pos not in grid:
                continue

            path_val = sum(grid[cur_pos + d * j] for j in range(1, min_d))
            for _ in range(min_d, max_d + 1):
                new_pos += d
                if new_pos in grid:
                    path_val += grid[new_pos]
                    heapq.heappush(heap, (cur_val + path_val, id(new_pos), new_pos, d))


print(dijksta(input_grid, 1, 3, input_end))
print(dijksta(input_grid, 4, 10, input_end))
