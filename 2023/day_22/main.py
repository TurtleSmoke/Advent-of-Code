#!/usr/bin/env python
import re

import numpy as np

input_file = "input"

input_stack = np.array(
    list(
        sorted((list(map(int, re.findall(r"\d+", line))) for line in open(input_file).readlines()), key=lambda x: x[2])
    )
) + np.array([[0, 0, 0, 1, 1, 1]])


def drop(stack, skip=None):
    stack_height_map = np.zeros((np.max(stack[[0, 3]]) + 1, np.max(stack[[1, 4]]) + 1))
    falling_bricks = 0

    for i, (u, v, w, x, y, z) in enumerate(stack):
        if skip == i:
            continue

        brick_height = z - w
        new_brick_height = np.max(stack_height_map[u:x, v:y])
        stack_height_map[u:x, v:y] = new_brick_height + brick_height
        stack[i] = u, v, new_brick_height, x, y, new_brick_height + brick_height
        falling_bricks += new_brick_height < w

    return falling_bricks


drop(input_stack)
print(sum(not drop(input_stack.copy(), i) for i in range(len(input_stack))))
print(sum(drop(input_stack.copy(), i) for i in range(len(input_stack))))
