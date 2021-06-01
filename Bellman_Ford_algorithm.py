from graph import Graph

# Bellman_ford algorithm implementation for specific graph


def bellman_ford(graph: Graph):
    try:
        distance = dict()
        predecessor = dict()
        for i in graph.vertices:
            distance[i] = float("Inf")
            predecessor[i] = -1
        distance[Graph.source] = 0
        predecessor[Graph.source] = -1

        for _ in range(graph.verticesCount - 1):
            for edge in graph.graph:
                if distance[edge.start] != float("Inf") and distance[edge.start] + edge.weight < distance[edge.end]:
                    distance[edge.end] = distance[edge.start] + edge.weight
                    predecessor[edge.end] = edge.start

        for edge in graph.graph:
            if distance[edge.start] != float("Inf") and distance[edge.start] + edge.weight < distance[edge.end]:
                print()
                print("Graph contains negative weight cycle, which is not allowed")
                return 0
        return distance, predecessor
    except:
        print()
        print("JSON file should contain info for each vertex")
        return 0


def print_solution(res):
    result = res[0]
    pred = res[1]
    if result:
        print("")
        print("-" * (len(result) * 8 + 30))
        print("|           VERTEX           |   ", end="")
        for vertex in result:
            print(f"{vertex}   |   ", end="")
        print("")
        print("-" * (len(result) * 8 + 30))
        print("|  DISTANCE FROM THE SOURCE  |   ", end="")
        for key in result:
            if result[key] < 0:
                print(f"\b{result[key]}   |   ", end="")
                continue
            if result[key] < 10:
                print(f"{result[key]}   |   ", end="")
                continue
            if result[key] < 100:
                print(f"{result[key]}  |   ", end="")
                continue
            if result[key] < 1000:
                print(f"\b{result[key]}  |   ", end="")
                continue
        print()
        print("-" * (len(result) * 8 + 30))
        print("|         PREDECESSOR        |   ", end="")
        for key in pred:
            if pred[key] < 0:
                print(f"    |   ", end="")
                continue
            if pred[key] < 10:
                print(f"{pred[key]}   |   ", end="")
                continue
            if pred[key] < 100:
                print(f"{pred[key]}  |   ", end="")
                continue
            if pred[key] < 1000:
                print(f"\b{pred[key]}  |   ", end="")
                continue
        print()
        print("-" * (len(result) * 8 + 30))
        print()



