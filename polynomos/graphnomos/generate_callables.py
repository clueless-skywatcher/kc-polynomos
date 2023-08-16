from polynomos.graphnomos.callables import BaseCallable
from polynomos.graphnomos.graph import SimpleGraphObject

__all__ = [
    "CycleGraph",
    "CompleteGraph",
    "CompleteBipartiteGraph"
]

class CycleGraph(BaseCallable):
    '''
    CycleGraph(n: int)
    -----------------
    Generate a cycle graph of n vertices
    
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