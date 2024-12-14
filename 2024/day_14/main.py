#!/usr/bin/env python
import re

input_file = "input"

width, height = 101 if input_file == "input" else 11, 103 if input_file == "input" else 7
data = [tuple(map(int, re.findall(r"-?\d+", line))) for line in open(input_file).readlines()]


def solve(robots, steps):
    top_left, top_right, bottom_left, bottom_right = 0, 0, 0, 0
    for x, y, dx, dy in robots:
        x = (x + dx * steps) % width
        y = (y + dy * steps) % height

        top_left += x > width // 2 and y < height // 2
        top_right += x < width // 2 and y < height // 2
        bottom_left += x > width // 2 and y > height // 2
        bottom_right += x < width // 2 and y > height // 2

    return top_left * top_right * bottom_left * bottom_right


print(solve(data.copy(), 100))
print(min(range(10000), key=lambda x: solve(data.copy(), x)))
