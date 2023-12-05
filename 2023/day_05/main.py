#!/usr/bin/env python

from itertools import chain

input_file = "input"

blocks = [lines.split("\n") for lines in open(input_file).read().split("\n\n")]
data_seeds = list(map(int, blocks[0][0].split()[1:]))
data_seeds1 = [(seed, seed + 1) for seed in data_seeds]
data_seeds2 = [(seed, seed + delta) for seed, delta in zip(data_seeds[::2], data_seeds[1::2])]
data_transforms = [
    [(src, src + num, dst - src) for dst, src, num in (map(int, line.split()) for line in lines[1:])]
    for lines in blocks[1:]
]


def apply_transforms(seeds, transforms):
    for transform in transforms:
        seeds = list(chain.from_iterable(grow_seeds_range(*seed, transform) for seed in seeds))
    return seeds


def grow_seeds_range(seed_start, seed_stop, transform):
    for start, stop, offset in transform:
        if seed_stop <= start or seed_start >= stop:
            continue

        if start <= seed_start < seed_stop <= stop:
            return [(seed_start + offset, seed_stop + offset)]

        return (
            grow_seeds_range(seed_start, start, transform)
            + [(max(seed_start, start) + offset, min(seed_stop, stop) + offset)]
            + grow_seeds_range(stop, seed_stop, transform)
        )

    return [(seed_start, seed_stop)]


print(min(apply_transforms(data_seeds1, data_transforms))[0])
print(min(apply_transforms(data_seeds2, data_transforms))[0])
