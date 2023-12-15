#!/usr/bin/env python
from functools import reduce

input_file = "input"

input_sequence = open(input_file).read().split(",")

hash_algorithm = lambda string: reduce(lambda h, c: ((h + ord(c)) * 17) % 256, string, 0)


def hashmap(sequence):
    boxes = [{} for _ in range(256)]
    for step in sequence:
        if step[-1] == "-":
            label = step[:-1]
            boxes[hash_algorithm(label)].pop(label, None)
        else:
            label, focal = step[:-2], int(step[-1])
            boxes[hash_algorithm(label)][label] = focal

    return boxes


print(sum(hash_algorithm(s) for s in input_sequence))
print(
    sum(
        (box_id * slot * focal)
        for box_id, box in enumerate(hashmap(input_sequence), start=1)
        for slot, focal in enumerate(box.values(), start=1)
    )
)
