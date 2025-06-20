import matplotlib.pyplot as plt

def plot_cartesian_line(x0, y0, x1, y1):
    plt.figure(figsize=(6, 6))
    plt.axhline(0, color='black', linewidth=1.5)
    plt.axvline(0, color='black', linewidth=1.5)
    plt.grid(True, which='both')
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    
    # Menggambar garis
    plt.plot([x0, x1], [y0, y1], marker='o', color='red', label='Garis Koordinat')
    plt.title("Garis pada Koordinat Cartesian")
    plt.legend()
    plt.show()

# Contoh menggambar garis dari (-7,-5) ke (8,9)
plot_cartesian_line(-7, -5, 8, 9)
