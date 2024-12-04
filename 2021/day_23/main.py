#!/usr/bin/env python
from collections import deque


def find_path(start, value, current_grid, goals, total):
    q = deque([[(start[0], start[1], total)]])
    prev = {start}
    steps = {}
    while q:
        path = q.popleft()
        x, y, cur = path[-1]
        if (x, y) in goals:
            steps[(x, y)] = cur
        for a, b in adj(x, y):
            if (a, b) in current_grid and (not current_grid[(a, b)].isalpha() and (a, b) not in prev):
                q.append(path + [(a, b, cur + cost[value])])
                prev.add((a, b))
    return steps


def find_route(grids, total):
    state = tuple(sorted(grids.items()))
    if (bests and total >= min(bests)) or (state in states and states[state] <= total):
        return
    states[state] = total
    if not any(v.isalpha() for v in grids.values()):
        bests.append(total)
        return
    for k, v in sorted(grids.items(), key=lambda x: x[0] not in [5, 7]):
        if v.isalpha() and ((k[0], k[1] - 1) not in grids or grids[k[0], k[1] - 1] == "."):
            goals = []
            valid_grid = {(x, 1): grids[x, 1] for x in range(min(vald), max(vald) + 1)}
            column = [(x, y) for x, y in grids.keys() if x == ends[v] and y > 1]
            if not any(grids[x].isalpha() for x in column):
                valid_grid.update({x: grids[x] for x in column})
                goals += [max(column)]
            if k[1] > 1:
                goals += [(x, 1) for x in vald]
                valid_grid.update({(k[0], y): grids[k[0], y] for y in range(1, k[1] + 1)})
            possibles = find_path(k, v, valid_grid, goals, total)
            for trial, steps in sorted(possibles.items(), key=lambda x: x[0][1] < 2):
                trial_grid = dict(grids.items())
                if column and trial == max(column):
                    trial_grid.pop(trial)
                else:
                    trial_grid[trial] = v
                trial_grid[k] = "."
                find_route(dict(trial_grid.items()), steps)


with open("input", "r") as file:
    data = file.read().splitlines()
    data = [x + " " * (len(data[0]) - len(x)) for x in data]
    grid = {
        (x, y): data[y][x]
        for x in range(len(data[0]))
        for y in range(len(data))
        if (data[y][x] == "." or data[y][x].isalpha())
    }
    adj = lambda x, y: ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
    cost = {"A": 1, "B": 10, "C": 100, "D": 1000}
    ends = {"A": 3, "B": 5, "C": 7, "D": 9}
    vald = [1, 2, 4, 6, 8, 10, 11]
    bests = []
    states = {}
    find_route(dict(grid.items()), 0)
    print(min(bests))
    bests = []
    states = {}
    data = data[:-2] + """  #D#C#B#A# #D#B#A#C#""".splitlines() + data[-2:]
    data = [x + " " * (len(data[0]) - len(x)) for x in data]
    grid = {
        (x, y): data[y][x]
        for x in range(len(data[0]))
        for y in range(len(data))
        if (data[y][x] == "." or data[y][x].isalpha())
    }
    find_route(dict(grid.items()), 0)
    print(min(bests))
