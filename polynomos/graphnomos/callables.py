from polynomos.base_callable import BaseCallable

from polynomos.graphnomos.graph import SimpleGraphObject, GraphVertex

__all__ = [
    "SimpleGraph",
    "SimpleGraphFromMatrix",
    "SimpleGraphFromList",
    "AdjacencyMatrix",
    "GraphEdges",
    "GraphVertices",
    "VertexCount",
    "EdgeCount",
    "AddEdge",
    "AddEdges"
]

class SimpleGraph(BaseCallable):
    def eval(vertices = None, edges = None):
        if vertices is None and edges is None:
            raise ValueError("Both vertices and edges cannot be None")
        if edges is None:
            edges = set()

        return SimpleGraphObject(vertices, edges)
    
class SimpleGraphFromMatrix(BaseCallable):
    def eval(adjacency_matrix, vertices = None):
        if vertices is None:
            vertices = [i + 1 for i in range(len(adjacency_matrix))]
        
        return SimpleGraphObject._from_adjacency_matrix(adjacency_matrix, labels=vertices)

class SimpleGraphFromList(BaseCallable):
    def eval(adj_list):
        return SimpleGraphObject._from_adjacency_list(adj_list)
    
class GraphVertices(BaseCallable):
    def eval(graph):
        if not isinstance(graph, SimpleGraphObject):
            raise TypeError("Input must be a graph")
        return graph.get_vertices()
    
class GraphEdges(BaseCallable):
    def eval(graph):
        if not isinstance(graph, SimpleGraphObject):
            raise TypeError("Input must be a graph")
        return graph.get_edges()
    
class AdjacencyMatrix(BaseCallable):
    def eval(graph, as_numpy = False):
        if isinstance(graph, SimpleGraphObject):
            return graph._get_adj_matrix(as_numpy = as_numpy)

        return NotImplemented
    
class VertexCount(BaseCallable):
    def eval(graph: SimpleGraphObject):
        return len(graph.get_vertices())
    
class EdgeCount(BaseCallable):
    def eval(graph: SimpleGraphObject):
        return len(graph.get_edges())
    
class AddEdge(BaseCallable):
    def eval(graph: SimpleGraphObject, edge: list):
        graph.add_edge(edge)

class AddEdges(BaseCallable):
    def eval(graph: SimpleGraphObject, edges: list):
        for edge in edges:
            graph.add_edge(edge)