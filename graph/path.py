
class path:

    def __init__(self, graph, s):
        self.s = s
        self.graph = graph
        self.prev = [-1 for _ in range(graph.v)]
        self.visited = [False for _ in range(graph.v)]

        for i in range(graph.v):
            if not self.visited[i]:
                self._dfs(i)

    
    def _dfs(self, v):
        self.visited[v] = True
        it = iter(self.graph.iter(self.graph, v))

        for j in it:
            if not self.visited[j]:
                self._dfs(j)
                self.prev[j] = v


    def has_path(self, v):
        return self.visited[v]

    def get_path(self, v):
        if not self.has_path(v):
            return None
        path = []

        i = v

        while self.prev[i] != -1:
            path.insert(0, i)
            i = self.prev[i]
        return path
        
    def show_path(self, v):
        path = self.get_path(v)
        if path :
            print(self.s, "->", end = "")
            for i in path:
                print(i, end = "")
                if i != v:
                    print("->", end = "")

