#!/usr/bin/env python
from itertools import product, chain

input_file = "input"

initial_blocks = {
    complex(*prod)
    for block in [list(map(eval, line.split("->"))) for line in open(input_file).read().strip().splitlines()]
    for ((x1, y1), (x2, y2)) in zip(block, block[1:])
    for prod in chain(product(range(min(x1, x2), max(x1, x2) + 1), range(min(y1, y2), max(y1, y2) + 1)))
}
initial_floor = max(b.imag for b in initial_blocks)
initial_blocks_number = len(initial_blocks)


def solve(part, blocks):
    dp = [500]
    while True:
        last_block = dp[-1]
        for new_block in last_block + 1j, last_block - 1 + 1j, last_block + 1 + 1j:
            if new_block not in blocks and new_block.imag < initial_floor + 2:
                dp.append(new_block)
                break
        else:
            if part(last_block):
                return len(blocks) - initial_blocks_number
            blocks.add(last_block)
            del dp[-1]


print(solve(lambda pos: pos.imag > initial_floor, initial_blocks))
print(solve(lambda pos: pos == 500, initial_blocks) + 1)
