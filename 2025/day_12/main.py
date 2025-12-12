#!/usr/bin/env python
import re

import numpy as np

input_file = "input"

*presents, regions = open(input_file).read().strip().split("\n\n")
presents = [present[3:] for present in presents]
regions = [
    ((a, b), np.array(plist)) for r in regions.splitlines() for a, b, *plist in [list(map(int, re.findall(r"\d+", r)))]
]


# This is a "Polyomino Packing problem", it is NP-complete in general.
# The only solution is brute-forcing with backtracking and early pruning.
# The idea is to add more and more pruning conditions until the solution works for the input of interest.

# True Lower bound
print(sum(sum(plist * [present.count("#") for present in presents]) <= a * b for (a, b), plist in regions))

# Initial upper bound (could be refined further with more complex checks, but not needed here)
print(
    sum(
        sum(plist * [present.index("\n") * len(present.split("\n")) for present in presents]) <= a * b
        for (a, b), plist in regions
    )
)

# lower bound == upper bound => exact solution
