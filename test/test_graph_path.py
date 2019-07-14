
import sys
sys.path.append(".")

from graph.sparse_graph import sparse_graph
from graph.path import path



graph = sparse_graph(7, False)

graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(0, 5)
graph.add_edge(0, 6)
graph.add_edge(5, 3)
graph.add_edge(5, 4)
graph.add_edge(3, 4)
graph.add_edge(6, 4)

p = path(graph, 0)
p.show_path(6)

