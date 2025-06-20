import pygame
import sys

# Inisialisasi pygame
pygame.init()

# Ukuran layar
width, height = 800, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Antialiasing with Pygame")

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font
font = pygame.font.SysFont("Arial", 20)

# Loop utama
running = True
while running:
    screen.fill(WHITE)

    # Teks label
    screen.blit(font.render("Aliased", True, BLACK), (150, 20))
    screen.blit(font.render("Anti-Aliased", True, BLACK), (550, 20))

    # --- Aliased (tanpa anti-aliasing) ---
    # Garis patah-patah kasar
    pygame.draw.line(screen, BLACK, (100, 50), (300, 150), 1)
    pygame.draw.circle(screen, BLACK, (200, 200), 50, 0)
    pygame.draw.lines(screen, BLACK, False, [(100, 300), (150, 250), (200, 300), (250, 250), (300, 300)], 3)

    # --- Anti-Aliased ---
    # Garis halus (menggunakan aaline)
    pygame.draw.aaline(screen, BLACK, (500, 50), (700, 150))
    
    # Lingkaran dihaluskan dengan blit dari permukaan lebih besar → kecil
    circle_surf = pygame.Surface((200, 200), pygame.SRCALPHA)
    pygame.draw.circle(circle_surf, BLACK, (100, 100), 80)
    circle_surf = pygame.transform.smoothscale(circle_surf, (100, 100))  # Downscale untuk efek halus
    screen.blit(circle_surf, (550, 150))

    # Garis zigzag halus (pakai aaline satu per satu)
    points = [(500, 300), (550, 250), (600, 300), (650, 250), (700, 300)]
    for i in range(len(points)-1):
        pygame.draw.aaline(screen, BLACK, points[i], points[i+1])

    # Update layar
    pygame.display.flip()

    # Keluar jika user tutup jendela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Keluar pygame
pygame.quit()
sys.exit()
