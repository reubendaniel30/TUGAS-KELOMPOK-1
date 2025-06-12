import pygame
import sys

# Warna
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

# Ukuran layar
WIDTH, HEIGHT = 800, 600

# Window clipping (area merah)
x_min, y_min = 200, 150
x_max, y_max = 600, 450

# Region codes
INSIDE = 0  # 0000
LEFT   = 1  # 0001
RIGHT  = 2  # 0010
BOTTOM = 4  # 0100
TOP    = 8  # 1000

def compute_code(x, y):
    code = INSIDE
    if x < x_min:
        code |= LEFT
    elif x > x_max:
        code |= RIGHT
    if y < y_min:
        code |= BOTTOM   # Perbaikan: BOTTOM jika y < y_min
    elif y > y_max:
        code |= TOP      # Perbaikan: TOP jika y > y_max
    return code

def cohen_sutherland_clip(x1, y1, x2, y2):
    code1 = compute_code(x1, y1)
    code2 = compute_code(x2, y2)
    accept = False

    while True:
        if code1 == 0 and code2 == 0:
            accept = True
            break
        elif (code1 & code2) != 0:
            break
        else:
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

            if code_out & TOP:
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                y = y_max
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                y = y_min
            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
                x = x_max
            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
                x = x_min

            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2)

    if accept:
        return int(x1), int(y1), int(x2), int(y2)
    else:
        return None

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Cohen-Sutherland Line Clipping")
    screen.fill(WHITE)

    # Gambar clipping window (kotak merah)
    pygame.draw.rect(screen, RED, (x_min, y_min, x_max - x_min, y_max - y_min), 2)

    # Contoh garis
    lines = [
        (100, 100, 700, 500),     # Memotong window (harus tampil)
        (250, 200, 550, 400),     # Di dalam window (harus tampil penuh)
        (50, 50, 100, 100),       # Di luar window (tidak tampil)
        (100, 300, 700, 300),     # Melintasi kiri dan kanan (harus tampil sebagian)
        (250, 100, 250, 500),     # Melintasi atas dan bawah (harus tampil sebagian)
    ]

    for line in lines:
        x1, y1, x2, y2 = line

        # Gambar garis awal (biru)
        pygame.draw.line(screen, BLUE, (x1, y1), (x2, y2), 1)

        # Proses clipping
        clipped_line = cohen_sutherland_clip(x1, y1, x2, y2)
        if clipped_line:
            cx1, cy1, cx2, cy2 = clipped_line
            pygame.draw.line(screen, GREEN, (cx1, cy1), (cx2, cy2), 3)
        else:
            print("Garis di luar window dan tidak ditampilkan:", line)

    pygame.display.update()

    # Loop utama
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()