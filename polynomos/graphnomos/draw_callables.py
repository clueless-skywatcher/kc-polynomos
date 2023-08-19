import random

from polynomos.base_callable import BaseCallable
from polynomos.graphnomos.draw import (
    draw_graph, fruchterman_reingold_layout, bipartite_layout,
    circular_layout
)
from polynomos.graphnomos.graph import GraphVertex, SimpleGraphObject

__all__ = [
    "DrawGraph",
    "CircularLayout",
    "BipartiteLayout",
    "FruchtermanReingoldLayout",
]

class FruchtermanReingoldLayout(BaseCallable):
    '''
    FruchtermanReingoldLayout(g: SimpleGraphObject)
    ---------------------------------------------------------------------------------
    Use the Fruchterman-Reingold Force-Directed drawing algorithm to calculate
    the coordinates of vertices of a given graph to be as aesthetically pleasing 
    as possible when drawn on a plot.

    The Fruchterman-Reingold algorithm involves calculating attractive and repulsive
    forces between a system of vertices (treated as real-life objects) and finding the 
    positions of vertices where the forces are balanced out and the system is at an 
    equilibrium.
    
    Arguments: \n
    - g: SimpleGraphObject
    The graph whose point coordinates need to be calculated

    Returns:\n
    A dict of GraphVertex-(x, y) tuple mappings denoting the optimal position of 
    each vertex

    References:\n
    - [1] https://dcc.fceia.unr.edu.ar/sites/default/files/uploads/materias/fruchterman.pdf
    (Graph Drawing by Force–Directed Placement by THOMAS M. J. FRUCHTERMAN AND EDWARD M. REINGOLD)
    Easy to implement from the paper, but code has been corrected with some modifications 
    and ChatGPT as deemed suitable
    '''
    def eval(g: SimpleGraphObject):
        return fruchterman_reingold_layout(g)

class DrawGraph(BaseCallable):
    '''
    DrawGraph(pos: dict[GraphVertex, tuple[float]], layout: string)
    ---------------------------------------------------------------------------------
    Draw the graph on a matplotlib plot using given position map, 
    or a given layout algorithm
    
    Arguments: \n
    - Either: \n
        pos: dict mapping GraphVertex objects to positions 
            (tuples with (x, y) values)\n
        The dictionary of positions of the graph vertices
    - Or: \n
        layout: string\n
        Algorithm for drawing the graph layout. Can be either of\n
        1. "fruchterman_reingold" (Default): Uses the Fruchterman-Reingold Force-Directed
        Algorithm\n
        2. "bipartite": Uses a bipartite layout algorithm, best suited for drawing
        bipartite graphs

    Returns:\n
    None. Opens up a Matplotlib window (or plot in iPython Notebook) showing the graph
    plot.
    '''
    def eval(g, pos = None, layout = 'fruchterman_reingold'):
        draw_graph(g, points=pos, algorithm=layout)

class BipartiteLayout(BaseCallable):
    '''
    BipartiteLayout(g: SimpleGraphObject)
    ---------------------------------------------------------------------------------
    Calculate the coordinates of vertices, with a given list of vertices on the left
    and the remaining vertices on the right. Best used for bipartite graphs.
    
    Arguments: \n
    - g: SimpleGraphObject\n
    The graph whose point coordinates need to be calculated
    - first_partition: list of integers/strings or None\n
    The vertices that are to be drawn on the left. If None, first_partition is chosen
    to be any number of vertices from 2 to n - 1, or if the graph has "bipartite_parties" in its properties
    (usually when creating bipartite graphs), it will take the first element in the "bipartite_parties"
    value to be used as the first_partition.

    Raises: \n
    ValueError: When first_partition contains a vertex not in the given graph

    Returns:\n
    A dict of GraphVertex-(x, y) tuple mappings denoting the optimal position of 
    each vertex

    References:\n
    - [1] nx.bipartite_layout() function in NetworkX Graph Library. The NX-version uses numpy but
    here it is implemented from scratch as much as possible.
    '''
    def eval(g: SimpleGraphObject, first_partition = None):
        return bipartite_layout(g, first_partition)
    
class CircularLayout(BaseCallable):
    '''
    CircularLayout(g: SimpleGraphObject)
    ---------------------------------------------------------------------------------
    Calculate the coordinates of vertices of given graph arranged in a circle
    
    Arguments: \n
    - g: SimpleGraphObject\n
    The graph whose point coordinates need to be calculated
    
    Returns:\n
    A dict of GraphVertex-(x, y) tuple mappings denoting the optimal position of 
    each vertex

    References:\n
    - [1] nx.circular_layout() function in NetworkX Graph Library. The NX-version uses numpy but
    here it is implemented from scratch as much as possible.
    '''
    def eval(g: SimpleGraphObject):
        return circular_layout(g)