#!/usr/bin/env python

input_file = "test_input"

data = [(i // 2 + 1 if i % 2 else 0, int(d)) for i, d in enumerate(open(input_file).read().strip(), 1)]


def solve1(states):
    used_idx, free_idx = len(states) - 1, 0
    while used_idx > free_idx:
        used, used_occ = states[used_idx]
        free, free_occ = states[free_idx]
        if not used:
            used_idx -= 1
            continue
        if free or free_occ == 0:
            free_idx += 1
            continue

        states[used_idx] = (used, max(0, used_occ - free_occ))
        states[free_idx] = (0, max(0, free_occ - used_occ))
        states.insert(free_idx, (used, min(free_occ, used_occ)))
        free_idx += 1
        used_idx += 1
        if not states[used_idx][1]:
            used_idx -= 1

    return states


def solve2(states):
    for used_pos in range(len(states))[::-1]:
        for free_pos in range(used_pos):
            used, used_occ = states[used_pos]
            free, free_occ = states[free_pos]
            if used and not free and free_occ >= used_occ:
                states[used_pos] = (0, used_occ)
                states[free_pos] = (0, free_occ - used_occ)
                states.insert(free_pos, (used, used_occ))
    return states


print(
    sum(i * (v - 1) for i, v in enumerate([x for y in [[v] * occ for v, occ in solve1(data.copy()) if v] for x in y]))
)
print(
    sum(i * (v - 1) for i, v in enumerate([x for y in [[v] * occ for v, occ in solve2(data.copy())] for x in y]) if v)
)
