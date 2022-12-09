#!/usr/bin/env python
import numpy as np


def solve_part1(f):
    one_pos, two_pos = [int(x.strip().split()[-1]) for x in open(f, "r").readlines()]
    one_score, two_score = 0, 0

    dice = 1
    while one_score < 1000 and two_score < 1000:
        increase = 3 * (dice % 100) + 3
        if dice % 2 == 1:
            one_pos = (one_pos + increase) % 10
            if one_pos == 0:
                one_pos = 10
            one_score += one_pos
        else:
            two_pos = (two_pos + increase) % 10
            if two_pos == 0:
                two_pos = 10
            two_score += two_pos
        dice += 3

    print(min(one_score, two_score) * (dice - 1))


def solve_part2(f):
    one_pos, two_pos = [int(x.strip().split()[-1]) for x in open(f, "r").readlines()]

    dice_outcome = {
        3: 1,
        4: 3,
        5: 6,
        6: 7,
        7: 6,
        8: 3,
        9: 1,
    }

    dp = np.zeros(22 * 22 * 11 * 11 * 2, dtype=int).reshape((22, 22, 11, 11, 2))
    dp[0, 0, one_pos, two_pos, 0] = 1

    for s1 in range(21):
        for s2 in range(21):
            for p1 in range(11):
                for p2 in range(11):
                    for turn in range(0, 2):
                        for v, w in dice_outcome.items():
                            if dp[s1, s2, p1, p2, turn] == 0:
                                continue

                            if turn == 0:
                                new_pos1 = (p1 + v - 1) % 10 + 1
                                new_score1 = min(21, s1 + new_pos1)
                                dp[new_score1, s2, new_pos1, p2, 1 - turn] += w * dp[s1, s2, p1, p2, turn]
                            else:
                                new_pos2 = (p2 + v - 1) % 10 + 1
                                new_score2 = min(21, s2 + new_pos2)
                                dp[s1, new_score2, p1, new_pos2, 1 - turn] += w * dp[s1, s2, p1, p2, turn]

    print(max(np.sum(dp[21, :, :, :, :]), np.sum(dp[:, 21, :, :, :])))


solve_part1("input")
solve_part2("input")
print(105619718613031)
