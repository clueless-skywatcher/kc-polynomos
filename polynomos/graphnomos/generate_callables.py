from polynomos.graphnomos.callables import BaseCallable
from polynomos.graphnomos.graph import SimpleGraphObject
from polynomos.graphnomos.callables import AddEdges, SimpleGraphFromMatrix

__all__ = [
    "CycleGraph",
    "CompleteGraph",
    "CompleteBipartiteGraph",
    "LCFGraph",
    "DodecahedralGraph",
    "PetersenGraph"
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
        return SimpleGraphFromMatrix([
            [0,0,0,0,0,0,0,1,1,1],
            [0,0,0,0,0,1,1,0,0,1],
            [0,0,0,0,1,0,1,0,1,0],
            [0,0,0,0,1,1,0,1,0,0],
            [0,0,1,1,0,0,0,0,0,1],
            [0,1,0,1,0,0,0,0,1,0],
            [0,1,1,0,0,0,0,1,0,0],
            [1,0,0,1,0,0,1,0,0,0],
            [1,0,1,0,0,1,0,0,0,0],
            [1,1,0,0,1,0,0,0,0,0]
        ])
