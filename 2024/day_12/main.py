#!/usr/bin/env python
from collections import defaultdict

input_file = "input"

data = {y + x * 1j: c for x, row in enumerate(open(input_file)) for y, c in enumerate(row.strip())}


def find(pos, union_find):
    if pos not in union_find:
        union_find[pos] = pos
    if union_find[pos] != pos:
        union_find[pos] = find(union_find[pos], union_find)
    return union_find[pos]


def union(pos1, pos2, union_find):
    union_find[find(pos1, union_find)] = find(pos2, union_find)


union_find = {}
for source in data:
    find(source, union_find)
    for neighbour in [source + 1, source + 1j, source - 1, source - 1j]:
        if neighbour in data and data[neighbour] == data[source]:
            union(source, neighbour, union_find)

components = defaultdict(set)
for source, component in union_find.items():
    components[find(source, union_find)].add(source)

areas = [len(component) for component in components.values()]
perimeters = [{(p, d) for d in [1, -1, 1j, -1j] for p in c if p + d not in c} for c in components.values()]

print(sum(area * len(perimeter) for area, perimeter in zip(areas, perimeters)))
print(
    sum(area * len(perimeter - {(p + 1j * d, d) for p, d in perimeter}) for area, perimeter in zip(areas, perimeters))
)
