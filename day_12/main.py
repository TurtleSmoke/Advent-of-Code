from collections import defaultdict

data = [line.split('-') for line in open('input', 'r').read().splitlines()]

road = defaultdict(set)
for s, d in data:
    road[s].add(d)
    road[d].add(s)


def dfs(start, seen):
    if start == 'end':
        return 1

    return sum(dfs(end, (seen | {end} if end == end.lower() else seen))
               for end in road[start] if end not in seen)


def dfs2(start, seen, double):
    if start == 'end':
        return 1

    s = 0
    for end in road[start]:
        if end not in seen:
            s += dfs2(end, seen | {end} if end == end.lower() else seen, double)
        elif end != 'start' and double:
            s += dfs2(end, seen, False)
    return s


print(dfs("start", {"start"}))
print(dfs2("start", {"start"}, True))
