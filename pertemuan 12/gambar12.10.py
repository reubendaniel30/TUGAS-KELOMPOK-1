import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter([2], [2], [2], color='red', label='Camera')
ax.text(2,2,2,'Camera', color='red')

ax.scatter([0], [0], [0], color='blue', label='Interest Point')
ax.text(0,0,0,'Interest', color='blue')

ax.quiver(2, 2, 2, -2, -2, -2, length=1, color='purple', label='View Direction')

ax.set_xlim([-1,3])
ax.set_ylim([-1,3])
ax.set_zlim([-1,3])
ax.set_title('Camera Point of View')
ax.legend()
plt.show()
