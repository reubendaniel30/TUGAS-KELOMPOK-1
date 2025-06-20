import pygame
import sys

# Inisialisasi pygame
pygame.init()

# Konstanta
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700
CHECKERBOARD_SIZE = 200  # Ukuran area checkerboard
TILE_SIZE = 15  # Ukuran setiap kotak

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
LIGHT_GRAY = (200, 200, 200)

def draw_checkerboard(surface, x, y, size, tile_size, color1, color2):
    """
    Menggambar pola checkerboard
    
    Args:
        surface: Surface pygame untuk menggambar
        x, y: Posisi kiri atas checkerboard
        size: Ukuran total checkerboard
        tile_size: Ukuran setiap kotak
        color1, color2: Warna untuk kotak bergantian
    """
    tiles_per_row = size // tile_size
    
    for row in range(tiles_per_row):
        for col in range(tiles_per_row):
            # Tentukan warna berdasarkan posisi (row + col)
            # Jika genap = color1, jika ganjil = color2
            if (row + col) % 2 == 0:
                color = color1
            else:
                color = color2
            
            # Hitung posisi kotak
            rect_x = x + col * tile_size
            rect_y = y + row * tile_size
            
            # Gambar kotak
            pygame.draw.rect(surface, color, (rect_x, rect_y, tile_size, tile_size))

def create_perspective_checkerboard(surface, x, y, size):
    """
    Membuat efek perspektif pada checkerboard dengan mengubah ukuran tile
    """
    base_tile_size = 8
    rows = 20
    
    for row in range(rows):
        # Ukuran tile mengecil ke atas (efek perspektif)
        current_tile_size = base_tile_size + (row * 2)
        tiles_per_row = size // current_tile_size
        
        for col in range(tiles_per_row):
            if col >= tiles_per_row:
                break
                
            # Tentukan warna
            if (row + col) % 2 == 0:
                color = WHITE
            else:
                color = BLACK
            
            # Posisi dengan efek perspektif
            rect_x = x + col * current_tile_size
            rect_y = y + size - (row + 1) * current_tile_size
            
            if rect_y < y:
                break
                
            pygame.draw.rect(surface, color, (rect_x, rect_y, current_tile_size, current_tile_size))

def main():
    # Buat window yang lebih besar untuk layout yang lebih baik
    screen = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption("Checkerboard Patterns")
    clock = pygame.time.Clock()
    
    # Font untuk teks
    title_font = pygame.font.Font(None, 36)
    label_font = pygame.font.Font(None, 20)
    
    # Ukuran pattern yang lebih kecil agar muat semua
    pattern_size = 200
    small_tile_size = 15
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        # Clear screen dengan background abu-abu muda
        screen.fill((240, 240, 240))
        
        # Judul utama
        title_text = title_font.render("Checkerboard Patterns", True, BLACK)
        title_rect = title_text.get_rect(center=(500, 30))
        screen.blit(title_text, title_rect)
        
        # Layout 2x2 untuk 4 pattern
        patterns = [
            {"pos": (80, 80), "label_pos": (80, 50), "label": "Pattern 1: Black & White", 
             "colors": (BLACK, WHITE)},
            {"pos": (520, 80), "label_pos": (520, 50), "label": "Pattern 2: Gray & White", 
             "colors": (GRAY, WHITE)},
            {"pos": (80, 360), "label_pos": (80, 330), "label": "Pattern 3: Light Gray & White", 
             "colors": (LIGHT_GRAY, WHITE)},
        ]
        
        # Gambar 3 pattern reguler
        for pattern in patterns:
            # Label
            label_text = label_font.render(pattern["label"], True, BLACK)
            screen.blit(label_text, pattern["label_pos"])
            
            # Border untuk pattern
            border_rect = (pattern["pos"][0] - 2, pattern["pos"][1] - 2, 
                          pattern_size + 4, pattern_size + 4)
            pygame.draw.rect(screen, BLACK, border_rect, 2)
            
            # Pattern
            draw_checkerboard(screen, pattern["pos"][0], pattern["pos"][1], 
                            pattern_size, small_tile_size, 
                            pattern["colors"][0], pattern["colors"][1])
        
        # Pattern 4 dengan efek perspektif (posisi khusus)
        perspective_label = label_font.render("Pattern 4: Perspective Effect", True, BLACK)
        screen.blit(perspective_label, (520, 330))
        
        # Border untuk perspective pattern
        border_rect = (518, 358, pattern_size + 4, pattern_size + 4)
        pygame.draw.rect(screen, BLACK, border_rect, 2)
        
        # Background putih untuk perspective pattern
        pygame.draw.rect(screen, WHITE, (520, 360, pattern_size, pattern_size))
        create_perspective_checkerboard(screen, 520, 360, pattern_size)
        
        # Garis pemisah
        pygame.draw.line(screen, (180, 180, 180), (50, 320), (950, 320), 1)
        
        # Instruksi di bagian bawah
        instruction = label_font.render("Press ESC to exit", True, (100, 100, 100))
        instruction_rect = instruction.get_rect(center=(500, 650))
        screen.blit(instruction, instruction_rect)
        
        # Info tambahan
        info_text = label_font.render("Computer Graphics - M. Rizky Wahyudi", True, (60, 60, 60))
        info_rect = info_text.get_rect(center=(500, 670))
        screen.blit(info_text, info_rect)
        
        # Update display
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()