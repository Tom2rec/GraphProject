from graph import Graph
from edge import Edge
import json
from collections import namedtuple

# class to read JSON representation of graph


def edge_decoder(e):

    return namedtuple('X', e.keys())(*e.values())


def graph_creator(g: Graph):

    with open("graph.json") as json_file:
        edges = json.load(json_file, object_hook=edge_decoder)
        for edge in edges:
            e = Edge(edge.start, edge.end, edge.weight)
            g.add_edge(e)
