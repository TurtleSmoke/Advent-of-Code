#!/usr/bin/env python
from itertools import product
import numpy as np

input_file = "input"

tree_grid = np.genfromtxt(input_file, delimiter=1, dtype=int)

tree_dirs = np.array(
    [np.rot90((np.diff(np.maximum.accumulate(np.rot90(tree_grid, r), 1), 1) != 0)[1:-1, :-1], -r) for r in range(4)]
)

print(4 * (len(tree_grid) - 1) + np.sum(np.logical_or.reduce(tree_dirs)))

print(
    max(
        np.product(
            list(
                next((i + 1 for i, t in enumerate(tree_view) if t >= tree_grid[x][y]), len(tree_view))
                for tree_view in [
                    tree_grid[x][y - 1 :: -1],
                    tree_grid[x][y + 1 : :],
                    tree_grid[x - 1 :: -1, y],
                    tree_grid[x + 1 : :, y],
                ]
            )
        )
        for x, y in product(range(1, len(tree_grid) - 1), range(1, len(tree_grid[0]) - 1))
    )
)
