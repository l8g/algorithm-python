
class sparse_graph:

    def __init__(self, v, direct):
        self.v = v
        self.direct = direct
        self.edges = []
        for _ in range(v):
            self.edges.append([])

    def add_edge(self, a, b):
        self.edges[a] = self.edges[a] or []
        self.edges[a].append(b)
        if not self.direct:
            self.edges[b] = self.edges[b] or []
            self.edges[b].append(a)

    def print(self):
        for j in range(self.v):
            it = iter(sparse_graph.iter(self, j))
            print(j, end = ": ")
            [print(i, end = " ") for i in it]
            print()
            
    class iter:
        def __init__(self, graph, v):
            self.v = v
            self.graph = graph

        def __iter__(self):
            self.index = -1
            return self

        def __next__(self):
            self.index = self.index + 1
            if self.index < len(self.graph.edges[self.v]):
                return self.graph.edges[self.v][self.index]
            else :
                raise StopIteration

    
