#!/usr/bin/env python

input_file = "input"

input_data = list(
    (springs, list(map(int, groups.split(","))))
    for springs, groups in (line.split() for line in open(input_file).read().splitlines())
)


def solve_memoization(springs, groups, i, j, cache):
    if i == len(springs):
        return j == len(groups), cache

    if j == len(groups):
        return "#" not in springs[i:], cache

    if (i, j) in cache:
        return cache[(i, j)], cache

    total = 0
    if springs[i] in ".?":
        new_total, cache = solve_memoization(springs, groups, i + 1, j, cache)
        total += new_total

    current_group_len = groups[j]
    if (
        springs[i] in "#?"
        and len(springs) >= i + current_group_len
        and "." not in springs[i : i + current_group_len]
        and springs[i + current_group_len] != "#"
    ):
        new_total, cache = solve_memoization(springs, groups, i + current_group_len + 1, j + 1, cache)
        total += new_total

    cache[(i, j)] = total
    return total, cache


# Actually slower than the memoization solution because all sub-problems does not need to be solved.
def solve_dp(springs, groups):
    springs = ".." + springs.strip(".")
    dp = [0] * len(springs)

    for i in range(next((i for i, c in enumerate(springs) if c == "#"), len(springs))):
        dp[i] = 1

    for count in groups:
        n_dp = [0] * len(springs)
        chunk = 0

        for i in range(1, len(springs)):
            c = springs[i]
            if c != ".":
                chunk += 1
            else:
                chunk = 0

            if c != "#":
                n_dp[i] += n_dp[i - 1]

            if chunk >= count and springs[i - count] != "#":
                n_dp[i] += dp[i - count - 1]

        dp = n_dp

    return dp[-1]


print(sum(solve_memoization(spring + ".", group, 0, 0, {})[0] for spring, group in input_data))
print(sum(solve_memoization("?".join([spring] * 5) + ".", group * 5, 0, 0, {})[0] for spring, group in input_data))
print(sum(solve_dp(spring, group) for spring, group in input_data))
print(sum(solve_dp("?".join([spring] * 5), group * 5) for spring, group in input_data))
