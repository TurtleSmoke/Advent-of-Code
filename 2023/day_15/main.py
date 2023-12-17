#!/usr/bin/env python
from functools import reduce

input_file = "input"

input_sequence = open(input_file).read().split(",")
hash_algorithm = lambda string: reduce(lambda h, c: ((h + ord(c)) * 17) % 256, string, 0)


def hashmap(sequence):
    boxes = [{} for _ in range(256)]
    for step in sequence:
        match step.strip("-").split("="):
            case [label, focal]:
                boxes[hash_algorithm(label)][label] = int(focal)
            case [label]:
                boxes[hash_algorithm(label)].pop(label, None)

    return boxes


print(sum(hash_algorithm(s) for s in input_sequence))
print(
    sum(
        (box_id * slot * focal)
        for box_id, box in enumerate(hashmap(input_sequence), start=1)
        for slot, focal in enumerate(box.values(), start=1)
    )
)
