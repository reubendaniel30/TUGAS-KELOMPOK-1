import matplotlib.pyplot as plt
import numpy as np

def binomial_coefficient(n, k):
    if k > n: return 0
    if k == 0 or k == n: return 1
    k = min(k, n - k)
    c = 1
    for i in range(k): c = c * (n - i) // (i + 1)
    return c

def bezier_curve(points, n=100):
    t = np.linspace(0, 1, n)
    curve = np.zeros((n, 2))
    for i in range(len(points)):
        bernstein = binomial_coefficient(len(points) - 1, i) * (t ** i) * ((1 - t) ** (len(points) - 1 - i))
        curve += np.outer(bernstein, points[i])
    return curve[:, 0], curve[:, 1]

def plot_bezier(points):
    plt.plot(*bezier_curve(points), label='Kurva Bézier')
    plt.plot(*zip(*points), 'ro--', label='Titik Kontrol')
    plt.title('Kurva Bézier')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()
# Contoh penggunaan
plot_bezier([(0, 0), (1, 2), (3, 3), (4, 0)])
