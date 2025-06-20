import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
import matplotlib.patches as patches

# Set up the figure
fig, axes = plt.subplots(1, 5, figsize=(15, 6))
fig.suptitle('Gambar 11.2 Line Thinning', fontsize=16, fontweight='bold', y=0.85)

# Define the titles for each subplot
titles = ['None', '2x', '4x', '8x', '16x']
line_widths = [8, 4, 2, 1, 0.5]  # Corresponding line widths

# Create diagonal striped pattern for each level of thinning
for i, (ax, title, width) in enumerate(zip(axes, titles, line_widths)):
    ax.set_title(title, fontsize=12, fontweight='bold', pad=10)
    
    # Set up the plot area
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 150)
    ax.set_aspect('equal')
    
    # Create diagonal lines pattern
    # Number of lines decreases as we go from None to 16x
    num_lines = max(1, int(20 / (i + 1)))  # Fewer lines for higher thinning
    
    for j in range(num_lines):
        # Create diagonal lines from bottom-left to top-right
        x_start = j * (100 / num_lines)
        y_start = 0
        x_end = x_start + 50
        y_end = 150
        
        # Adjust line width based on thinning level
        line_width = width * (1 + i * 0.5)  # Gradually decrease thickness
        
        # Draw the diagonal line
        ax.plot([x_start, x_end], [y_start, y_end], 
               color='black', linewidth=line_width, alpha=0.8)
        
        # Add some variation in the lines
        if i == 0:  # None - thickest lines
            # Add additional thick lines
            ax.plot([x_start + 2, x_end + 2], [y_start, y_end], 
                   color='black', linewidth=line_width, alpha=0.6)
    
    # Add some horizontal elements to simulate text/content
    for k in range(5):
        y_pos = 30 + k * 25
        # Create pixelated/jagged effect for "None", smoother for higher thinning
        if i == 0:  # None - most jagged
            x_positions = np.arange(10, 90, 3)
            y_noise = np.random.normal(0, 1, len(x_positions))
            ax.plot(x_positions, y_pos + y_noise, 'k-', linewidth=2, alpha=0.7)
        else:  # Progressively smoother
            smoothness = i + 1
            x_positions = np.linspace(10, 90, 20 // smoothness)
            y_noise = np.random.normal(0, 0.5/smoothness, len(x_positions))
            ax.plot(x_positions, y_pos + y_noise, 'k-', linewidth=1.5/smoothness, alpha=0.8)
    
    # Remove ticks and labels for cleaner look
    ax.set_xticks([])
    ax.set_yticks([])
    
    # Add border
    for spine in ax.spines.values():
        spine.set_edgecolor('black')
        spine.set_linewidth(1)

plt.tight_layout()
plt.subplots_adjust(top=0.8)
plt.show()

# Print explanation text
print("\nPenjelasan Line Thinning:")
print("=" * 50)
print("Diperbesar akan membentuk sebuah tangga/garis patah-patah. Anti aliasing")
print("sejauh ini dibagi menjadi 2x,4x,8x,16x semakin tinggi tingkat aliasing nya maka")
print("semakin halus atau semakin menarik gambar/objek tersebut.")
print()
print("Sebagai contoh yang lebih sederhana:")
print("Jika kamu zoom suatu gambar dengan jarak yang sangat dekat, maka")
print("kamu tidak akan melihat gambar tersebut seperti semula, melainkan gambar")
print("tersebut akan pecah atau bergerigi pada pinggir, itu disepertemuankan karena")
print("kamu belum memberikan anti aliasing pada gambar tersebut. Contoh")
print("selanjutnya jika kalian membuat garis, dan garis yang anda buat menggunakan")
print("ukuran yang kecil maka setelah di zoom akan terlihat seperti patah-patah jika")
print("tidak diberikan anti aliasing.")
print()
print("Fungsi dari anti aliasing ini yaitu sebagai filter yang mengubah warna pada")
print("pixel disekitar objek yang terlihat patah-patah untuk dibuat menjadi objek yang")
print("lebih halus.")