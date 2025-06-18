import numpy as np
import matplotlib.pyplot as plt


shape = np.array([
    [0, 0],
    [2, 0],
    [1, 2],
    [0, 0]  
])

def shear(shape, shx=0, shy=0):
    """Fungsi untuk melakukan shear (geser)"""
    shear_matrix = np.array([
        [1, shx],
        [shy, 1]
    ])
    return shape @ shear_matrix


shx = 1.0  
shy = 0.0  


sheared_shape = shear(shape, shx, shy)


plt.figure(figsize=(6, 6))
plt.plot(shape[:, 0], shape[:, 1], 'bo-', label='Asli')
plt.plot(sheared_shape[:, 0], sheared_shape[:, 1], 'ro--', label=f'Shear (shx={shx}, shy={shy})')

plt.title("Transformasi Shear (Geser) 2D")
plt.legend()
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.gca().set_aspect('equal')
plt.show()
