import numpy as np
import matplotlib.pyplot as plt

# Titik-titik 3D dari kubus
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

# Sisi-sisi kubus (edge pairs)
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  # dasar
    (4, 5), (5, 6), (6, 7), (7, 4),  # atas
    (0, 4), (1, 5), (2, 6), (3, 7)   # tiang
]

# Fungsi proyeksi oblique
def oblique_projection(points, angle_deg=45, scale=1):
    angle_rad = np.radians(angle_deg)

    # Matriks proyeksi oblique (2D)
    projection_matrix = np.array([
        [1, 0, scale * np.cos(angle_rad)],
        [0, 1, scale * np.sin(angle_rad)]
    ])

    # Kalikan titik 3D dengan matriks proyeksi → hasil: titik 2D
    projected = points @ projection_matrix.T
    return projected

# Cavalier (scale=1), Cabinet (scale=0.5)
projections = {
    "Cavalier (45°, scale=1)": oblique_projection(vertices, 45, 1),
    "Cabinet (63.4°, scale=0.5)": oblique_projection(vertices, 63.4, 0.5)
}

# Gambar kedua proyeksi
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

for ax, (title, proj_vertices) in zip(axs, projections.items()):
    for edge in edges:
        p1, p2 = proj_vertices[edge[0]], proj_vertices[edge[1]]
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], 'k')
    ax.set_aspect('equal')
    ax.set_title(title)
    ax.grid(True)

plt.tight_layout()
plt.show()
