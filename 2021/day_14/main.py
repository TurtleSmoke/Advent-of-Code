#!/usr/bin/env python
from collections import Counter, defaultdict

with open("input", "r") as f:
    polymer, pair = f.read().split("\n\n")

pair = {line.split(" -> ")[0]: line.split(" -> ")[1] for line in pair.splitlines()}

for j in range(10):
    poly = ""
    for i in range(len(polymer) - 1):
        c1, c2 = polymer[i], polymer[i + 1]
        poly += c1
        if c1 + c2 in pair:
            poly += pair[c1 + c2]

    polymer = poly + polymer[-1]

occ = Counter(polymer)
print(max(occ.values()) - min(occ.values()))

with open("input", "r") as f:
    polymer, pair = f.read().split("\n\n")

pair = {line.split(" -> ")[0]: line.split(" -> ")[1] for line in pair.splitlines()}

occ2 = Counter(a + b for a, b in zip(polymer[:-1], polymer[1:]))
for j in range(40):
    next_occ = Counter()
    for p, v in occ2.items():
        if p in pair:
            next_occ[p[0] + pair[p]] += v
            next_occ[pair[p] + p[1]] += v
            occ2[p] = 0
    for p, v in next_occ.items():
        occ2[p] += v
    occ2 = Counter({k: v for k, v in occ2.items() if v > 0})

res = defaultdict(lambda: 0)
for p, v in occ2.items():
    res[p[0]] += v
    res[p[1]] += v

res = {k: (v + 1) // 2 for k, v in res.items()}
print(max(res.values()) - min(res.values()))
