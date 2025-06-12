import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Rasterisasi Garis - Algoritma Bresenham")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def bresenham_line(x1, y1, x2, y2):
    # Algoritma rasterisasi garis Bresenham
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x, y = x1, y1
    sx = 1 if x2 >= x1 else -1
    sy = 1 if y2 >= y1 else -1
    if dx > dy:
        err = dx // 2
        while x != x2:
            screen.set_at((x, y), BLACK)
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy // 2
        while y != y2:
            screen.set_at((x, y), BLACK)
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy
    screen.set_at((x, y), BLACK)

# Main loop
running = True
while running:
    screen.fill(WHITE)
    
    # Contoh garis: titik awal dan akhir
    garis = [
        (50, 50, 300, 200),
        (100, 300, 300, 100),
        (400, 100, 700, 200)
    ]
    
    for g in garis:
        bresenham_line(*g)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()