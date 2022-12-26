#!/usr/bin/env python

input_file = "input"

jets = [1 if c == ">" else -1 for c in open(input_file).read().strip()]
rocks = [
    (0, 1, 2, 3),
    (1, 1j, 2 + 1j, 1 + 2j),
    (0, 1, 2, 2 + 1j, 2 + 2j),
    (0, 1j, 2j, 3j),
    (0, 1, 1j, 1 + 1j),
]
top_layer_rocks = [
    [0, 0, 0, 0, -1, -1, -1],
    [1, 2, 1, -1, -1, -1, -1],
    [0, 0, 2, -1, -1, -1, -1],
    [3, -1, -1, -1, -1, -1, -1],
    [1, 1, -1, -1, -1, -1, -1],
]


def update(tower, height, top, i_rock, i_jet):
    pos = complex(2, height + 4)
    is_pos_empty = lambda p: 0 <= p.real < 7 and p not in tower
    while True:
        jet = jets[i_jet]
        i_jet = (i_jet + 1) % len(jets)
        if all(is_pos_empty(pos + r + jet) for r in rocks[i_rock]):
            pos += jet
        if all(is_pos_empty(pos + r - 1j) for r in rocks[i_rock]):
            pos -= 1j
        else:
            last_rock = {pos + r for r in rocks[i_rock]}
            tower |= last_rock
            break

    new_height = int(pos.imag + [0, 2, 2, 3, 1][i_rock])
    top_last_rock = [top_layer_rocks[i_rock][int(i - pos.real) % 7] for i in range(7)]
    top = tuple(h + new_height - height - (p != -1) * (pos.imag - height + h + p) for h, p in zip(top, top_last_rock))

    return tower, max(height, new_height), top, (i_rock + 1) % len(rocks), i_jet


def tower_build(stop):
    tower, cache, top = set(range(7)), {}, [0] * 7
    height, i_rock, i_jet = 0, 0, 0

    for n in range(int(stop)):
        tower, height, top, i_rock, i_jet = update(tower, height, top, i_rock, i_jet)

        if (i_rock, i_jet, top) in cache:
            number_of_cycle, iteration_until_cycle = divmod(int(stop) - n, n - cache[i_rock, i_jet, top][0])
            for _ in range(iteration_until_cycle - 1):
                tower, height, top, i_rock, i_jet = update(tower, height, top, i_rock, i_jet)
            return height + number_of_cycle * (height - cache[i_rock, i_jet, top][1])
        else:
            cache[i_rock, i_jet, top] = n, height

    return height


print(int(tower_build(2022)))
print(int(tower_build(1e12)))
