#!/usr/bin/env python
import itertools
import math

import networkx as nx

input_file = "input"

input_graph = nx.from_edgelist(
    itertools.chain(
        *(
            itertools.product([src], dsts.split())
            for src, dsts in [line.strip().split(":") for line in open(input_file)]
        )
    )
)


def split_graph(graph):
    graph.remove_edges_from(nx.minimum_edge_cut(graph))
    return nx.connected_components(graph)


print(math.prod(map(len, split_graph(input_graph))))
