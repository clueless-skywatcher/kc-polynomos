from collections import Counter

from polynomos.base_callable import BaseCallable
from polynomos.graphnomos.graph import SimpleGraphObject, GraphVertex

__all__ = [
    'AddEdge',
    'AddEdges',
    'AddVertex',
    'AddVertices',
    'AdjacencyMatrix',
    'DegreeFrequency',
    'DegreeMap',
    'DegreeSequence',
    'EdgeCount',
    'GraphEdges',
    'GraphVertices',
    'KRegularQ',
    'Regularity',
    'RegularQ',
    'SimpleGraph',
    'SimpleGraphFromList',
    'SimpleGraphFromMatrix',
    'VertexCount',
    'VertexDegree'
]

class SimpleGraph(BaseCallable):
    '''
    SimpleGraph(vertices: list[int|string], edges: list[list[int|string]])
    ---------------------------------------------------------------------------------
    Generate a simple graph from a list of edges and vertices
    
    Arguments:
    - vertices: list of integers/strings\n
        The vertex labels of the graph
    - edges (optional): list of lists of 2 integers/strings\n
        The edges of the graph, each represented as a list of 2 
        vertex labels

    Returns:\n
    A SimpleGraphObject representing the graph
    '''
    def eval(vertices = None, edges = None):
        if vertices is None and edges is None:
            raise ValueError("Both vertices and edges cannot be None")
        if edges is None:
            edges = set()

        return SimpleGraphObject(vertices, edges)
    
class SimpleGraphFromMatrix(BaseCallable):
    '''
    SimpleGraphFromMatrix(adjacency_matrix: list[list[int]], vertices: None/list[any])
    ---------------------------------------------------------------------------------
    Generate a graph from a given adjacency matrix
    
    Arguments:
    - adjacency_matrix: n x n list of lists of 0s and 1s\n
        The adjacency matrix of the graph
    - vertices (optional): list of strings or integers\n
        The vertex labels of the graph. If nothing is provided, 
        1, 2, ..., n is inferred, where n is the length of the adjacency matrix

    Returns:\n
    A SimpleGraphObject representing the graph constructed from the adjacency matrix
    '''
    def eval(adjacency_matrix, vertices = None):
        if vertices is None:
            vertices = [i + 1 for i in range(len(adjacency_matrix))]
        
        return SimpleGraphObject._from_adjacency_matrix(adjacency_matrix, labels=vertices)

class SimpleGraphFromList(BaseCallable):
    '''
    SimpleGraphFromList(adj_list: dict[any, list[any]])
    --------------------------------------------------
    Generate a graph from a given adjacency list
    
    Arguments:
    - adj_list: dict, mapping keys/integers to lists of keys/integers\n
        Adjacency List of the graph, mapping vertices to a list of other vertices 
        that are connected to the vertex.

    Returns:\n
    A SimpleGraphObject representing the graph constructed from the adjacency list
    '''
    def eval(adj_list):
        return SimpleGraphObject._from_adjacency_list(adj_list)
    
class GraphVertices(BaseCallable):
    '''
    GraphVertices(graph: SimpleGraphObject)
    --------------------------------------------------
    Return the vertices in the graph
    
    Arguments:
    - graph: SimpleGraphObject\n
        A SimpleGraphObject representing the graph
    
    Returns:\n
    A list of GraphVertex objects that each denote a vertex of the graph
    '''
    def eval(graph):
        if not isinstance(graph, SimpleGraphObject):
            raise TypeError("Input must be a graph")
        return graph.get_vertices()
    
class GraphEdges(BaseCallable):
    '''
    GraphEdges(graph: SimpleGraphObject)
    --------------------------------------------------
    Return the edges in the graph
    
    Arguments:
    - graph: SimpleGraphObject\n
        A SimpleGraphObject representing the graph
    
    Returns:\n
    A list of GraphEdge objects that each denote an edge of the graph
    '''
    def eval(graph):
        if not isinstance(graph, SimpleGraphObject):
            raise TypeError("Input must be a graph")
        return graph.get_edges()
    
