from polynomos.base_callable import BaseCallable
from polynomos.graphnomos.draw import fruchterman_reingold_layout, fruchterman_reingold_plot
from polynomos.graphnomos.graph import SimpleGraphObject

__all__ = [
    "FruchtermanReingoldLayout",
    "DrawGraph"
]

class FruchtermanReingoldLayout(BaseCallable):
    def eval(g: SimpleGraphObject):
        return fruchterman_reingold_layout(g)

class DrawGraph(BaseCallable):
    def eval(g, pos = None, layout = 'fruchterman_reingold'):
        if layout == 'fruchterman_reingold':
            fruchterman_reingold_plot(g)
