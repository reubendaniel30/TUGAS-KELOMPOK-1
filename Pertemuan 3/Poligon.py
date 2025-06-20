import matplotlib.pyplot as plt

def draw_polyline(points, closed=False):
    pts = points + [points[0]] if closed else points
    xs, ys = zip(*pts)

    plt.plot(xs, ys, marker='o', linestyle='-', color='b')
    plt.title('Garis Poligon' + (' Tertutup' if closed else ' Terbuka'))
    plt.grid(True)
    plt.axis('equal')
    plt.show()

# Contoh penggunaan
points = [(1, 5), (4, 7), (7, 3), (5, 1)]
draw_polyline(points, closed=True)   # Poligon tertutup
draw_polyline(points, closed=False)  # Poligon terbuka (switch)