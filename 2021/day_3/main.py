#!/usr/bin/env python
with open("input", "r") as file:
    values = file.read().splitlines()

gamma = int(
    "".join(
        ("1" if sum(line[i] == "1" for line in values) >= (len(values) + 1) // 2 else "0")
        for i in range(len(values[0]))
    ),
    2,
)

print(gamma * (~gamma & 0xFFF))

lsr = values
co2 = values
for i, _ in enumerate(range(len(values[0]))):
    v = "1" if sum(line[i] == "1" for line in lsr) >= (len(lsr) + 1) // 2 else "0"
    if len(lsr) > 1:
        lsr = [n for n in lsr if n[i] == v]
    v = "1" if sum(line[i] == "1" for line in co2) >= (len(co2) + 1) // 2 else "0"
    if len(co2) > 1:
        co2 = [n for n in co2 if n[i] != v]

print(int(lsr[0], 2) * int(co2[0], 2))
