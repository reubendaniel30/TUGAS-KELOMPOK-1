import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Rasterisasi Lingkaran - Midpoint Circle Algorithm")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_circle_midpoint(xc, yc, r):
    x = 0
    y = r
    p = 1 - r
    plot_circle_points(xc, yc, x, y)
    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        plot_circle_points(xc, yc, x, y)

def plot_circle_points(xc, yc, x, y):
    points = [
        (xc + x, yc + y), (xc - x, yc + y),
        (xc + x, yc - y), (xc - x, yc - y),
        (xc + y, yc + x), (xc - y, yc + x),
        (xc + y, yc - x), (xc - y, yc - x)
    ]
    for px, py in points:
        screen.set_at((px, py), BLACK)

running = True
while running:
    screen.fill(WHITE)
    
    # Gambar lingkaran di tengah layar
    draw_circle_midpoint(300, 300, 100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()