#!/usr/bin/env python

val_input = "input"

jets = [1 if c == ">" else -1 for c in open(val_input).read().strip()]
rocks = [
    (0, 1, 2, 3),
    (1, 1j, 2 + 1j, 1 + 2j),
    (0, 1, 2, 2 + 1j, 2 + 2j),
    (0, 1j, 2j, 3j),
    (0, 1, 1j, 1 + 1j),
]


def rock_fall(i_jet, pos, rock, tower):
    is_pos_empty = lambda p: 0 <= p.real < 7 and p not in tower
    while True:
        jet = jets[i_jet]
        i_jet = (i_jet + 1) % len(jets)
        if all(is_pos_empty(pos + r + jet) for r in rock):
            pos += jet
        if all(is_pos_empty(pos + r - 1j) for r in rock):
            pos -= 1j
        else:
            last_rock = {pos + r for r in rock}
            return i_jet, last_rock, tower | last_rock


def update(tower, height, top, last_rock, i_rock, i_jet):
    height = max(height, max(p.imag for p in last_rock))
    initial_position = complex(2, height + 4)
    rock = rocks[i_rock]
    i_rock = (i_rock + 1) % len(rocks)
    i_jet, last_rock, tower = rock_fall(i_jet, initial_position, rock, tower)

    new_height = max(p.imag for p in last_rock)
    top_layer_last_rock = [min(new_height - p.imag * (p.real == x) for p in last_rock) for x in range(7)]
    top = tuple(min(h + new_height - height, p) for h, p in zip(top, top_layer_last_rock))

    return tower, height, top, last_rock, i_rock, i_jet


def tower_build(stop):
    tower, cache, last_rock, top = set(range(7)), {}, set(range(7)), [0] * 7
    height, i_rock, i_jet = 0, 0, 0

    for n in range(int(stop)):
        tower, height, top, last_rock, i_rock, i_jet = update(tower, height, top, last_rock, i_rock, i_jet)

        if (i_rock, i_jet, top) in cache:
            number_of_cycle, iteration_until_cycle = divmod(int(stop) - n, n - cache[i_rock, i_jet, top][0])
            for _ in range(iteration_until_cycle):
                tower, height, top, last_rock, i_rock, i_jet = update(tower, height, top, last_rock, i_rock, i_jet)
            return height + number_of_cycle * (height - cache[i_rock, i_jet, top][1])
        else:
            cache[i_rock, i_jet, top] = n, height

    return max(p.imag for p in tower)


print(int(tower_build(2022)))
print(int(tower_build(1e12)))
