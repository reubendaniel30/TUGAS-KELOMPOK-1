import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


points = np.array([
    [0.2, 0.0],
    [0.3, 0.3],
    [0.1, 0.6],
    [0.4, 0.9],
    [0.2, 1.2],
    [0.3, 1.5],
    [0.2, 1.8]
])

r_profile = points[:, 0]
z_profile = points[:, 1]

z = np.linspace(z_profile.min(), z_profile.max(), 300)
r = np.interp(z, z_profile, r_profile)

theta = np.linspace(0, 2*np.pi, 100)
theta, z = np.meshgrid(theta, z)
r = np.interp(z, points[:,1], points[:,0])
x = r * np.cos(theta)
y = r * np.sin(theta)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, color='navy')

for px, pz in zip(points[:,0], points[:,1]):
    ax.scatter(px, 0, pz, color='red')

ax.set_title("Lathe Object - Linear Spline")

plt.show()
