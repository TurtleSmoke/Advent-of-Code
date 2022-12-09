#!/bin/python3
from itertools import product

import numpy as np

val_input = "input"

tree_grid = np.genfromtxt(val_input, delimiter=1, dtype=int)
tree_dirs = np.array(
    [
        np.rot90(np.maximum.accumulate(np.rot90(np.pad(tree_grid, 1, constant_values=-1), r), axis=1)[1:-1, :-2], -r)
        for r in range(4)
    ]
)

print(np.sum(np.logical_or.reduce(tree_dirs - tree_grid < 0)))

print(
    max(
        np.product(
            list(
                next((i + 1 for i in range(len(tree_view)) if tree_view[i] >= tree_grid[x][y]), len(tree_view))
                for tree_view in [
                    tree_grid[x][y - 1:: -1],
                    tree_grid[x][y + 1::],
                    tree_grid[x - 1:: -1, y],
                    tree_grid[x + 1::, y],
                ]
            )
        )
        for x, y in product(range(1, len(tree_grid) - 1), range(1, len(tree_grid[0]) - 1))
    )
)