class AdjacencyMatrix(BaseCallable):
    '''
    AdjacencyMatrix(graph: SimpleGraphObject)
    --------------------------------------------------
    Return the edges in the graph
    
    Arguments:
    - graph: SimpleGraphObject\n
        A SimpleGraphObject representing the graph
    
    Returns:\n
    A list of lists of 1's and 0's representing the adjacency matrix
    of the graph
    '''
    def eval(graph, as_numpy = False):
        if isinstance(graph, SimpleGraphObject):
            return graph._get_adj_matrix(as_numpy = as_numpy)

        return NotImplemented
    
class VertexCount(BaseCallable):
    '''
    VertexCount(graph: SimpleGraphObject)
    --------------------------------------------------
    Return the number of vertices in the graph
    
    Arguments:
    - graph: SimpleGraphObject\n
        A SimpleGraphObject representing the graph
    
    Returns:\n
    An integer equal to the number of vertices
    '''
    def eval(graph: SimpleGraphObject):
        return len(GraphVertices(graph))
    
class EdgeCount(BaseCallable):
    '''
    EdgeCount(graph: SimpleGraphObject)
    --------------------------------------------------
    Return the number of edges in the graph
    
    Arguments:
    - graph: SimpleGraphObject\n
        A SimpleGraphObject representing the graph
    
    Returns:\n
    An integer equal to the number of edges
    '''
    def eval(graph: SimpleGraphObject):
        return len(GraphEdges(graph))
    
class AddEdge(BaseCallable):
    '''
    AddEdge(graph: SimpleGraphObject, edge: list[int|string])
    --------------------------------------------------
    Add an edge to a given graph
    
    Arguments:
    - graph: SimpleGraphObject\n
        A SimpleGraphObject representing the graph
    - edge: list of 2 integers or strings
        A list representing the edge, with list elements representing
        the ends of the edge
    
    Returns:\n
    None. Only an edge is added to the given graph
    '''
    def eval(graph: SimpleGraphObject, edge: list):
        graph.add_edge(edge)

class AddEdges(BaseCallable):
    '''
    AddEdges(graph: SimpleGraphObject, edge: list[list[int|string]])
    --------------------------------------------------
    Add one or more edges to a given graph from a given list
    
    Arguments:
    - graph: SimpleGraphObject\n
        A SimpleGraphObject representing the graph
    - edge: list of 2 integers or strings
        A list representing the edge, with list elements representing
        the ends of the edge
    
    Returns:\n
    None. Only an edge is added to the given graph
    '''
    def eval(graph: SimpleGraphObject, edges: list):
        for edge in edges:
            graph.add_edge(edge)

class AddVertex(BaseCallable):
    '''
    AddVertex(graph: SimpleGraphObject, vertex: int|str)
    --------------------------------------------------
    Add a vertex to the given graph
    
    Arguments:
    - graph: SimpleGraphObject\n
        A SimpleGraphObject representing the graph
    - vertex: integer or string\n
        The label of the vertex to be added

    Returns:\n
    None. Only a vertex is added to the graph. Nothing happens
    if the given vertex already exists in the graph
    '''
    def eval(graph: SimpleGraphObject, vertex: int|str):
        graph.add_vertex(vertex)

class AddVertices(BaseCallable):
    '''
    AddVertices(graph: SimpleGraphObject, vertices: list[int|str])
    --------------------------------------------------
    Add a list of vertices to the given graph
    
    Arguments:
    - graph: SimpleGraphObject\n
        A SimpleGraphObject representing the graph
    - vertices: list of integers or strings\n
        The labels of the vertices to be added

    Returns:\n
    None. Only the given vertices are added to the graph.
    '''
    def eval(graph: SimpleGraphObject, vertices: list[int|str]):
        for vertex in vertices:
            graph.add_vertex(vertex)

