#!/usr/bin/env python

import numpy as np

val_input = "input"

instructions = [1] + list(map(int, open(val_input).read().replace("addx ", "noop\n").replace("noop", "0").splitlines()))

signal = np.add.accumulate(instructions)

print(np.sum(np.arange(20, 221, 40) * signal[19:221:40]))
print("".join(["\n" * (i % 40 == 0) + "█" if abs((i % 40) - signal[i]) <= 1 else " " for i in range(len(signal))]))
