from graph import Graph

# Bellman_ford algorithm implementation for specific graph


def bellman_ford(graph: Graph) -> float:

    distance = [float("Inf")] * graph.verticesCount
    distance[Graph.source] = 0

    for _ in range(graph.verticesCount - 1):
        for edge in graph.graph:
            if distance[edge.start] != float("Inf") and distance[edge.start] + edge.weight < distance[edge.end]:
                distance[edge.end] = distance[edge.start] + edge.weight

    for edge in graph.graph:
        if distance[edge.start] != float("Inf") and distance[edge.start] + edge.weight < distance[edge.end]:
            print("Graf zawiera cykl o łącznej ujemnej wadze")
            return 0
    return distance


def print_solution(graph: Graph,result):

    print("")
    print("-" * (len(result) * 8 + 24))
    print("| WIERZCHOŁEK          |   ",end="")
    for vertex in sorted(graph.vertices):
        print(f"{vertex}   |   ", end="")
    print("")
    print("-" * (len(result) * 8 + 24))
    print("| ODLEGŁOŚĆ OD ŹRÓDŁA  |   ", end="")
    for res in result:
        if res < 0:
            print(f"\b{res}   |   ", end="")
            continue
        if res < 10:
            print(f"{res}   |   ", end="")
            continue
        if res < 100:
            print(f"{res}  |   ", end="")
            continue
        if res < 1000:
            print(f"\b{res}  |   ", end="")
            continue
    print("")
    print("-" * (len(result) * 8 + 24))



