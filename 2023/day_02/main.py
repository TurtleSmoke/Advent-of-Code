#!/usr/bin/env python

import operator
import re
from functools import reduce

input_file = "input"

values = open("test_input").read().splitlines()

get_max_color = lambda regex, game: max(int(match) for match in re.findall(regex, game))
games = {
    int(id): (
        get_max_color(r"(\d+) red", game),
        get_max_color(r"(\d+) green", game),
        get_max_color(r"(\d+) blue", game),
    )
    for id, game in re.findall(r"Game (\d+): (.*)", open(input_file).read())
}

print(sum(id for id, color in games.items() if color[0] <= 12 and color[1] <= 13 and color[2] <= 14))
print(sum(reduce(operator.mul, max_colors) for max_colors in games.values()))
