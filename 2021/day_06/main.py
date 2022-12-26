#!/usr/bin/env python
from collections import Counter

import numpy as np

print(
    sum(
        (
            np.linalg.matrix_power(
                np.array(
                    [
                        [0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [1, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0],
                    ]
                ),
                256,
            )
        ).dot(
            np.array(
                [
                    dict(Counter([int(x) for line in open("input", "r") for x in line.strip().split(",")])).get(e, 0)
                    for e in range(9)
                ]
            )
        )
    )
)
