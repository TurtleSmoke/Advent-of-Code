#!/usr/bin/env python
from collections import Counter

input_file = "input"

left, right = map(sorted, zip(*list(map(int, line.split()) for line in open(input_file))))
left_2, right_2 = Counter(left), Counter(right)

print(sum(abs(r - l) for l, r in zip(left, right)))
print(sum(occ * k * right_2[k] for k, occ in left_2.items()))
