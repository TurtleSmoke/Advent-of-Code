#!/usr/bin/env python

import networkx as nx

input_file = "input"

data = [x.strip().split("-") for x in open(input_file).readlines()]

graph = nx.Graph()
for x, y in data:
    graph.add_edge(x, y)

print(
    len([clique for clique in nx.enumerate_all_cliques(graph) if len(clique) == 3 and any(c[0] == "t" for c in clique)])
)
print(",".join(sorted([clique for clique in nx.enumerate_all_cliques(graph)][-1])))
