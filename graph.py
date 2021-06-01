from edge import Edge

# class to represent whole graph


class Graph:

    verticesCount = 0
    source = 0

    def __init__(self):
        self.graph = []
        self.vertices = []

    def add_edge(self, e: Edge):
        self.graph.append(e)
        if not len(self.graph):
            Graph.source = e.start
        if not e.start in self.vertices:
            self.vertices.append(e.start)
            Graph.verticesCount += 1
        if not e.end in self.vertices:
            self.vertices.append(e.end)
            Graph.verticesCount += 1
        self.vertices = sorted(self.vertices)

    def print(self):
        for edge in self.graph:
            print(f"{edge.start} -> {edge.end} w: {edge.weight}")

