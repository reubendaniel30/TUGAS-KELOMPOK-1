import pygame
import sys

# Inisialisasi
pygame.init()

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GRAY = (240, 240, 240)
DARK_GRAY = (50, 50, 50)
ACCENT = (70, 130, 180)  # SteelBlue

# Ukuran layar
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Perbandingan Anti-Aliasing Huruf 'R'")

# Font
font_path = pygame.font.match_font('arial')
font_size = 140
font = pygame.font.Font(font_path, font_size)

# Render huruf "R" dengan dan tanpa anti-aliasing
text_no_aa = font.render("R", False, BLACK)
text_aa = font.render("R", True, BLACK)

# Judul dan label font
title_font = pygame.font.SysFont('segoeui', 32, bold=True)
label_font = pygame.font.SysFont('segoeui', 20)

# Loop utama
running = True
while running:
    # Background gradient-ish effect
    screen.fill(LIGHT_GRAY)
    pygame.draw.rect(screen, WHITE, (50, 80, 300, 250), border_radius=20)
    pygame.draw.rect(screen, WHITE, (450, 80, 300, 250), border_radius=20)

    # Judul
    title_surface = title_font.render("Anti-Aliasing & Tipografi", True, DARK_GRAY)
    screen.blit(title_surface, ((WIDTH - title_surface.get_width()) // 2, 20))

    # Shadow effect (sedikit blur tiruan)
    shadow_offset = 3
    shadow = (180, 180, 180)

    screen.blit(font.render("R", False, shadow), (100 + shadow_offset, 130 + shadow_offset))
    screen.blit(font.render("R", True, shadow), (500 + shadow_offset, 130 + shadow_offset))

    # Huruf utama
    screen.blit(text_no_aa, (100, 130))
    screen.blit(text_aa, (500, 130))

    # Label bawah
    label1 = label_font.render("Tanpa Anti-Aliasing", True, ACCENT)
    label2 = label_font.render("Dengan Anti-Aliasing", True, ACCENT)
    screen.blit(label1, (200 - label1.get_width() // 2, 320))
    screen.blit(label2, (600 - label2.get_width() // 2, 320))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
sys.exit()
