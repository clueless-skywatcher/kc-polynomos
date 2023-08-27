from polynomos.graphnomos.callables import BaseCallable, GraphEdges, GraphNeighbours, SimpleGraphFromList
from polynomos.graphnomos.graph import SimpleGraphObject
from polynomos.graphnomos.callables import (
    AddEdges, 
    GraphVertices
)

__all__ = [
    'CycleGraph',
    'CompleteGraph',
    'CompleteBipartiteGraph',
    'LCFGraph',
    'Mycielskian',
    'DodecahedralGraph',
    'PetersenGraph'
]

class CycleGraph(BaseCallable):
    '''
    CycleGraph(n: int)
    -----------------
    Generate a cycle graph of n vertices

    Can be best visualized with CircularLayout
    
    Arguments:
    - n: integer
        Number of vertices in the graph

    Returns:
    A SimpleGraphObject representing the graph C_n
    '''
    def eval(n: int):
        if n <= 2:
            raise ValueError("You cannot generate cycles of length <= 2")
        vertices = [i + 1 for i in range(n)]
        edges = [sorted([i + 1, ((i + 1) % n) + 1]) for i in range(n)]
        return SimpleGraphObject(vertices, edges)
    
class CompleteBipartiteGraph(BaseCallable):
    '''
    CompleteBipartiteGraph(m: int, n: int)
    -------------------------------------
    Generate a complete bipartite graph K_{m, n}, where m, n are the lengths of 
    the two parties on either side

    Can be best visualized with BipartiteLayout

    Arguments:
    - m: integer
        Number of vertices on left-hand side
    - n: integer
        Number of vertices on right-hand side

    Returns:
    A SimpleGraphObject representing the graph K_{m, n}
    '''
    def eval(m: int, n: int):
        if m < 1 or n < 1:
            raise ValueError("Both parties should have at least 1 vertex")
        
        vertices = [i for i in range(1, m + n + 1)]
        party_1 = vertices[:m]
        party_2 = vertices[m:m + n]

        edges = []

        for v1 in party_1:
            for v2 in party_2:
                edges.append(sorted([v1, v2]))

        return SimpleGraphObject(vertices, edges, bipartite_parties = [party_1, party_2])
    
class CompleteGraph(BaseCallable):
    '''
    CompleteGraph(m: int)
    -------------------------------------
    Generate a complete graph K_m where all vertices are connected by an edge

    Can be best visualized with CircularLayout

    Arguments:
    - m: integer
        Number of vertices in the graph

    Returns:
    A SimpleGraphObject representing the graph K_m
    '''
    def eval(m: int):
        if m < 2:
            raise ValueError("Complete graphs have at least 2 vertices")
        vertices = [i + 1 for i in range(m)]

        edges = []

        for i in range(1, m + 1):
            for j in range(1, m + 1):
                if i < j:
                    edges.append([i, j])

        return SimpleGraphObject(vertices, edges)
    
class LCFGraph(BaseCallable):
    '''
    LCFGraph(n: int, shifts: list[int], repetitions: int)
    -------------------------------------
    Generate a graph using a given LCF notation.

    The Lederberg-Coxeter-Frucht (or LCF, in short) notation is used for
    cubic (or 3-regular) graphs that have a Hamiltonian cycle. We take in a list
    of integers `shifts`, and an integer `n`. The `n` nodes are arranged in a cycle,
    then the remaining third edge from each node is joined according to the `shifts`
    (1st vertex in the cycle is joined to `shifts[0]` vertices after vertex 1, 2nd 
    vertex in the cycle is joined to `shifts[1]` vertices after vertex, and so on)
    The vertices are chosen clockwise if positive, counter-clockwise if negative.

    Can be best visualized with CircularLayout

    Arguments:
    - n: integer\n
        Number of vertices in the graph
    - shifts: list of integers\n
        Shift for each vertex. Keep in mind, length of shift * repetitions = number of vertices
    - repetitions: integer\n
        How many times the given shift sequence is to be repeated

    Returns:
    A SimpleGraphObject representing the graph generated from the LCF notation
    '''
    def eval(n: int, shifts: list[int], repetitions: int = 1):
        if n != len(shifts) * repetitions:
            raise ValueError("Number of vertices should be equal to length of shifts * number of repetitions")

        shifts = shifts * repetitions
        g = CycleGraph(n)

        additional_edges = []
        vertices = list(g.get_vertices())

        for i in range(n):
            label = vertices[i].label
            shifted_label = vertices[(i + shifts[i]) % n].label

            additional_edges.append([label, shifted_label])
        
        AddEdges(g, additional_edges)
        return g
    
