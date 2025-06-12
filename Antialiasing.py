import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Antialiasing Demo")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.SysFont(None, 30)
clock = pygame.time.Clock()

def draw_antialiased_line(screen, color, start, end):
    # Antialiasing dengan pygame gfxdraw (menghaluskan tepi garis)
    import pygame.gfxdraw
    pygame.gfxdraw.line(screen, *start, *end, color)

running = True
while running:
    screen.fill(WHITE)
    
    text1 = font.render("Tanpa Antialiasing", True, BLACK)
    text2 = font.render("Dengan Antialiasing", True, BLACK)
    screen.blit(text1, (50, 50))
    screen.blit(text2, (50, 300))
    
    # Garis kasar (tanpa antialiasing)
    for i in range(5):
        pygame.draw.line(screen, BLACK, (50, 100 + i*10), (400, 100 + i*10 + 15), 1)

    # Garis halus (dengan antialiasing)
    for i in range(5):
        draw_antialiased_line(screen, BLACK, (50, 350 + i*10), (400, 350 + i*10 + 15))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()