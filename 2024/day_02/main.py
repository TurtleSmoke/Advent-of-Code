#!/usr/bin/env python

input_file = "input"

reports = [list(map(int, line.strip().split())) for line in open(input_file)]


def is_safe(nums):
    delta = [a - b for a, b in zip(nums, nums[1:])]
    return all(1 <= abs(d) <= 3 for d in delta) and all(d * delta[0] > 0 for d in delta)


def is_safe_with_dampener(nums):
    if is_safe(nums):
        return True
    return any(is_safe(nums[:i] + nums[i + 1 :]) for i in range(len(nums)))


print(sum(map(is_safe, reports)))
print(sum(map(is_safe_with_dampener, reports)))
