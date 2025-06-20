import matplotlib.pyplot as plt
import numpy as np

def plot_ellipse(cx, cy, a, b):
    theta = np.linspace(0, 2 * np.pi, 100)
    x = cx + a * np.cos(theta)  # Sumbu semi-major
    y = cy + b * np.sin(theta)  # Sumbu semi-minor
    
    plt.plot(x, y, label='Elips', color='blue', linewidth=2)

    # Menambahkan garis radial
    for angle in np.linspace(0, 2 * np.pi, 8, endpoint=False):
        x_end, y_end = cx + a * np.cos(angle), cy + b * np.sin(angle)
        plt.plot([cx, x_end], [cy, y_end], color='orange', linestyle='--', linewidth=1)
        plt.scatter(x_end, y_end, color='red')  # Titik pada elips

    plt.gca().set_aspect('equal')
    plt.title('Elips dengan Garis Radial')
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.legend()
    plt.show()

# Contoh penggunaan
plot_ellipse(0, 0, 5, 3)  # Elips dengan pusat (0,0), sumbu semi-major 5, dan semi-minor 3


