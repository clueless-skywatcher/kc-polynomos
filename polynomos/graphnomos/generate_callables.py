from polynomos.graphnomos.callables import BaseCallable
from polynomos.graphnomos.graph import SimpleGraphObject

__all__ = [
    "CycleGraph"
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
