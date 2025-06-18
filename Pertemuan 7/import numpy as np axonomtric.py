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


def axonometric_projection(points):
    
    angle_x = np.radians(35.264)  
    angle_y = np.radians(45)      

    
    Rx = np.array([
        [1, 0, 0],
        [0, np.cos(angle_x), -np.sin(angle_x)],
        [0, np.sin(angle_x), np.cos(angle_x)]
    ])

    
    Ry = np.array([
        [np.cos(angle_y), 0, np.sin(angle_y)],
        [0, 1, 0],
        [-np.sin(angle_y), 0, np.cos(angle_y)]
    ])

    
    R = Rx @ Ry

    
    projected = points @ R.T
    return projected[:, :2]


projected_vertices = axonometric_projection(vertices)


plt.figure(figsize=(6, 6))
for edge in edges:
    p1, p2 = projected_vertices[edge[0]], projected_vertices[edge[1]]
    plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'k')

plt.gca().set_aspect('equal')
plt.title("Axonometric Projection (Isometric)")
plt.grid(True)
plt.show()
