from polynomos.graphnomos.callables import BaseCallable
from polynomos.graphnomos.graph import SimpleGraphObject

__all__ = [
    "CycleGraph",
    "CompleteBipartiteGraph"
]

class CycleGraph(BaseCallable):
    '''
    Generate a cycle graph of n vertices
    '''
    def eval(n: int):
        if n <= 2:
            raise ValueError("You cannot generate cycles of length <= 2")
        vertices = [i + 1 for i in range(n)]
        edges = [sorted([i + 1, ((i + 1) % n) + 1]) for i in range(n)]
        return SimpleGraphObject(vertices, edges)
    
class CompleteBipartiteGraph(BaseCallable):
    '''
    Generate a complete bipartite graph K_{m, n}, where m, n are the lengths of 
    the two parties on either side
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