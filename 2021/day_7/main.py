values = list(sorted(int(x) for x in open("input", "r").read().split(",")))

print(sum(abs(i - values[(len(values) - 1) // 2]) for i in values))

print(sum(abs(n - sum(values) // len(values)) * (abs(n - sum(values) // len(values)) + 1) // 2 for n in values))
