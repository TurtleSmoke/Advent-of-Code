#!/bin/python3
from itertools import product, chain, count

val_input = "input"

blocks_coors = [
    [tuple(map(int, coors.strip().split(","))) for coors in line.split("->")]
    for line in open(val_input).read().splitlines()
]

all_blocks = {
    complex(*prod)
    for block_coors in blocks_coors
    for ((x1, y1), (x2, y2)) in zip(block_coors, block_coors[1:])
    for prod in chain(product(range(min(x1, x2), max(x1, x2) + 1), range(min(y1, y2), max(y1, y2) + 1)))
}


def fall(floor, blocks):
    pos = 500
    for y in range(0, floor):
        for x in 0, -1, 1:
            if complex(pos + x, y + 1) not in blocks:
                pos += x
                break
        else:
            return complex(pos, y)

    return complex(pos, floor)


def part1(floor, blocks):
    for i in count(0):
        new_block = fall(floor, blocks)
        if new_block.imag == floor:
            return i
        blocks.add(new_block)


def part2(floor, blocks):
    for i in count(1):
        blocks.add(fall(floor, blocks))
        if 500 in blocks:
            return i


initial_floor = int(max(b.imag for b in all_blocks))
print(part1(initial_floor, all_blocks.copy()))
print(part2(initial_floor + 1, all_blocks.copy()))
