import matplotlib.pyplot as plt

def draw_line (x0, y0, x1, y1):
    # Menghitung perubahan dalam x dan y
    dx = x1 - x0
    dy = y1 - y0
    steps = max(abs(dx), abs(dy))

    # Menghitung inkremen per langkah
    x_inc = dx / steps
    y_inc = dy / steps

    # Menghitung titik - titik garis
    points = [(round(x0 + i * x_inc), round(y0 + i * y_inc)) for i in range(steps + 1)]

    # Memisahkan x dan y untuk menggambar 
    x_points, y_points = zip(*points)
    plt.plot(x_points, y_points, marker='o')
    plt.title('Midpoint Line Algorithm')
    plt.xlim(min(x0, x1) - 1, max(x0, x1) + 1)
    plt.ylim(min(y0, y1) - 1, max(y0, y1) + 1)
    plt.grid()
    plt.axhline(0, color = 'black', linewidth=0.5, ls='--')
    plt.axvline(0, color = 'black', linewidth=0.5, ls='--')
    plt.show()

# Contoh penggunaan
draw_line (2, 5, 10, 8)