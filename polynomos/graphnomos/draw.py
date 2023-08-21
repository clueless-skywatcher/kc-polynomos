import math
import random

import numpy as np

import matplotlib.pyplot as plt
import matplotlib.patches as pch

from polynomos.graphnomos.graph import GraphVertex, SimpleGraphObject

def fruchterman_reingold_layout(g: SimpleGraphObject, 
    iterations = 50, 
    seed = None,
    optimal_distance = None
):
    def cool(temp, iterations):
        return temp * 0.975

    if seed is not None:
        random.seed(seed)

    # Initialize positions randomly
    positions = {vertex: (random.random(), random.random()) for vertex in g.get_vertices()}

    # Parameters
    width = 1.0
    height = 1.0
    if optimal_distance is None:
        optimal_distance = math.sqrt(width * height / len(g.get_vertices()))
    iterations_total = iterations
    temperature = width / 10.0

    for it in range(iterations):
        # Calculate repulsive forces
        displacements = {vertex: [0.0, 0.0] for vertex in g.get_vertices()}
        for v1 in g.get_vertices():
            for v2 in g.get_vertices():
                if v1 != v2:
                    delta_x = positions[v2][0] - positions[v1][0]
                    delta_y = positions[v2][1] - positions[v1][1]
                    
                    delta_dist = max(0.01, math.sqrt(delta_x ** 2 + delta_y ** 2))
                    repulsion = (optimal_distance ** 2) / delta_dist

                    displacement_x = (delta_x / delta_dist) * repulsion
                    displacement_y = (delta_y / delta_dist) * repulsion

                    displacements[v1][0] -= displacement_x
                    displacements[v1][1] -= displacement_y

        # Calculate attractive forces
        for edge in g.get_edges():
            delta_x = positions[edge.v1][0] - positions[edge.v2][0]
            delta_y = positions[edge.v1][1] - positions[edge.v2][1]
            
            delta_dist = max(0.01, math.sqrt(delta_x ** 2 + delta_y ** 2))
            attraction = (delta_dist ** 2) / optimal_distance

            displacement_x = (delta_x / delta_dist) * attraction
            displacement_y = (delta_y / delta_dist) * attraction

            displacements[edge.v1][0] -= displacement_x
            displacements[edge.v1][1] -= displacement_y
            displacements[edge.v2][0] += displacement_x
            displacements[edge.v2][1] += displacement_y

        # Update node positions
        for vertex in g.get_vertices():
            displacement = displacements[vertex]
            displacement_mag = max(0.01, math.sqrt(displacement[0] ** 2 + displacement[1] ** 2))
            
            # Apply displacement with temperature scaling
            displacement_x = (displacement[0] / displacement_mag) * min(displacement_mag, temperature)
            displacement_y = (displacement[1] / displacement_mag) * min(displacement_mag, temperature)

            # Update positions
            x, y = positions[vertex]
            x = min(width, max(-width, x + displacement_x))
            y = min(height, max(-height, y + displacement_y))
            positions[vertex] = (x, y)

        # Cool down temperature
        temperature = cool(temperature, it)

    return positions

def draw_graph(g: SimpleGraphObject, points = None, algorithm = "fruchterman_reingold"):
    if points is None:
        if algorithm == "fruchterman_reingold":
            points = fruchterman_reingold_layout(g)
        elif algorithm == "bipartite":
            points = bipartite_layout(g)
        else:
            raise ValueError("Either provide an algorithm or a dict of points for the graph")
    # Draw edges
    for edge in g.get_edges():
        x1, y1 = points[edge.v1]
        x2, y2 = points[edge.v2]

        plt.plot([x1, x2], [y1, y2], 'k-', lw=1, zorder=1)

        if edge.weight is not None:
            weight = edge.weight
            mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2

            plt.text(mid_x, mid_y, str(weight), fontsize=15, ha='center', va='center')

    # Draw nodes
    for node, pos in points.items():
        plt.scatter(pos[0], pos[1], color='orange', marker='o', s=500, zorder=2)
        plt.text(pos[0], pos[1], str(node.label), fontsize=12, ha='center', va='center')
    
    plt.axis('off')
    plt.show()

