from graph import Graph

# Bellman_ford algorithm implementation for specific graph


def bellman_ford(graph: Graph) -> float:
    try:
        distance = [float("Inf")] * graph.verticesCount
        distance[Graph.source] = 0

        for _ in range(graph.verticesCount - 1):
            for edge in graph.graph:
                if distance[edge.start] != float("Inf") and distance[edge.start] + edge.weight < distance[edge.end]:
                    distance[edge.end] = distance[edge.start] + edge.weight

        for edge in graph.graph:
            if distance[edge.start] != float("Inf") and distance[edge.start] + edge.weight < distance[edge.end]:
                print()
                print("Graph contains negative weight cycle, which is not allowed")
                return 0
        return distance
    except:
        print()
        print("JSON file should contain info for each vertex")
        return 0


def print_solution(graph: Graph,result):
    if result:
        print("")
        print("-" * (len(result) * 8 + 30))
        print("|           VERTEX           |   ", end="")
        for vertex in graph.vertices:
            print(f"{vertex}   |   ", end="")
        print("")
        print("-" * (len(result) * 8 + 30))
        print("|  DISTANCE FROM THE SOURCE  |   ", end="")
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
        print()
        print("-" * (len(result) * 8 + 30))
        print()



