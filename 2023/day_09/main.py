#!/usr/bin/env python

input_file = "input"
input_nums = [list(map(int, line.split())) for line in open(input_file).readlines()]


def extrapolate(nums):
    last_diff = [nums[-1]]
    while any(diff != 0 for diff in nums):
        nums = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
        last_diff.append(nums[-1])
    return sum(last_diff)


print(sum(extrapolate(nums) for nums in input_nums))
print(sum(extrapolate(nums[::-1]) for nums in input_nums))
