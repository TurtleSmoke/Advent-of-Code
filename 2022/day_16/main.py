#!/usr/bin/env python
import re

val_input = "input"

lines_infos = [re.findall(r"[A-Z][A-Z]|\d+", line) for line in open(val_input).read().splitlines()]

graph = {x[0]: set(x[1:]) for x in lines_infos}
flow = {x[0]: int(x[1]) for x in lines_infos if int(x[1]) != 0}
encoded_valves = {x: 1 << i for i, x in enumerate(flow)}
shortest_path = {x: {y: 1 if y in graph[x] else float("+inf") for y in graph} for x in graph}
for mid in shortest_path:
    for dst in shortest_path:
        for src in shortest_path:
            shortest_path[src][dst] = min(shortest_path[src][dst], shortest_path[src][mid] + shortest_path[mid][dst])


def dp(current, remaining_time, state, current_flow, res):
    res[state] = max(res.get(state, 0), current_flow)
    for dest in flow:
        time_after_dest = remaining_time - shortest_path[current][dest] - 1
        if encoded_valves[dest] & state or time_after_dest <= 0:
            continue
        dp(dest, time_after_dest, state | encoded_valves[dest], current_flow + time_after_dest * flow[dest], res)
    return res


visited1 = max(dp("AA", 30, 0, 0, {}).values())
print(visited1)
visited2 = dp("AA", 26, 0, 0, {})
print(max(v1 + v2 for k1, v1 in visited2.items() for k2, v2 in visited2.items() if not k1 & k2))
