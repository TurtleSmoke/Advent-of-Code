with open("input", "r") as file:
    values = [int(line) for line in file.read().splitlines()]

print(sum(a < b for a, b in zip(values[:-1], values[1:])))

three_values = [sum(v) for v in zip(values[:-2], values[1:-1], values[2:])]

print(sum(a < b for a, b in (zip(three_values[:-1], three_values[1:]))))
