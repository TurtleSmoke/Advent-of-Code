#!/usr/bin/env python
input_file = "input"

data = open(input_file).read().replace(" ", "").splitlines()

part1 = {"BX": 1, "CY": 2, "AZ": 3, "AX": 4, "BY": 5, "CZ": 6, "CX": 7, "AY": 8, "BZ": 9}
part2 = {"BX": 1, "CX": 2, "AX": 3, "AY": 4, "BY": 5, "CY": 6, "CZ": 7, "AZ": 8, "BZ": 9}

print(sum(map(part1.get, data)))
print(sum(map(part2.get, data)))
