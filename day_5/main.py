import re

values = [line.strip() for line in open('input', 'r')]

print(values)

values = [list(map(int, re.findall(r'\d+', l))) for l in values]

s1 = set()
s2 = set()

for (x1, y1, x2, y2) in values:
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            s1.add((x1, y)) if (x1, y) not in s1 else s2.add((x1, y))
    if y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            s1.add((x, y1)) if (x, y1) not in s1 else s2.add((x, y1))

print(len(set.intersection(s1, s2)))

s1 = set()
s2 = set()

for (x1, y1, x2, y2) in values:
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            s1.add((x1, y)) if (x1, y) not in s1 else s2.add((x1, y))
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            s1.add((x, y1)) if (x, y1) not in s1 else s2.add((x, y1))
    else:
        for i in range(0, abs(x1 - x2) + 1):
            (xi, yi) = (x1 + i * (1 if x2 > x1 else -1), y1 + i * (1 if y2 > y1 else -1))
            s1.add((xi, yi)) if (xi, yi) not in s1 else s2.add((xi, yi))

print(len(set.intersection(s1, s2)))
