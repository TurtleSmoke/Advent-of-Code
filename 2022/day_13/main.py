#!/usr/bin/env python

from ast import literal_eval

input_file = "input"

packets = [tuple(map(literal_eval, line.split("\n"))) for line in open(input_file).read().strip().split("\n\n")]


def compare(left, right):
    if type(left) == type(right) == int:
        return right - left
    elif type(left) == int:
        return compare([left], right)
    elif type(right) == int:
        return compare(left, [right])

    if len(left) == 0 or len(right) == 0:
        return len(right) - len(left)

    return compare(left[0], right[0]) or compare(left[1:], right[1:])


print(sum(i + 1 for i in range(len(packets)) if compare(*packets[i]) > 0))
print(
    (1 + sum(compare([[2]], p) < 0 for packet in packets for p in packet))
    * (2 + sum(compare([[6]], p) < 0 for packet in packets for p in packet))
)
