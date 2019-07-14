
import sys
sys.path.append(".")

from graph.sparse_graph import sparse_graph
# import graph.dense_graph
from graph.dense_graph import dense_graph

from graph.component import component

graph =  sparse_graph(10, False)

graph.add_edge(0, 2)
graph.add_edge(0, 3)
graph.add_edge(0, 4)
graph.add_edge(0, 5)

graph.print()


graph = dense_graph(10, False)

graph.add_edge(0, 2)
graph.add_edge(0, 3)
graph.add_edge(0, 4)
graph.add_edge(0, 5)

graph.print()

comp = component(graph)

print(comp.ccount)