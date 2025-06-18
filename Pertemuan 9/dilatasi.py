import numpy as np
import matplotlib.pyplot as plt


shape = np.array([
    [0, 0],
    [2, 0],
    [1, 2],
    [0, 0]  
])

def dilate(shape, sx, sy):
    """Fungsi untuk melakukan dilatasi (skalasi) terhadap titik asal"""
    scaling_matrix = np.array([
        [sx, 0],
        [0, sy]
    ])
    return shape @ scaling_matrix


sx = 2  
sy = 1.5  


dilated_shape = dilate(shape, sx, sy)


plt.figure(figsize=(6, 6))
plt.plot(shape[:, 0], shape[:, 1], 'bo-', label='Asli')
plt.plot(dilated_shape[:, 0], dilated_shape[:, 1], 'ro--', label=f'Dilatasi ({sx}, {sy})')

plt.title("Dilatasi (Skalasi) Geometri 2D")
plt.legend()
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.gca().set_aspect('equal')
plt.show()
