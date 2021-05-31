from graph import Graph
from readJSON import graph_creator
from Bellman_Ford_algorithm import bellman_ford, print_solution

graph = Graph()
graph_creator(graph)
print_solution(graph,bellman_ford(graph))