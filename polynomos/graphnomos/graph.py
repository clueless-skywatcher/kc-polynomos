from typing import List

class GraphVertex:
    def __init__(self, label) -> None:
        self.label = label

    def __str__(self) -> str:
        return f"GraphVertex({self.label})"
    
    def __hash__(self) -> int:
        return hash(self.label)
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, GraphVertex):
            return False
        return self.label == other.label
    
    def __ne__(self, other) -> bool:
        return not self.__eq__(other)
    
    def __gt__(self, other):
        if not isinstance(other, GraphVertex):
            return False
        return self.label > other.label
    
    def __lt__(self, other):
        if not isinstance(other, GraphVertex):
            return False
        return self.label < other.label
    
    def __repr__(self) -> str:
        return str(self)

class GraphEdge:
    def __init__(self, v1: GraphVertex, v2: GraphVertex, weight = None) -> None:
        self.v1 = v1
        self.v2 = v2
        self.weight = weight
        
    def __eq__(self, other):
        if not isinstance(other, GraphEdge):
            return False
        return sorted([self.v1, self.v2]) == sorted([other.v1, other.v2])
    
    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self) -> str:
        return f"GraphEdge({str(self.v1)}-{str(self.weight) if self.weight is not None else ''}-{str(self.v2)})"
    
    def __repr__(self) -> str:
        return str(self)
    
    def __hash__(self) -> int:
        return hash(tuple(sorted([self.v1, self.v2])))

class SimpleGraphObject:
    def __init__(self, vertices: List, edges: List = None, **properties) -> None:
        if all([isinstance(x, (int, str)) for x in vertices]):
            self._vertices = set([GraphVertex(x) for x in vertices])
        else:
            self._vertices = set(vertices)
        self._edges = set()
        if edges is not None:
            for edge in edges:
                if len(edge) == 3:
                    self._edges.add(GraphEdge(GraphVertex(edge[0]), GraphVertex(edge[1]), weight=edge[2]))
                else:
                    self._edges.add(GraphEdge(GraphVertex(edge[0]), GraphVertex(edge[1])))

        
        self._construct_label_map()
        self._construct_adj_matrix()
        self._properties = properties

    def set_property(self, **properties):
        self._properties = properties

    def get_property(self, property):
        return self._properties.get(property, None)

    def _construct_label_map(self):
        self._label_map = {vertex.label: i + 1 for i, vertex in enumerate(sorted(list(self._vertices)))}
        self._reverse_label_map = {i + 1: vertex.label for i, vertex in enumerate(sorted(list(self._vertices)))}

    def __str__(self) -> str:
        return f"{self.__class__.__name__}{tuple([str(edge) for edge in self._edges])}"
    
    def _construct_adj_matrix(self):
        self._adj_matrix = [[0] * len(self._vertices) for _ in range(len(self._vertices))] 
        for edge in self._edges:
            i = self._label_map[edge.v1.label] - 1
            j = self._label_map[edge.v2.label] - 1
            
            self._adj_matrix[i][j] = 1
            self._adj_matrix[j][i] = 1
            
    def __repr__(self) -> str:
        return str(self)
    
    @staticmethod
    def _from_adjacency_matrix(adj_matrix, labels = None):
        if labels is None:
            labels = [i + 1 for i in range(len(adj_matrix))]
        
        vertices = labels
        edges = []

        for i in range(len(adj_matrix)):
            for j in range(len(adj_matrix[0])):
                vertex_i = vertices[i]
                vertex_j = vertices[j]

                if adj_matrix[i][j] == 1 and sorted([vertex_i, vertex_j]) not in edges:
                    edges.append(sorted([vertex_i, vertex_j]))

        return SimpleGraphObject(vertices, edges)
    
    @staticmethod
    def _from_adjacency_list(adj_list: dict):
        vertices = [GraphVertex(i) for i in adj_list.keys()]
        edges = []

        for u in adj_list:
            for v in adj_list[u]:
                if sorted([u, v]) not in edges:
                    edges.append(sorted([u, v]))

        return SimpleGraphObject(vertices, edges)
    
    def get_degree_sequence(self, do_sort=False):
        degrees = []
        for row in self._adj_matrix:
            degrees.append(sum(row))
        
        if do_sort:
            degrees = sorted(degrees, reverse=True)

        return degrees
    
    def get_degree(self, vertex: int|str|GraphVertex):
        if isinstance(vertex, str):
            if vertex not in self._label_map:
                raise ValueError(f"{vertex} not present in graph")
            i = self._label_map[vertex] - 1
            return sum(self._adj_matrix[i])
        elif isinstance(vertex, int):
            if GraphVertex(vertex) not in self._vertices:
                raise ValueError(f"{vertex} not present in graph")
            return sum(self._adj_matrix[vertex - 1])
        else:
            if vertex not in self._vertices:
                raise ValueError(f"{vertex.label} not present in graph")
            i = self._label_map[vertex.label] - 1
            return sum(self._adj_matrix[i])
    
    def get_edges(self):
        return self._edges
    
    def get_vertices(self):
        return self._vertices
    
    def _get_adj_matrix(self, as_numpy = False):
        if as_numpy:
            import numpy as np
            return np.array(self._adj_matrix)
        return self._adj_matrix
    
    def add_edge(self, edge: List):
        if edge[0] > edge[1]:
            edge[0], edge[1] = edge[1], edge[0]
        edge_wt = None
        if len(edge) == 3:
            edge_wt = edge[2]
        v1 = GraphVertex(edge[0])
        v2 = GraphVertex(edge[1])

        if v1 not in self._vertices:
            self._vertices.add(v1)
        if v2 not in self._vertices:
            self._vertices.add(v2)

        self._edges.add(GraphEdge(v1, v2, weight=edge_wt))
        self._construct_label_map()
        self._construct_adj_matrix()

    def remove_edge(self, edge: List, add_weight_mode=False):
        if edge[0] > edge[1]:
            edge[0], edge[1] = edge[1], edge[0]
        
        v1 = GraphVertex(edge[0])
        v2 = GraphVertex(edge[1])

        if v1 not in self._vertices:
            raise ValueError(f"{v1.label} not present in graph")
        if v2 not in self._vertices:
            raise ValueError(f"{v2.label} not present in graph")
        
        self._edges.remove(GraphEdge(v1, v2))
        if add_weight_mode == False:
            self._construct_label_map()
            self._construct_adj_matrix()

    def add_vertex(self, vertex: int | str):
        v = GraphVertex(vertex)

        if v not in self._vertices:
            self._vertices.add(v)

        self._construct_label_map()
        self._construct_adj_matrix()
