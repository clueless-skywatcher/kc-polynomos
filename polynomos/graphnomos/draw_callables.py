import random

from polynomos.base_callable import BaseCallable
from polynomos.graphnomos.draw import draw_graph, fruchterman_reingold_layout, bipartite_layout
from polynomos.graphnomos.graph import GraphVertex, SimpleGraphObject

__all__ = [
    "DrawGraph",
    "BipartiteLayout",
    "FruchtermanReingoldLayout",
]

class FruchtermanReingoldLayout(BaseCallable):
    def eval(g: SimpleGraphObject):
        return fruchterman_reingold_layout(g)

class DrawGraph(BaseCallable):
    def eval(g, pos = None, layout = 'fruchterman_reingold'):
        draw_graph(g, points=pos, algorithm=layout)

class BipartiteLayout(BaseCallable):
    def eval(g: SimpleGraphObject, first_partition = None):
        return bipartite_layout(g, first_partition)
