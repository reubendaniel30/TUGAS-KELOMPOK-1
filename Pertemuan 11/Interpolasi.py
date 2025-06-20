import pygame
import sys

# Inisialisasi pygame
pygame.init()

# Ukuran layar
width, height = 800, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Interpolasi Linear")

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)

# Font
font = pygame.font.SysFont("Arial", 20)

# Titik-titik data (x, y)
points = [
    (100, 300),  # titik 0
    (200, 100),  # titik 1
    (300, 150),  # titik 2
    (400, 250),  # titik 3
    (500, 150),  # titik 4
    (600, 250)   # titik 5
]

# Loop utama
running = True
while running:
    screen.fill(WHITE)

    # Gambar garis X
    pygame.draw.line(screen, BLACK, (50, 300), (700, 300), 2)

    # Gambar garis vertikal angka 1-5
    for i in range(6):
        x = 100 + i * 100
        pygame.draw.line(screen, BLACK, (x, 290), (x, 310), 2)
        label = font.render(str(i), True, BLACK)
        screen.blit(label, (x - 5, 315))

    # Gambar titik merah
    for pt in points:
        pygame.draw.circle(screen, RED, pt, 7)

    # Gambar garis interpolasi biru
    for i in range(len(points) - 1):
        pygame.draw.line(screen, BLUE, points[i], points[i+1], 3)

    # Label
    label = font.render("Interpolasi: Menciptakan Sesuatu dari (Hampir) Tidak Ada", True, BLACK)
    screen.blit(label, (180, 30))

    # Update layar
    pygame.display.flip()

    # Event keluar
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Keluar pygame
pygame.quit()
sys.exit()