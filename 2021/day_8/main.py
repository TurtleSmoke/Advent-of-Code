values = [tuple(values.split() for values in line.split("|")) for line in open("input", "r").read().splitlines()]

print(sum(len(value) in (2, 3, 4, 7) for line in values for value in line[1]))

ldic = {2: "1", 3: "7", 4: "4", 7: "8"}
res = 0
for pattern, value in values:
    vdic = {}
    for p in pattern:
        if len(p) in ldic:
            vdic[len(p)] = set(c for c in p)

    cur = ""
    for v in value:
        l = len(v)
        if l in ldic:
            cur += ldic[l]

        v = set(c for c in v)
        if l == 5:
            if len(v.intersection(vdic[2])) == 2:
                cur += "3"
            elif len(v.intersection(vdic[4])) == 3:
                cur += "5"
            else:
                cur += "2"
        if l == 6:
            if len(v.intersection(vdic[4])) == 4:
                cur += "9"
            elif len(v.intersection(vdic[2])) == 2:
                cur += "0"
            else:
                cur += "6"
    print(cur)
    res += int(cur)

print(res)