class DodecahedralGraph(BaseCallable):
    '''
    DodecahedralGraph()
    -------------------------------------
    Generate the dodecahedral graph of 20 vertices. LCF notation has
    been used for the generation

    Arguments:
    - m: integer
        Number of vertices in the graph

    Returns:
    A SimpleGraphObject representing the dodecahedral graph
    '''
    def eval():
        return LCFGraph(20, [10, 7, 4, -4, -7, 10, -4, 7, -7,4], 2)

class PetersenGraph(BaseCallable):
    '''
    PetersenGraph()
    -------------------------------------
    Generate the famous Petersen Graph

    Returns:
    A SimpleGraphObject representing the Petersen Graph
    '''
    def eval():
        return SimpleGraphFromList({
            1: [3, 4, 6],
            2: [4, 5, 7],
            3: [1, 5, 8],
            4: [1, 2, 9],
            5: [2, 3, 10],
            6: [1, 7, 10],
            7: [2, 6, 8],
            8: [3, 7, 9],
            9: [4, 8, 10],
            10: [5, 6, 9]
        })

class Mycielskian(BaseCallable):
    '''
    Mycielskian(graph: SimpleGraphObject, u_label_prefix: str = None, v_label: str = None)
    -------------------------------------
    Generate the Mycielskian of a given graph.

    The Mycielskian of an undirected graph is a larger graph
    that preserves triangle-freedom, i.e. if the original graph
    doesn't have triangles, it's Mycielskian won't have triangles
    as well, and it will if the original graph has triangles.
    Construction is fairly simple: 
        1) Take a new set of vertices, equal to the number of vertices 
        in the original graph + 1, label them u_1, u_2, ..., u_n, v, 
        where n is the number of original vertices. 
        2) Connect each u_i to all the neighbours of v_i
        3) Connect the v to all the u_i.

    Note: The original labels in the graph are lost and are renamed to
    1, 2, ..., n

    Arguments:
    - graph: SimpleGraphObject
        The graph whose Mycielskian is to be generated
    - u_label_prefix: str or None (optional)
        Prefix to be assigned to the new 'u' vertices. If None,
        it just assigns numbers. Defaults to None.
        E.g: If u_label_prefix = 'u', then the new vertices will
        be labeled 'u1', 'u2', etc.
    - v_label: str or None (optional)
        Label to be assigned to the new 'v' vertex. If None,
        it just assigns a number. Defaults to None.
        E.g: If v_label = 'v', then the new vertex will
        be labeled 'v'

    Returns:
    A SimpleGraphObject representing the Mycielskian of the graph
    '''
    def eval(graph: SimpleGraphObject, u_label_prefix: str|None = None, v_label: str|None = None):
        vertices = GraphVertices(graph)
        new_labels = sorted([graph._label_map[v.label] for v in vertices])

        u_labels = [i for i in range(1, len(vertices) + 1)]
        if u_label_prefix is not None:
            u_labels = [u_label_prefix + str(label) for label in u_labels]
        else:
            u_labels = [new_labels[-1] + label for label in u_labels]
        
        v = 2 * len(vertices) + 1
        if v_label is not None:
            v = v_label

        edges = [[edge.v1, edge.v2] for edge in GraphEdges(graph)]
        for i in range(len(edges)):
            edge = edges[i]
            edge_label1 = graph._label_map[edge[0].label]
            edge_label2 = graph._label_map[edge[1].label]
            edges[i] = [edge_label1, edge_label2]

        for label, u_label in zip(new_labels, u_labels):
            neighbours = [graph._label_map[neighbour] for neighbour in GraphNeighbours(graph, label)]
            for neighbour in neighbours:
                edges.append(
                    [u_label, neighbour]
                )
        
        for u_label in u_labels:
            edges.append(
                [u_label, v]
            )

        return SimpleGraphObject(new_labels + u_labels + [v], edges)