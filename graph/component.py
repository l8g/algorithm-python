

class component:

    def __init__(self, graph):
        self.graph = graph
        self.visited = [False for _ in range(graph.v)]
        self.ids = [-1 for _ in range(graph.v)]
        self.ccount = 0
        self.circle = False

        for v in range(graph.v):
            if not self.visited[v]:
                self.dfs(v)
                self.ccount = self.ccount + 1
                


    def dfs (self, v):
        self.visited[v] = True
        self.ids[v] = self.ccount
        it = iter(self.graph.iter(self.graph, v))
        for i in it:
            if not self.visited[i]:
                self.dfs(i)
            else:
                self.circle = True
                
    def count(self):
        return self.ccount

    def is_connected(self, a, b):
        return self.ids[a] == self.ids[b]

    def has_Circle(self):
        return self.circle

            
        


    

