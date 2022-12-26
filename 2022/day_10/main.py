#!/usr/bin/env python
from itertools import accumulate

import numpy as np

input_file = "input"

instructions = list(map(int, open(input_file).read().replace("addx ", "noop\n").replace("noop", "0").splitlines()))

signal = list(accumulate(instructions, initial=1))

print(np.sum(np.arange(20, 221, 40) * signal[19:221:40]))
print("".join(["\n" * (i % 40 == 0) + "█" if abs((i % 40) - s) <= 1 else " " for i, s in enumerate(signal)]))
