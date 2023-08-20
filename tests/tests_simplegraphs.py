import unittest

import sys

sys.path.insert(0, "../../kc-polynomos")
sys.path.insert(0, "../kc-polynomos")

from polynomos.graphnomos.all import *
from polynomos.graphnomos.graph import GraphEdge, GraphVertex

class TestGraphs(unittest.TestCase):
    def test_init(self):
        g1 = SimpleGraph(vertices = [1, 2, 3, 4, 5], edges = [
            [1, 2],
            [1, 3],
            [2, 3],
            [1, 5],
            [3, 4]
        ])
        self.assertEqual(GraphVertices(g1), set([GraphVertex(i) for i in [1, 2, 3, 4, 5]]))
        self.assertEqual(GraphEdges(g1), set([
            GraphEdge(GraphVertex(1), GraphVertex(2)),
            GraphEdge(GraphVertex(1), GraphVertex(3)),
            GraphEdge(GraphVertex(2), GraphVertex(3)),
            GraphEdge(GraphVertex(1), GraphVertex(5)),
            GraphEdge(GraphVertex(3), GraphVertex(4)),
        ]))

    def test_adjacency_matrix(self):
        g1 = SimpleGraph(vertices = [1, 2, 3, 4, 5], edges = [
            [1, 2],
            [1, 3],
            [2, 3],
            [1, 5],
            [3, 4]
        ])
        self.assertEqual(AdjacencyMatrix(g1), [
            [0, 1, 1, 0, 1], 
            [1, 0, 1, 0, 0], 
            [1, 1, 0, 1, 0], 
            [0, 0, 1, 0, 0], 
            [1, 0, 0, 0, 0], 
        ])

        g2 = SimpleGraphFromMatrix([
            [0, 1, 1, 0, 1], 
            [1, 0, 1, 0, 0], 
            [1, 1, 0, 1, 0], 
            [0, 0, 1, 0, 0], 
            [1, 0, 0, 0, 0],
        ])
        self.assertEqual(AdjacencyMatrix(g1), AdjacencyMatrix(g2))

        g3 = SimpleGraph(
                vertices = ['A', 'B', 'C', 'D', 'E'], 
                edges = [
                    ['A', 'B'],
                    ['A', 'C'],
                    ['B', 'C'],
                    ['A', 'E'],
                    ['C', 'D']
                ]
            )
        
        self.assertEqual(AdjacencyMatrix(g3), AdjacencyMatrix(g1))
        self.assertEqual(AdjacencyMatrix(g2), AdjacencyMatrix(g3))

    def test_adjacency_list(self):
        g1 = SimpleGraphFromList({
            1: [2, 3, 5],
            2: [3],
            3: [2, 4],
            4: [3],
            5: [1]
        })

        self.assertEqual(GraphVertices(g1), set([GraphVertex(i) for i in [1, 2, 3, 4, 5]]))
        self.assertEqual(GraphEdges(g1), set([
            GraphEdge(GraphVertex(1), GraphVertex(2)),
            GraphEdge(GraphVertex(1), GraphVertex(3)),
            GraphEdge(GraphVertex(2), GraphVertex(3)),
            GraphEdge(GraphVertex(1), GraphVertex(5)),
            GraphEdge(GraphVertex(3), GraphVertex(4)),
        ]))

        g2 = SimpleGraph(
                vertices = ['A', 'B', 'C', 'D', 'E'], 
                edges = [
                    ['A', 'B'],
                    ['A', 'C'],
                    ['B', 'C'],
                    ['A', 'E'],
                    ['C', 'D']
                ]
            )
        
        g3 = SimpleGraphFromMatrix([
            [0, 1, 1, 0, 1], 
            [1, 0, 1, 0, 0], 
            [1, 1, 0, 1, 0], 
            [0, 0, 1, 0, 0], 
            [1, 0, 0, 0, 0],
        ])

        self.assertEqual(AdjacencyMatrix(g1), AdjacencyMatrix(g2))
        self.assertEqual(AdjacencyMatrix(g2), AdjacencyMatrix(g3))
        self.assertEqual(AdjacencyMatrix(g3), AdjacencyMatrix(g1))

    def test_counts(self):
        g1 = SimpleGraphFromList({
            1: [2, 3, 5],
            2: [3],
            3: [2, 4],
            4: [3],
            5: [1]
        })
        self.assertEqual(VertexCount(g1), 5)
        self.assertEqual(EdgeCount(g1), 5)

        g2 = SimpleGraph(
                vertices = ['A', 'B', 'C', 'D', 'E'], 
                edges = [
                    ['A', 'B'],
                    ['A', 'C'],
                    ['B', 'C'],
                    ['A', 'E'],
                    ['C', 'D']
                ]
            )   
        self.assertEqual(VertexCount(g2), 5)
        self.assertEqual(EdgeCount(g2), 5)

    def test_add_edge(self):
        g1 = SimpleGraph(vertices = [1, 2, 3, 4, 5], edges = [
            [1, 2],
            [1, 3],
            [2, 3],
            [1, 5],
            [3, 4]
        ])
        AddEdge(g1, [2, 4])
        self.assertEqual(VertexCount(g1), 5)
        self.assertEqual(EdgeCount(g1), 6)
        self.assertEqual(AdjacencyMatrix(g1), [
            [0, 1, 1, 0, 1], 
            [1, 0, 1, 1, 0], 
            [1, 1, 0, 1, 0], 
            [0, 1, 1, 0, 0], 
            [1, 0, 0, 0, 0], 
        ])

        AddEdge(g1, [3, 6])
        self.assertEqual(VertexCount(g1), 6)
        self.assertEqual(EdgeCount(g1), 7)
        self.assertEqual(AdjacencyMatrix(g1), [
            [0, 1, 1, 0, 1, 0], 
            [1, 0, 1, 1, 0, 0], 
            [1, 1, 0, 1, 0, 1], 
            [0, 1, 1, 0, 0, 0], 
            [1, 0, 0, 0, 0, 0], 
            [0, 0, 1, 0, 0, 0], 
        ])

        AddEdge(g1, [4, 2])
        self.assertEqual(VertexCount(g1), 6)
        self.assertEqual(EdgeCount(g1), 7)
        self.assertEqual(AdjacencyMatrix(g1), [
            [0, 1, 1, 0, 1, 0], 
            [1, 0, 1, 1, 0, 0], 
            [1, 1, 0, 1, 0, 1], 
            [0, 1, 1, 0, 0, 0], 
            [1, 0, 0, 0, 0, 0], 
            [0, 0, 1, 0, 0, 0], 
        ])


    def test_multiple_edges(self):
        g1 = SimpleGraph(vertices = [1, 2, 3, 4, 5], edges = [
            [1, 2],
            [1, 3],
            [2, 3],
            [1, 5],
            [3, 4]
        ])
        AddEdges(g1, [
            [2, 4],
            [2, 5],
            [3, 5]
        ])
        self.assertEqual(VertexCount(g1), 5)
        self.assertEqual(EdgeCount(g1), 8)
        self.assertEqual(AdjacencyMatrix(g1), [
            [0, 1, 1, 0, 1], 
            [1, 0, 1, 1, 1], 
            [1, 1, 0, 1, 1], 
            [0, 1, 1, 0, 0], 
            [1, 1, 1, 0, 0]
        ])

    def test_add_vertices(self):
        g1 = SimpleGraph(vertices = [1, 2, 3, 4, 5], edges = [
            [1, 2],
            [1, 3],
            [2, 3],
            [1, 5],
            [3, 4]
        ])
        AddVertex(g1, 6)
        self.assertEqual(VertexCount(g1), 6)
        self.assertEqual(EdgeCount(g1), 5)
        self.assertEqual(AdjacencyMatrix(g1), [
            [0, 1, 1, 0, 1, 0], 
            [1, 0, 1, 0, 0, 0], 
            [1, 1, 0, 1, 0, 0], 
            [0, 0, 1, 0, 0, 0], 
            [1, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0] 
        ])

        AddVertices(g1, [3, 7, 8])
        self.assertEqual(VertexCount(g1), 8)
        self.assertEqual(EdgeCount(g1), 5)
        self.assertEqual(AdjacencyMatrix(g1), [
            [0, 1, 1, 0, 1, 0, 0, 0], 
            [1, 0, 1, 0, 0, 0, 0, 0], 
            [1, 1, 0, 1, 0, 0, 0, 0], 
            [0, 0, 1, 0, 0, 0, 0, 0], 
            [1, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0]
        ])


if __name__ == '__main__':
    unittest.main()