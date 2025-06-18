import numpy as np
import matplotlib.pyplot as plt


shape = np.array([
    [0, 0],
    [1, 0],
    [0.5, 1],
    [0, 0] 
])

def translate(shape, tx, ty):
    
    translation_matrix = np.array([tx, ty])
    return shape + translation_matrix

def scale(shape, sx, sy):
    
    scaling_matrix = np.array([[sx, 0], [0, sy]])
    return shape @ scaling_matrix

def rotate(shape, angle_deg):
    
    angle_rad = np.radians(angle_deg)
    rotation_matrix = np.array([
        [np.cos(angle_rad), -np.sin(angle_rad)],
        [np.sin(angle_rad),  np.cos(angle_rad)]
    ])
    return shape @ rotation_matrix


translated = translate(shape, tx=2, ty=1)
scaled = scale(shape, sx=2, sy=2)
rotated = rotate(shape, angle_deg=45)


plt.figure(figsize=(10, 8))

plt.plot(shape[:, 0], shape[:, 1], 'k-', label='Asli')
plt.plot(translated[:, 0], translated[:, 1], 'r--', label='Translasi')
plt.plot(scaled[:, 0], scaled[:, 1], 'g--', label='Skala')
plt.plot(rotated[:, 0], rotated[:, 1], 'b--', label='Rotasi')

plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.legend()
plt.title("Transformasi Geometri 2D")
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