class DegreeSequence(BaseCallable):
    '''
    DegreeSequence(graph: SimpleGraphObject, do_sort=True)
    ----------------------------------------
    Return the degree sequence of the graph

    Arguments:
    - graph: SimpleGraphObject\n
        A SimpleGraphObject representing the graph
    - do_sort: boolean (defaults to False)\n
        A boolean specifying whether to sort the degree list 
        in a non-increasing order

    Returns:\n
    A list of degrees (in non-increasing order if `do_sort` is `True`)
    '''
    def eval(graph: SimpleGraphObject, do_sort=True):
        return graph.get_degree_sequence(do_sort=do_sort)
    
class VertexDegree(BaseCallable):
    '''
    VertexDegree(graph: SimpleGraphObject, vertex: int|string)
    ----------------------------------------
    Return the degree of a given vertex in a graph

    Arguments:
    - graph: SimpleGraphObject\n
        A SimpleGraphObject representing the graph
    - vertex: int or string\n
        The label of the vertex we are interested in

    Returns:\n
    The degree of the vertex as an integer
    '''
    def eval(graph: SimpleGraphObject, vertex: int|str):
        return graph.get_degree(vertex)
    
class DegreeMap(BaseCallable):
    '''
    DegreeMap(graph: SimpleGraphObject)
    -----------------------------------
    Return a map, associating each vertex with its degree

    Arguments:
    - graph: SimpleGraphObject\n
        A SimpleGraphObject representing the graph

    Returns:\n
    A dict mapping each vertex label to its degree
    '''
    def eval(graph: SimpleGraphObject):
        d_map = {}
        for vertex in GraphVertices(graph):
            d_map[vertex.label] = VertexDegree(graph, vertex)

        return d_map
    
class DegreeFrequency(BaseCallable):
    '''
    DegreeFrequency(graph: SimpleGraphObject)
    -----------------------------------
    Return a map, containing the frequencies of degrees in the graph

    Arguments:
    - graph: SimpleGraphObject\n
        A SimpleGraphObject representing the graph

    Returns:\n
    A dict mapping each degree to its frequency
    '''
    def eval(graph: SimpleGraphObject):
        d_freq = Counter(DegreeSequence(graph))
        return dict(d_freq)
    
class RegularQ(BaseCallable):
    '''
    RegularQ(graph: SimpleGraphObject)
    -----------------------------------
    Determines whether the given graph is regular, i.e. each
    vertex is connected to the same number of vertices

    Arguments:
    - graph: SimpleGraphObject\n
        A SimpleGraphObject representing the graph

    Returns:\n
    True if the graph is regular, False otherwise
    '''
    def eval(graph: SimpleGraphObject):
        deg_freq = DegreeFrequency(graph)
        for degree in deg_freq:
            if deg_freq[degree] == VertexCount(graph):
                return True
        return False
    
class KRegularQ(BaseCallable):
    '''
    KRegularQ(graph: SimpleGraphObject)
    -----------------------------------
    Determines whether the given graph is k-regular, i.e each
    vertex is connected to exactly k other vertices

    Arguments:
    - graph: SimpleGraphObject\n
        A SimpleGraphObject representing the graph
    - k: int
        The value of k for which k-regularity is to be checked

    Returns:\n
    True if the graph is k-regular, False otherwise
    '''
    def eval(graph: SimpleGraphObject, k: int):
        deg_freq = DegreeFrequency(graph)
        for degree in deg_freq:
            if deg_freq[degree] == VertexCount(graph) and degree == k:
                return True
        return False
    
class Regularity(BaseCallable):
    '''
    Regularity(graph: SimpleGraphObject)
    ------------------------------------
    Returns the value of k if the given graph is k-regular

    Arguments:
    - graph: SimpleGraphObject\n
        A SimpleGraphObject representing the graph

    Returns:
    An integer representing the value of k for which the graph
    is k-regular, or -1 if the graph is not regular
    '''
    def eval(graph: SimpleGraphObject):
        deg_freq = DegreeFrequency(graph)
        for degree in deg_freq:
            if deg_freq[degree] == VertexCount(graph):
                return degree
        return -1