import matplotlib.pyplot as plt
import numpy as np
radius = 5
center_x, center_y = 0,0

angels = np.linspace(0, 2*np.pi, 8, endpoint=False)
x_points = center_x + radius * np.cos(angels)
y_points = center_y + radius * np.sin(angels)

circle = plt.Circle ((center_x, center_y), radius, fill=False, linestyle='--', color="blue")
fig, ax = plt.subplots()
ax.add_artist(circle)

ax.plot(x_points, y_points, "ro")

ax.set_aspect("equal")
ax.set_xlim(-radius-1, radius+1)
ax.set_ylim(-radius-1, radius+1)
ax.grid(True)
plt.title("Lingkaran dan 8 Titik Simetris")
plt.show()