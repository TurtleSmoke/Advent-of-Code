#!/usr/bin/env python
import itertools

input_file = "input"

input_galaxies = {(y, x) for y, line in enumerate(open(input_file)) for x, c in enumerate(line) if c == "#"}


def expand_space(galaxies, expansion):
    rows, cols = zip(*galaxies)
    max_row, max_col = max(rows) + 1, max(cols) + 1
    empty_rows, empty_cols = set(range(max_row)) - set(rows), set(range(max_col)) - set(cols)
    cum_sum_rows = {row: sum(r < row for r in empty_rows) * (expansion - 1) for row in range(max_row)}
    cum_sum_cols = {col: sum(c < col for c in empty_cols) * (expansion - 1) for col in range(max_col)}

    return {(y + cum_sum_rows[y], x + cum_sum_cols[x]) for y, x in galaxies}


norm_1 = lambda x1, y1, x2, y2: abs(x1 - x2) + abs(y1 - y2)


print(sum(norm_1(*c1, *c2) for c1, c2 in itertools.combinations(expand_space(input_galaxies, 2), 2)))
print(sum(norm_1(*c1, *c2) for c1, c2 in itertools.combinations(expand_space(input_galaxies, 1000000), 2)))
