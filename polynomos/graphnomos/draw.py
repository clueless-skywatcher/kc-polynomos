import math
import random

import numpy as np

import matplotlib.pyplot as plt
import matplotlib.patches as pch

from polynomos.graphnomos.graph import SimpleGraphObject

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

def fruchterman_reingold_plot(g: SimpleGraphObject):
    points = fruchterman_reingold_layout(g)
    # Draw edges
    for edge in g.get_edges():
        x1, y1 = points[edge.v1]
        x2, y2 = points[edge.v2]
        plt.plot([x1, x2], [y1, y2], 'k-', lw=1, zorder=1)

    # Draw nodes
    for node, pos in points.items():
        plt.scatter(pos[0], pos[1], color='orange', marker='o', s=500, zorder=2)
        plt.text(pos[0], pos[1], str(node.label), fontsize=12, ha='center', va='center')
    
    plt.axis('off')
    plt.show()
    