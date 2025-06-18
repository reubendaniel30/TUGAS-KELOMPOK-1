import numpy as np
import matplotlib.pyplot as plt


shape = np.array([
    [0, 0],
    [2, 0],
    [1, 2],
    [0, 0]  
])

def translate(shape, tx, ty):
    """Fungsi untuk translasi (pergeseran posisi)"""
    translation_vector = np.array([tx, ty])
    return shape + translation_vector


translated_shape = translate(shape, tx=3, ty=1)


plt.figure(figsize=(6, 6))
plt.plot(shape[:, 0], shape[:, 1], 'bo-', label='Asli')
plt.plot(translated_shape[:, 0], translated_shape[:, 1], 'ro--', label='Hasil Translasi')

plt.title("Translasi Geometri 2D")
plt.legend()
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.gca().set_aspect('equal')
plt.show()
