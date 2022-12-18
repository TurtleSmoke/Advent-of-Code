#!/usr/bin/env python

import numpy as np
import scipy.ndimage as ndi

val_input = "input"

cubes = np.loadtxt(val_input, dtype=int, delimiter=",")
space = np.zeros(cubes.max(axis=0) + 1)
space[tuple(cubes.T)] = 1

print(sum(np.count_nonzero(np.diff(space, 1, dim, 0, 0)) for dim in range(3)))

space = ndi.binary_fill_holes(space)
print(sum(np.count_nonzero(np.diff(space, 1, dim, 0, 0)) for dim in range(3)))
