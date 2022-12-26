#!/usr/bin/env python
with open("input", "r") as file:
    values = file.read().splitlines()

horizontal, depth = 0, 0
for line in values:
    direction, amount = line.split(" ")
    if direction == "forward":
        horizontal += int(amount)
    elif direction == "up":
        depth -= int(amount)
    elif direction == "down":
        depth += int(amount)

print(horizontal * depth)

horizontal, depth, aim = 0, 0, 0
for line in values:
    direction, amount = line.split(" ")
    if direction == "forward":
        horizontal += int(amount)
        depth += aim * int(amount)
    elif direction == "up":
        aim -= int(amount)
    elif direction == "down":
        aim += int(amount)

print(horizontal * depth)
