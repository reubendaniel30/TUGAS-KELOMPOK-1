import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


vertices = np.array([[0, 0, 0],
                     [1, 0, 0],
                     [1, 1, 0],
                     [0, 1, 0],
                     [0, 0, 1],
                     [1, 0, 1],
                     [1, 1, 1],
                     [0, 1, 1]])


faces = [[0, 1, 2, 3],
         [4, 5, 6, 7],
         [0, 1, 5, 4],
         [2, 3, 7, 6],
         [1, 2, 6, 5],
         [0, 3, 7, 4]]


def orthographic_projection(vertices, axis='z'):
    projection = vertices.copy()
    if axis == 'z':
        projection[:, 2] = 0
    elif axis == 'x':
        projection[:, 0] = 0
    elif axis == 'y':
        projection[:, 1] = 0
    return projection


projected_vertices = orthographic_projection(vertices, axis='z')


fig, ax = plt.subplots()
for face in faces:
    face_vertices = projected_vertices[face]
    poly = plt.Polygon(face_vertices[:, :2], edgecolor='black', facecolor='skyblue', alpha=0.5)
    ax.add_patch(poly)

ax.set_xlim(-0.5, 1.5)
ax.set_ylim(-0.5, 1.5)
ax.set_aspect('equal')
plt.title("Orthographic Projection (XY plane)")
plt.grid(True)
plt.show()
