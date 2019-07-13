
class dense_graph:
    def __init__(self, v, direct):
        self.v = v
        self.direct = direct
        self.edges = []

        for i in range(v):
            self.edges.append([])
            for _ in range(v):
                self.edges[i].append(0)
    

    def add_edge(self, a, b):
        self.edges[a][b] = 1
        if not self.direct :
            self.edges[b][a] = 1

    def print(self):
        print("  ", end = " ") 
        [print(i, end = " ") for i in range(self.v)]
        print()

        for i in range(self.v):
            print(i, end = " :")
            [print(self.edges[i][j], end = " ") for j in range(self.v)]
            print()

    class iter:
        def __init__(self, graph, v):
            self.graph = graph
            self.v = v
        
        def __iter__(self):
            self.index = -1
            return self
        
        def __next__(self):
            self.index = self.index + 1
            while self.index < self.graph.v and self.graph.edges[self.v][self.index] == 0:
                self.index = self.index + 1
            
            if self.index == self.graph.v:
                raise StopIteration
            
            return self.index
