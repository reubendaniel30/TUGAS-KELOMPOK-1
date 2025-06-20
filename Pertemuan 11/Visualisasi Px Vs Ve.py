import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
import matplotlib.patches as patches

# Set up the figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 8))
fig.suptitle('Gambar 11.1 Vektor dan Piksel', fontsize=16, fontweight='bold')

# Left subplot - Pixel representation
ax1.set_title('Pixel\n1957', fontsize=14, fontweight='bold')
ax1.set_xlabel('Picture Elements', fontsize=10)

# Create a pixelated/raster image effect
# Create a grid of pixels to simulate a pixelated image
pixel_size = 20
grid_x, grid_y = np.meshgrid(np.arange(0, 200, pixel_size), np.arange(0, 200, pixel_size))

# Create some pixel data to simulate an image
pixel_data = np.random.rand(len(grid_y), len(grid_x[0]))
for i in range(len(grid_y)):
    for j in range(len(grid_x[0])):
        color_intensity = pixel_data[i, j]
        if color_intensity > 0.7:
            color = 'black'
        elif color_intensity > 0.4:
            color = 'gray'
        else:
            color = 'lightgray'
        
        rect = Rectangle((j*pixel_size, i*pixel_size), pixel_size, pixel_size, 
                        facecolor=color, edgecolor='white', linewidth=0.5)
        ax1.add_patch(rect)

# Add "Px" text
ax1.text(100, 100, 'Px', fontsize=60, fontweight='bold', ha='center', va='center')

ax1.set_xlim(0, 200)
ax1.set_ylim(0, 200)
ax1.set_aspect('equal')
ax1.grid(True, alpha=0.3)

# Right subplot - Vector representation
ax2.set_title('Vector\n1960', fontsize=14, fontweight='bold')
ax2.set_xlabel('Line Primitive', fontsize=10)

# Create vector graphics (smooth curves and lines)
# Draw smooth curves using mathematical functions
t = np.linspace(0, 4*np.pi, 1000)
x1 = 50 + 30 * np.cos(t) + 10 * np.cos(3*t)
y1 = 50 + 30 * np.sin(t) + 10 * np.sin(3*t)

x2 = 150 + 40 * np.cos(t/2) + 15 * np.cos(2*t)
y2 = 150 + 40 * np.sin(t/2) + 15 * np.sin(2*t)

# Plot smooth vector curves
ax2.plot(x1, y1, 'b-', linewidth=2, alpha=0.7)
ax2.plot(x2, y2, 'r-', linewidth=2, alpha=0.7)

# Add some geometric shapes (vector primitives)
circle = patches.Circle((100, 100), 25, linewidth=2, edgecolor='green', facecolor='none')
ax2.add_patch(circle)

# Add straight lines
ax2.plot([50, 150], [50, 150], 'k-', linewidth=2)
ax2.plot([50, 150], [150, 50], 'k-', linewidth=2)

# Add "Ve" text
ax2.text(100, 30, 'Ve', fontsize=60, fontweight='bold', ha='center', va='center')

ax2.set_xlim(0, 200)
ax2.set_ylim(0, 200)
ax2.set_aspect('equal')
ax2.grid(True, alpha=0.3)

# Remove axis ticks for cleaner look
ax1.set_xticks([])
ax1.set_yticks([])
ax2.set_xticks([])
ax2.set_yticks([])

# Add border around each subplot
for ax in [ax1, ax2]:
    for spine in ax.spines.values():
        spine.set_edgecolor('black')
        spine.set_linewidth(2)

plt.tight_layout()
plt.show()

# Explanation text (as shown in the document)
print("\nPenjelasan:")
print("Ada sejumlah perbedaan mendasar antara keduanya:")
print("• Piksel adalah susunan cahaya, pigmen, atau warna")
print("• Vektor adalah representasi matematis dari garis, bentuk, gradien, dll.")
print("• Vektor tepat mereka ada di koordinat absolut pada grid aljabar")
print("• Karena mereka sangat absolut, tidak ada garis kabur antara tempat mereka berada dan di mana mereka tidak")
print("• Bahkan jika monitor tidak dapat membuat ketipisan tak terbatas segmen garis")
print("  (selalu harus menampilkannya dalam piksel), itu masih setiap garis yang hanya ada di dunia matematika teoretis.")