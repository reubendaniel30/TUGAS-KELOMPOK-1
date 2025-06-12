from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib import pyplot as plt
import numpy as np

u = np.linspace(0, np.pi, 30)
v = np.linspace(0, 2*np.pi, 30)
x = np.outer(np.sin(u), np.sin(v))
y = np.outer(np.sin(u), np.cos(v))
z = np.outer(np.cos(u), np.ones_like(v))

fig = plt.figure(figsize=(15,5))

# Wireframe
ax1 = fig.add_subplot(131, projection='3d')
ax1.plot_wireframe(x, y, z)
ax1.set_title('Wireframe Rendering')

# Hidden line (simulasi dengan semi-transparansi)
ax2 = fig.add_subplot(132, projection='3d')
ax2.plot_surface(x, y, z, color='gray', alpha=0.5, edgecolor='k')
ax2.set_title('Hidden Line Rendering')

# Shaded rendering
ax3 = fig.add_subplot(133, projection='3d')
ax3.plot_surface(x, y, z, color='orange')
ax3.set_title('Shaded Rendering')

plt.tight_layout()
plt.show()
