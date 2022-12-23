#!/usr/bin/env python
from collections import Counter
from itertools import count

val_input = "input"

elves = {
    complex(x, y)
    for y, row in enumerate(open(val_input).read().splitlines())
    for x, val in enumerate(row)
    if val == "#"
}
directions = [
    [-1j, -1j + 1, -1j - 1],
    [1j, 1j + 1, 1j - 1],
    [-1, -1 + 1j, -1 - 1j],
    [1, 1 + 1j, 1 - 1j],
]
around = {d for dirs in directions for d in dirs}
next_dir = [-1j, 1j, -1, 1]

for i in count(0):
    move_to = {}
    for elf in elves:
        if elves & {elf + v for v in around}:
            for d in range(4):
                if not elves & {elf + v for v in directions[(i + d) % 4]}:
                    move_to[elf] = elf + next_dir[(i + d) % 4]
                    break

    move_to_number = Counter(move_to.values())
    can_moves = {cur for cur, nxt in move_to.items() if move_to_number[nxt] == 1}
    if not can_moves:
        print(i + 1)
        break

    elves = (elves - can_moves) | {move_to[elf] for elf in can_moves}

    if i == 9:
        minh, maxh, minw, maxw = (
            min(e.real for e in elves),
            max(e.real for e in elves),
            min(e.imag for e in elves),
            max(e.imag for e in elves),
        )
        print((maxh - minh + 1) * (maxw - minw + 1) - len(elves))
