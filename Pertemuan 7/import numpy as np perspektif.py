import numpy as np
import matplotlib.pyplot as plt


vertices = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
    [0, 1, 1]
])


edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  
    (4, 5), (5, 6), (6, 7), (7, 4),  
    (0, 4), (1, 5), (2, 6), (3, 7)   
]


def perspective_projection(points, d=2.5):
    projected = []
    for x, y, z in points:
        
        z_offset = z + 1e-5 if z == d else z
        factor = d / (d + z_offset)  
        x_p = x * factor
        y_p = y * factor
        projected.append([x_p, y_p])
    return np.array(projected)


projected_vertices = perspective_projection(vertices, d=3)


plt.figure(figsize=(6, 6))
for edge in edges:
    p1, p2 = projected_vertices[edge[0]], projected_vertices[edge[1]]
    plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'k')

plt.title("Perspective Projection")
plt.gca().set_aspect('equal')
plt.grid(True)
plt.show()
