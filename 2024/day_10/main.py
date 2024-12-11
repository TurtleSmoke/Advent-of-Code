#!/usr/bin/env python

input_file = "input"

data = {y + x * 1j: int(v) for x, row in enumerate(open(input_file)) for y, v in enumerate(row.strip())}

starts = [[pos] for pos in data if data[pos] == 0]
for hike in range(1, 10):
    starts = [[p + d for p in poses for d in [1, -1, 1j, -1j] if data.get(p + d) == hike] for poses in starts]

print(sum(map(len, map(set, starts))))
print(len(list(x for y in starts for x in y)))
