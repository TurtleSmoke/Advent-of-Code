#!/bin/python3
from itertools import product

import numpy as np

val_input = "input"

tree_grid = np.genfromtxt(val_input, delimiter=1, dtype=int)

tree_dirs = np.array(
    [
        np.pad(np.maximum.accumulate(tree_grid, axis=1), ((0, 1), (1, 0)), constant_values=-1),
        np.roll(
            np.pad(
                np.flip(np.maximum.accumulate(np.flip(tree_grid, axis=1), axis=1), axis=1),
                ((0, 1), (0, 1)),
                constant_values=-1,
            ),
            -1,
        ),
        np.pad(np.maximum.accumulate(tree_grid, axis=0), ((1, 0), (0, 1)), constant_values=-1),
        np.roll(
            np.flip(
                np.pad(np.maximum.accumulate(np.flip(tree_grid, axis=0), axis=0), ((1, 0), (0, 1)), constant_values=-1),
                axis=0,
            ),
            -1,
            axis=0,
        ),
    ]
)

print(sum(tree_grid[i, j] > min(tree_dirs[:, i, j]) for i, j in np.ndindex(tree_grid.shape)))

print(
    max(
        np.product(
            list(
                next((i + 1 for i in range(len(tree_view)) if tree_view[i] >= tree_grid[x][y]), len(tree_view))
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
