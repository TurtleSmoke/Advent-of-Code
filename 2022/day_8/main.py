#!/bin/python3
from itertools import product

import numpy as np

val_input = "input"

tree_grid = np.genfromtxt(val_input, delimiter=1, dtype=int)
padded_tree_grid = np.pad(tree_grid, 1, constant_values=-1)

tree_dirs = np.array(
    [
        np.maximum.accumulate(padded_tree_grid, axis=1)[1:-1, :-2],
        np.maximum.accumulate(padded_tree_grid[:, ::-1], axis=1)[:, ::-1][1:-1, 2:],
        np.maximum.accumulate(padded_tree_grid, axis=0)[:-2, 1:-1],
        np.maximum.accumulate(padded_tree_grid[::-1])[::-1][2:, 1:-1],
    ]
)

print(sum(tree_grid[i, j] > min(tree_dirs[:, i, j]) for i, j in np.ndindex(tree_grid.shape)))

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
