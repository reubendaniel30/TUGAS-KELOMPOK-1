import numpy as np
import matplotlib.pyplot as plt


shape = np.array([
    [0, 0],
    [2, 0],
    [1, 2],
    [0, 0]  
])

def rotate(shape, angle_deg):
    """Fungsi untuk merotasi bentuk terhadap titik asal (0,0)"""
    angle_rad = np.radians(angle_deg)
    rotation_matrix = np.array([
        [np.cos(angle_rad), -np.sin(angle_rad)],
        [np.sin(angle_rad),  np.cos(angle_rad)]
    ])
    return shape @ rotation_matrix


rotated_shape = rotate(shape, angle_deg=45)


plt.figure(figsize=(6, 6))
plt.plot(shape[:, 0], shape[:, 1], 'bo-', label='Asli')
plt.plot(rotated_shape[:, 0], rotated_shape[:, 1], 'ro--', label='Setelah Rotasi 45°')

plt.title("Rotasi Geometri 2D")
plt.legend()
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.gca().set_aspect('equal')
plt.show()