def bipartite_layout(g: SimpleGraphObject, first_partition: list = None):
    def rescale(positions):
        limit = 0
        y_max = -1
        x_max = -1

        len_pos = len(positions)

        x_mean = 0
        y_mean = 0

        for pos in positions:
            if positions[pos][0] > x_max:
                x_max = positions[pos][0]
            if positions[pos][1] > y_max:
                y_max = positions[pos][1]

            x_mean += positions[pos][0] / len_pos
            y_mean += positions[pos][1] / len_pos

            limit = max(limit, x_max, y_max)

        for pos in positions:
            positions[pos][0] -= x_mean
            positions[pos][1] -= y_mean
        
        if limit > 0:
            for pos in positions:
                positions[pos][0] *= 1 / limit
                positions[pos][1] *= 1 / limit

        return positions

    if first_partition is None:
        if g.get_property("bipartite_parties") is not None:
            first_partition = [GraphVertex(v) for v in g.get_property("bipartite_parties")[0]]
        else:
            first_partition = [GraphVertex(v) for v in range(1, random.randint(2, len(g.get_vertices())))]
    else:
        temp = []
        for v in first_partition:
            if GraphVertex(v) not in g.get_vertices():
                raise ValueError(f"Vertex {v} is not in the graph")
            else:
                temp.append(GraphVertex(v))
        first_partition = temp
        
    height = 1
    width = 4 / 3
    offset = (width / 2, height / 2)

    first_partition = set(first_partition)
    second_partition = g.get_vertices() - first_partition

    first_part_points = {
        vertex: [0, i * height] for i, vertex in enumerate(first_partition)
    }

    second_part_points = {
        vertex: [width, i * height] for i, vertex in enumerate(second_partition)
    }

    for pt in first_part_points:
        first_part_points[pt][0] -= offset[0]
        first_part_points[pt][1] -= offset[1]

    for pt in second_part_points:
        second_part_points[pt][0] -= offset[0]
        second_part_points[pt][1] -= offset[1]

    final_pts_dict = {}

    for pt in first_part_points:
        final_pts_dict[pt] = first_part_points[pt]

    for pt in second_part_points:
        final_pts_dict[pt] = second_part_points[pt]

    return rescale(final_pts_dict)

def circular_layout(g: SimpleGraphObject):
    center = (0, 0)

    vertices = g.get_vertices()
    
    if len(vertices) == 0:
        return {}
    elif len(vertices) == 1:
        return {
            list(vertices)[0]: center
        }
    else:
        thetas = [float(angle) * 2 * math.pi / len(vertices) for angle in range(len(vertices))]
        positions = {vertex: (math.cos(theta), math.sin(theta)) for vertex, theta in zip(vertices, thetas)}
        return positions
    
def shell_layout(g: SimpleGraphObject, shells: list[list[int]]):
    center = (0, 0)

    vertices = g.get_vertices()

    if len(vertices) == 0:
        return {}
    elif len(vertices) == 1:
        return {
            list(vertices)[0]: center
        }
    else:
        if len(shells[0]) == 1:
            radius = 0
        else:
            radius = 1.0 / len(shells)

        rotate = math.pi / len(shells)
        
        init_rotate = rotate

        positions = {}
        for shell in shells:
            thetas = (np.linspace(0, 2 * math.pi, len(shell), endpoint=False, dtype=np.float32) + init_rotate)
            positions.update(
                {
                    GraphVertex(vertex): (
                        radius * np.cos(theta) + center[0], 
                        radius * np.sin(theta) + center[1]
                    ) for vertex, theta in zip(shell, thetas)
                }
            )
            radius += 1.0 / (len(shells))
            init_rotate += rotate
        
        return positions