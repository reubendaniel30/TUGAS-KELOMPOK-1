import pygame
import pygame.gfxdraw
import sys
import math

# Inisialisasi pygame
pygame.init()

# Konstanta
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
LIGHT_GRAY = (200, 200, 200)
BLUE = (0, 100, 200)
RED = (200, 50, 50)

class AntiAliasingDemo:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Anti-Aliasing Demo - Editing Photoshop Alias")
        self.clock = pygame.time.Clock()
        
        # Font
        self.title_font = pygame.font.Font(None, 36)
        self.label_font = pygame.font.Font(None, 24)
        self.small_font = pygame.font.Font(None, 18)
        
        # Gambar contoh (simulasi wajah dengan kacamata)
        self.create_sample_images()
    
    def create_sample_images(self):
        """Membuat gambar contoh untuk demonstrasi anti-aliasing"""
        # Ukuran gambar
        img_width, img_height = 300, 200
        
        # Gambar tanpa anti-aliasing (aliased)
        self.aliased_surface = pygame.Surface((img_width, img_height))
        self.aliased_surface.fill(WHITE)
        
        # Gambar dengan anti-aliasing
        self.antialiased_surface = pygame.Surface((img_width, img_height))
        self.antialiased_surface.fill(WHITE)
        
        # Gambar bentuk dasar untuk simulasi wajah
        self.draw_face_aliased(self.aliased_surface)
        self.draw_face_antialiased(self.antialiased_surface)
    
    def draw_face_aliased(self, surface):
        """Menggambar wajah tanpa anti-aliasing (jagged edges)"""
        width, height = surface.get_size()
        center_x, center_y = width // 2, height // 2
        
        # Warna kulit
        skin_color = (255, 220, 177)
        
        # Wajah (lingkaran) - tanpa anti-aliasing
        pygame.draw.circle(surface, skin_color, (center_x, center_y), 80)
        pygame.draw.circle(surface, BLACK, (center_x, center_y), 80, 2)
        
        # Mata
        pygame.draw.circle(surface, WHITE, (center_x - 25, center_y - 20), 12)
        pygame.draw.circle(surface, WHITE, (center_x + 25, center_y - 20), 12)
        pygame.draw.circle(surface, BLACK, (center_x - 25, center_y - 20), 12, 1)
        pygame.draw.circle(surface, BLACK, (center_x + 25, center_y - 20), 12, 1)
        
        # Pupil
        pygame.draw.circle(surface, BLACK, (center_x - 25, center_y - 20), 5)
        pygame.draw.circle(surface, BLACK, (center_x + 25, center_y - 20), 5)
        
        # Kacamata (persegi panjang dengan sudut tajam)
        glasses_rect1 = pygame.Rect(center_x - 45, center_y - 35, 40, 30)
        glasses_rect2 = pygame.Rect(center_x + 5, center_y - 35, 40, 30)
        pygame.draw.rect(surface, BLACK, glasses_rect1, 3)
        pygame.draw.rect(surface, BLACK, glasses_rect2, 3)
        
        # Bridge kacamata
        pygame.draw.line(surface, BLACK, (center_x - 5, center_y - 20), (center_x + 5, center_y - 20), 3)
        
        # Mulut (garis lengkung kasar)
        mouth_points = []
        for i in range(21):
            x = center_x - 20 + i * 2
            y = center_y + 20 + int(5 * math.sin(i * 0.3))
            mouth_points.append((x, y))
        
        if len(mouth_points) > 1:
            pygame.draw.lines(surface, BLACK, False, mouth_points, 2)
    
    def draw_face_antialiased(self, surface):
        """Menggambar wajah dengan anti-aliasing (smooth edges)"""
        width, height = surface.get_size()
        center_x, center_y = width // 2, height // 2
        
        # Warna kulit
        skin_color = (255, 220, 177)
        
        # Wajah (lingkaran) - dengan anti-aliasing
        pygame.gfxdraw.filled_circle(surface, center_x, center_y, 80, skin_color)
        pygame.gfxdraw.aacircle(surface, center_x, center_y, 80, BLACK)
        
        # Mata dengan anti-aliasing
        pygame.gfxdraw.filled_circle(surface, center_x - 25, center_y - 20, 12, WHITE)
        pygame.gfxdraw.filled_circle(surface, center_x + 25, center_y - 20, 12, WHITE)
        pygame.gfxdraw.aacircle(surface, center_x - 25, center_y - 20, 12, BLACK)
        pygame.gfxdraw.aacircle(surface, center_x + 25, center_y - 20, 12, BLACK)
        
        # Pupil dengan anti-aliasing
        pygame.gfxdraw.filled_circle(surface, center_x - 25, center_y - 20, 5, BLACK)
        pygame.gfxdraw.filled_circle(surface, center_x + 25, center_y - 20, 5, BLACK)
        
        # Kacamata dengan sudut rounded (simulasi anti-aliasing)
        self.draw_rounded_rect(surface, (center_x - 45, center_y - 35, 40, 30), BLACK, 3, 5)
        self.draw_rounded_rect(surface, (center_x + 5, center_y - 35, 40, 30), BLACK, 3, 5)
        
        # Bridge kacamata dengan anti-aliasing
        pygame.draw.aaline(surface, BLACK, (center_x - 5, center_y - 20), (center_x + 5, center_y - 20))
        
        # Mulut dengan kurva halus
        mouth_points = []
        for i in range(41):  # Lebih banyak titik untuk kurva yang halus
            x = center_x - 20 + i
            y = center_y + 20 + int(5 * math.sin(i * 0.15))
            mouth_points.append((x, y))
        
        # Gambar kurva halus untuk mulut
        for i in range(len(mouth_points) - 1):
            pygame.draw.aaline(surface, BLACK, mouth_points[i], mouth_points[i+1])
    
    def draw_rounded_rect(self, surface, rect, color, width, radius):
        """Menggambar persegi panjang dengan sudut rounded"""
        x, y, w, h = rect
        
        # Gambar garis-garis dengan anti-aliasing
        pygame.draw.aaline(surface, color, (x + radius, y), (x + w - radius, y))  # Top
        pygame.draw.aaline(surface, color, (x + radius, y + h), (x + w - radius, y + h))  # Bottom
        pygame.draw.aaline(surface, color, (x, y + radius), (x, y + h - radius))  # Left
        pygame.draw.aaline(surface, color, (x + w, y + radius), (x + w, y + h - radius))  # Right
        
        # Sudut rounded menggunakan arc
        pygame.gfxdraw.arc(surface, x + radius, y + radius, radius, 180, 270, color)
        pygame.gfxdraw.arc(surface, x + w - radius, y + radius, radius, 270, 360, color)
        pygame.gfxdraw.arc(surface, x + radius, y + h - radius, radius, 90, 180, color)
        pygame.gfxdraw.arc(surface, x + w - radius, y + h - radius, radius, 0, 90, color)
    
    def draw_comparison_text(self, surface, x, y, text, is_aliased=True):
        """Menggambar teks dengan atau tanpa anti-aliasing"""
        if is_aliased:
            # Teks tanpa anti-aliasing (bitmap font simulation)
            text_surface = self.label_font.render(text, False, BLACK)
        else:
            # Teks dengan anti-aliasing
            text_surface = self.label_font.render(text, True, BLACK)
        
        surface.blit(text_surface, (x, y))
    
    def run(self):
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            
            # Clear screen
            self.screen.fill(LIGHT_GRAY)
            
            # Judul utama
            title_text = self.title_font.render("Editing Photoshop Alias", True, BLACK)
            title_rect = title_text.get_rect(center=(WINDOW_WIDTH // 2, 50))
            self.screen.blit(title_text, title_rect)
            
            # Gambar tanpa anti-aliasing (kiri)
            aliased_x = 150
            aliased_y = 120
            
            # Border untuk gambar kiri
            border_rect1 = (aliased_x - 5, aliased_y - 5, 310, 210)
            pygame.draw.rect(self.screen, BLACK, border_rect1, 2)
            pygame.draw.rect(self.screen, WHITE, (aliased_x, aliased_y, 300, 200))
            
            # Blit gambar aliased
            self.screen.blit(self.aliased_surface, (aliased_x, aliased_y))
            
            # Label untuk gambar kiri
            label1 = self.label_font.render("Tanpa Anti-Aliasing", True, BLACK)
            self.screen.blit(label1, (aliased_x + 80, aliased_y + 220))
            
            # Deskripsi gambar kiri
            desc1 = self.small_font.render("(Edges terlihat kasar/jagged)", True, GRAY)
            self.screen.blit(desc1, (aliased_x + 60, aliased_y + 245))
            
            # Gambar dengan anti-aliasing (kanan)
            antialiased_x = 650
            antialiased_y = 120
            
            # Border untuk gambar kanan
            border_rect2 = (antialiased_x - 5, antialiased_y - 5, 310, 210)
            pygame.draw.rect(self.screen, BLACK, border_rect2, 2)
            pygame.draw.rect(self.screen, WHITE, (antialiased_x, antialiased_y, 300, 200))
            
            # Blit gambar antialiased
            self.screen.blit(self.antialiased_surface, (antialiased_x, antialiased_y))
            
            # Label untuk gambar kanan
            label2 = self.label_font.render("Dengan Anti-Aliasing", True, BLACK)
            self.screen.blit(label2, (antialiased_x + 80, antialiased_y + 220))
            
            # Deskripsi gambar kanan
            desc2 = self.small_font.render("(Edges terlihat halus/smooth)", True, GRAY)
            self.screen.blit(desc2, (antialiased_x + 60, antialiased_y + 245))
            
            # Penjelasan konsep
            explanation_y = 400
            explanation_text = [
                "Konsep Anti-Aliasing:",
                "",
                "• Anti-aliasing adalah teknik untuk mengurangi efek 'jagged edges' atau 'stair-stepping'",
                "• Pada gambar kiri: edges terlihat kasar karena tidak ada smoothing",
                "• Pada gambar kanan: edges terlihat halus karena menggunakan anti-aliasing",
                "• Teknik ini menggunakan gradasi warna untuk menciptakan ilusi tepi yang halus",
                "",
                "Dalam pygame, anti-aliasing dapat dicapai dengan:",
                "• pygame.gfxdraw untuk shapes dengan anti-aliasing",
                "• Font rendering dengan parameter antialias=True",
                "• Menggunakan alpha blending untuk smooth transitions"
            ]
            
            for i, line in enumerate(explanation_text):
                if line.startswith("•"):
                    text_surface = self.small_font.render(line, True, BLUE)
                elif line.startswith("Konsep") or line.startswith("Dalam"):
                    text_surface = self.label_font.render(line, True, BLACK)
                else:
                    text_surface = self.small_font.render(line, True, BLACK)
                
                self.screen.blit(text_surface, (100, explanation_y + i * 20))
            
            # Instruksi
            instruction = self.small_font.render("Press ESC to exit", True, GRAY)
            instruction_rect = instruction.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 30))
            self.screen.blit(instruction, instruction_rect)
            
            # Update display
            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    demo = AntiAliasingDemo()
    demo.run()