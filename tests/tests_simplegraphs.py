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

    def test_degree(self):
        g1 = SimpleGraph(vertices = [1, 2, 3, 4, 5], edges = [
            [1, 2],
            [1, 3],
            [2, 3],
            [1, 5],
            [3, 4]
        ])
        self.assertEqual(VertexDegree(g1, 1), 3)
        self.assertEqual(VertexDegree(g1, 2), 2)
        self.assertEqual(VertexDegree(g1, 3), 3)
        self.assertEqual(VertexDegree(g1, 4), 1)
        self.assertEqual(VertexDegree(g1, 5), 1)

        g1 = SimpleGraph(vertices = ['A', 'B', 'C', 'D', 'E'], edges = [
            ['A', 'B'],
            ['A', 'C'],
            ['B', 'C'],
            ['A', 'E'],
            ['C', 'D']
        ])
        self.assertEqual(VertexDegree(g1, 'A'), 3)
        self.assertEqual(VertexDegree(g1, 'B'), 2)
        self.assertEqual(VertexDegree(g1, 'C'), 3)
        self.assertEqual(VertexDegree(g1, 'D'), 1)
        self.assertEqual(VertexDegree(g1, 'E'), 1)

        g1 = SimpleGraph(vertices = [1, 2, 3, 4, 5])
        for i in range(1, 6):
            self.assertEqual(VertexDegree(g1, i), 0)

    def test_degree_sequence(self):
        g1 = SimpleGraph(vertices = [1, 2, 3, 4, 5], edges = [
            [1, 2],
            [1, 3],
            [2, 3],
            [1, 5],
            [3, 4]
        ])
        self.assertEqual(DegreeSequence(g1, do_sort=False), [3, 2, 3, 1, 1])
        self.assertEqual(DegreeSequence(g1, do_sort=True), [3, 3, 2, 1, 1])

        g1 = SimpleGraph(vertices = [1, 2, 3, 4, 5])
        self.assertEqual(DegreeSequence(g1, do_sort=False), [0, 0, 0, 0, 0])

    def test_degree_map(self):
        g1 = SimpleGraph(vertices = [1, 2, 3, 4, 5], edges = [
            [1, 2],
            [1, 3],
            [2, 3],
            [1, 5],
            [3, 4]
        ])
        self.assertEqual(DegreeMap(g1), {1: 3, 2: 2, 3: 3, 4: 1, 5: 1})

        g1 = SimpleGraph(vertices = ['A', 'B', 'C', 'D', 'E'], edges = [
            ['A', 'B'],
            ['A', 'C'],
            ['B', 'C'],
            ['A', 'E'],
            ['C', 'D']
        ])
        self.assertEqual(DegreeMap(g1), {'A': 3, 'B': 2, 'C': 3, 'D': 1, 'E': 1})

    def test_degree_frequency(self):
        g1 = SimpleGraph(vertices = [1, 2, 3, 4, 5], edges = [
            [1, 2],
            [1, 3],
            [2, 3],
            [1, 5],
            [3, 4]
        ])
        self.assertEqual(DegreeFrequency(g1), {3: 2, 2: 1, 1: 2})

        petersen = PetersenGraph()
        self.assertEqual(DegreeFrequency(petersen), {3: 10})

    def test_regularq(self):
        g1 = SimpleGraph(vertices = [1, 2, 3, 4, 5], edges = [
            [1, 2],
            [1, 3],
            [2, 3],
            [1, 5],
            [3, 4]
        ])
        self.assertEqual(RegularQ(g1), False)
        self.assertEqual(KRegularQ(g1, 3), False)
        self.assertEqual(Regularity(g1), -1)
        
        petersen = PetersenGraph()
        self.assertEqual(RegularQ(petersen), True)
        self.assertEqual(KRegularQ(petersen, 3), True)
        self.assertEqual(Regularity(petersen), 3)

    def test_neighbours(self):
        g1 = SimpleGraph(vertices = [1, 2, 3, 4, 5], edges = [
            [1, 2],
            [1, 3],
            [2, 3],
            [1, 5],
            [3, 4]
        ])
        self.assertEqual(GraphNeighbours(g1, 1), {2, 3, 5})
        self.assertEqual(GraphNeighbours(g1, 2), {1, 3})
        self.assertEqual(GraphNeighbours(g1, 3), {1, 2, 4})
        self.assertEqual(GraphNeighbours(g1, 4), {3})
        self.assertEqual(GraphNeighbours(g1, 5), {1})
        self.assertEqual(GraphNeighbours(g1, GraphVertex(1)), {2, 3, 5})
        self.assertEqual(GraphNeighbours(g1, GraphVertex(2)), {1, 3})
        self.assertEqual(GraphNeighbours(g1, GraphVertex(3)), {1, 2, 4})
        self.assertEqual(GraphNeighbours(g1, GraphVertex(4)), {3})
        self.assertEqual(GraphNeighbours(g1, GraphVertex(5)), {1})


        g2 = SimpleGraph(vertices = ['A', 'B', 'C', 'D', 'E'], edges = [
            ['B', 'A'],
            ['A', 'C'],
            ['B', 'C'],
            ['A', 'E'],
            ['C', 'D']
        ])
        self.assertEqual(GraphNeighbours(g2, GraphVertex('A')), {'B', 'C', 'E'})
        self.assertEqual(GraphNeighbours(g2, GraphVertex('B')), {'A', 'C'})
        self.assertEqual(GraphNeighbours(g2, GraphVertex('C')), {'A', 'B', 'D'})
        self.assertEqual(GraphNeighbours(g2, GraphVertex('D')), {'C'})
        self.assertEqual(GraphNeighbours(g2, GraphVertex('E')), {'A'})

    def test_mycielskian(self):
        g1 = SimpleGraph(vertices = [1, 2, 3, 4], edges = [
            [1, 2],
            [2, 3],
            [3, 1],
            [4, 3]
        ])

        myc = Mycielskian(g1)
        self.assertEqual(GraphVertices(myc), set([GraphVertex(i + 1) for i in range(2 * len(GraphVertices(g1)) + 1)]))
        self.assertEqual(GraphEdges(myc), set(
            [GraphEdge(GraphVertex(edge[0]), GraphVertex(edge[1])) for edge in [
                [1, 2],
                [2, 3],
                [1, 3],
                [3, 4],
                [2, 5],
                [3, 5],
                [1, 6],
                [3, 6],
                [2, 7],
                [1, 7],
                [4, 7],
                [3, 8],
                [5, 9],
                [6, 9],
                [7, 9],
                [8, 9]
            ]])
        )
        self.assertEqual(VertexCount(myc), 2 * VertexCount(g1) + 1)
        self.assertEqual(EdgeCount(myc), 3 * EdgeCount(g1) + VertexCount(g1))



if __name__ == '__main__':
    unittest.main()