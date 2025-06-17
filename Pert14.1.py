import pygame
import sys
import math

# Inisialisasi
pygame.init()

# Layar
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Warna
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

# Clock
clock = pygame.time.Clock()

# Posisi awal stickman
x = -50
y = 300
step = 4
angle = 0  # untuk animasi langkah

# Fungsi menggambar stickman
def draw_stickman(x, y, angle):
    # Kepala
    pygame.draw.circle(screen, white, (x, y - 50), 10)
    
    # Badan
    pygame.draw.line(screen, white, (x, y - 40), (x, y - 10), 5)

    # Kaki dengan animasi
    offset = 15
    leg_left_y = y + math.sin(angle) * offset
    leg_right_y = y + math.sin(angle + math.pi) * offset

    pygame.draw.line(screen, white, (x, y - 10), (x - 10, leg_left_y), 4)
    pygame.draw.line(screen, white, (x, y - 10), (x + 10, leg_right_y), 4)

    # Tangan
    pygame.draw.line(screen, white, (x, y - 30), (x - 10, y - 20), 3)
    pygame.draw.line(screen, white, (x, y - 30), (x + 10, y - 20), 3)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(black)

    # Judul
    font = pygame.font.Font(None, 64)
    text = font.render("Stickman", True, green)
    screen.blit(text, (screen_width // 2 - 100, 50))

    # Update posisi dan animasi
    draw_stickman(x, y, angle)
    x += step
    angle += 0.1

    if x > screen_width + 50:
        x = -50

    pygame.display.flip()
    clock.tick(30)
