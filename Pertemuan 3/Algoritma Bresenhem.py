import matplotlib.pyplot as plt

def bresenham(x0, y0, x1, y1):
    points = []
    dx, dy = abs(x1 - x0), abs(y1 - y0)
    sx, sy = (1 if x0 < x1 else -1), (1 if y0 < y1 else -1)
    err = dx - dy

    while True:
        points.append((x0, y0))
        if x0 == x1 and y0 == y1: break
        err2 = err * 2
        if err2 > -dy: err, x0 = err - dy, x0 + sx
        if err2 < dx: err, y0 = err + dx, y0 + sy
    return points

def plot_bresenham_line(x0, y0, x1, y1):
    xs, ys = zip(*bresenham(x0, y0, x1, y1))
    plt.figure(figsize=(6, 6))
    plt.axhline(0, color='black', linewidth=1.5)
    plt.axvline(0, color='black', linewidth=1.5)
    plt.grid(True)
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.plot(xs, ys, marker='o', color='red')
    plt.title("Garis Bresenham")
    plt.show()
# Contoh penggunaan
plot_bresenham_line(-7, -5, 8, 9)
