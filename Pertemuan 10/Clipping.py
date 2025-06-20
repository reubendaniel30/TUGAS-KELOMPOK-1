import pygame
import math
import sys

# Inisialisasi pygame
pygame.init()

# Konstanta
WIDTH, HEIGHT = 1000, 700
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)
LIGHT_GRAY = (200, 200, 200)
PURPLE = (128, 0, 128)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x:.1f}, {self.y:.1f})"

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

class ClippingApp:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Implementasi Clipping - Cohen-Sutherland & Liang-Barsky")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 20)
        self.title_font = pygame.font.Font(None, 24)
        
        # Clipping window (rectangle)
        self.clip_rect = pygame.Rect(100, 100, 300, 200)
        self.dragging_rect = False
        self.rect_offset = (0, 0)
        
        # Lines untuk di-clip
        self.lines = [
            Line(Point(50, 150), Point(200, 250)),
            Line(Point(150, 50), Point(350, 300)),
            Line(Point(250, 80), Point(450, 180)),
            Line(Point(80, 250), Point(380, 120)),
            Line(Point(200, 200), Point(300, 100)),
        ]
        
        # Mode clipping
        self.clipping_mode = "cohen_sutherland"  # atau "liang_barsky"
        
        # State untuk menambah line baru
        self.drawing_line = False
        self.temp_line_start = None
        
        # Cohen-Sutherland region codes
        self.INSIDE = 0  # 0000
        self.LEFT = 1    # 0001
        self.RIGHT = 2   # 0010
        self.BOTTOM = 4  # 0100
        self.TOP = 8     # 1000
    
    def compute_outcode(self, point):
        """Menghitung outcode untuk Cohen-Sutherland algorithm"""
        code = self.INSIDE
        
        if point.x < self.clip_rect.left:
            code |= self.LEFT
        elif point.x > self.clip_rect.right:
            code |= self.RIGHT
        
        if point.y < self.clip_rect.top:
            code |= self.TOP
        elif point.y > self.clip_rect.bottom:
            code |= self.BOTTOM
        
        return code
    
    def cohen_sutherland_clip(self, line):
        """Implementasi Cohen-Sutherland line clipping algorithm"""
        x1, y1 = line.p1.x, line.p1.y
        x2, y2 = line.p2.x, line.p2.y
        
        outcode1 = self.compute_outcode(Point(x1, y1))
        outcode2 = self.compute_outcode(Point(x2, y2))
        
        accept = False
        
        while True:
            # Kedua titik di dalam
            if outcode1 == 0 and outcode2 == 0:
                accept = True
                break
            # Kedua titik di luar dan di sisi yang sama
            elif outcode1 & outcode2:
                break
            else:
                # Pilih titik yang di luar
                if outcode1 != 0:
                    outcode_out = outcode1
                else:
                    outcode_out = outcode2
                
                # Cari intersection point
                if outcode_out & self.TOP:
                    x = x1 + (x2 - x1) * (self.clip_rect.top - y1) / (y2 - y1)
                    y = self.clip_rect.top
                elif outcode_out & self.BOTTOM:
                    x = x1 + (x2 - x1) * (self.clip_rect.bottom - y1) / (y2 - y1)
                    y = self.clip_rect.bottom
                elif outcode_out & self.RIGHT:
                    y = y1 + (y2 - y1) * (self.clip_rect.right - x1) / (x2 - x1)
                    x = self.clip_rect.right
                elif outcode_out & self.LEFT:
                    y = y1 + (y2 - y1) * (self.clip_rect.left - x1) / (x2 - x1)
                    x = self.clip_rect.left
                
                # Update point dan outcode
                if outcode_out == outcode1:
                    x1, y1 = x, y
                    outcode1 = self.compute_outcode(Point(x1, y1))
                else:
                    x2, y2 = x, y
                    outcode2 = self.compute_outcode(Point(x2, y2))
        
        if accept:
            return Line(Point(x1, y1), Point(x2, y2))
        return None
    
    def liang_barsky_clip(self, line):
        """Implementasi Liang-Barsky line clipping algorithm"""
        x1, y1 = line.p1.x, line.p1.y
        x2, y2 = line.p2.x, line.p2.y
        
        dx = x2 - x1
        dy = y2 - y1
        
        # Parameter equations: x = x1 + t*dx, y = y1 + t*dy
        p = [-dx, dx, -dy, dy]
        q = [x1 - self.clip_rect.left, self.clip_rect.right - x1, 
             y1 - self.clip_rect.top, self.clip_rect.bottom - y1]
        
        u1, u2 = 0.0, 1.0
        
        for i in range(4):
            if p[i] == 0:
                # Line parallel to clipping boundary
                if q[i] < 0:
                    return None  # Line is outside
            else:
                t = q[i] / p[i]
                if p[i] < 0:
                    # Line entering clipping region
                    if t > u2:
                        return None
                    elif t > u1:
                        u1 = t
                else:
                    # Line leaving clipping region
                    if t < u1:
                        return None
                    elif t < u2:
                        u2 = t
        
        if u1 < u2:
            # Calculate clipped endpoints
            clip_x1 = x1 + u1 * dx
            clip_y1 = y1 + u1 * dy
            clip_x2 = x1 + u2 * dx
            clip_y2 = y1 + u2 * dy
            return Line(Point(clip_x1, clip_y1), Point(clip_x2, clip_y2))
        
        return None
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    # Toggle clipping algorithm
                    if self.clipping_mode == "cohen_sutherland":
                        self.clipping_mode = "liang_barsky"
                    else:
                        self.clipping_mode = "cohen_sutherland"
                elif event.key == pygame.K_r:
                    # Reset lines
                    self.lines = [
                        Line(Point(50, 150), Point(200, 250)),
                        Line(Point(150, 50), Point(350, 300)),
                        Line(Point(250, 80), Point(450, 180)),
                        Line(Point(80, 250), Point(380, 120)),
                        Line(Point(200, 200), Point(300, 100)),
                    ]
                elif event.key == pygame.K_SPACE:
                    # Clear all lines
                    self.lines = []
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    mouse_pos = pygame.mouse.get_pos()
                    
                    # Check if clicking on clipping rectangle
                    if self.clip_rect.collidepoint(mouse_pos):
                        self.dragging_rect = True
                        self.rect_offset = (mouse_pos[0] - self.clip_rect.x, 
                                          mouse_pos[1] - self.clip_rect.y)
                    else:
                        # Start drawing line
                        self.drawing_line = True
                        self.temp_line_start = Point(mouse_pos[0], mouse_pos[1])
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if self.dragging_rect:
                        self.dragging_rect = False
                    elif self.drawing_line:
                        # Finish drawing line
                        mouse_pos = pygame.mouse.get_pos()
                        end_point = Point(mouse_pos[0], mouse_pos[1])
                        if abs(self.temp_line_start.x - end_point.x) > 5 or \
                           abs(self.temp_line_start.y - end_point.y) > 5:
                            self.lines.append(Line(self.temp_line_start, end_point))
                        self.drawing_line = False
                        self.temp_line_start = None
            elif event.type == pygame.MOUSEMOTION:
                if self.dragging_rect:
                    mouse_pos = pygame.mouse.get_pos()
                    self.clip_rect.x = mouse_pos[0] - self.rect_offset[0]
                    self.clip_rect.y = mouse_pos[1] - self.rect_offset[1]
        return True
    
    def draw_line(self, line, color, width=2):
        """Draw line on screen"""
        pygame.draw.line(self.screen, color, 
                        (int(line.p1.x), int(line.p1.y)), 
                        (int(line.p2.x), int(line.p2.y)), width)
    
    def draw_point(self, point, color, radius=3):
        """Draw point on screen"""
        pygame.draw.circle(self.screen, color, 
                          (int(point.x), int(point.y)), radius)
    
    def draw_interface(self):
        """Draw user interface"""
        # Title
        title = f"Line Clipping - {self.clipping_mode.replace('_', ' ').title()}"
        title_surface = self.title_font.render(title, True, WHITE)
        self.screen.blit(title_surface, (10, 10))
        
        # Instructions
        instructions = [
            "Kontrol:",
            "• Klik & drag: Buat garis baru",
            "• Drag kotak: Pindah clipping window",
            "• C: Ganti algoritma clipping",
            "• R: Reset garis default",
            "• SPACE: Hapus semua garis",
            "",
            f"Algoritma: {self.clipping_mode.replace('_', ' ').title()}",
        ]
        
        y_offset = 40
        for instruction in instructions:
            text_surface = self.font.render(instruction, True, WHITE)
            self.screen.blit(text_surface, (10, y_offset))
            y_offset += 22
        
        # Algorithm info
        info_x = WIDTH - 300
        if self.clipping_mode == "cohen_sutherland":
            info = [
                "Cohen-Sutherland Algorithm:",
                "• Menggunakan region codes (outcodes)",
                "• Membagi area menjadi 9 region",
                "• Efficient untuk rectangular clipping",
                "",
                "Region Codes:",
                "1001 | 1000 | 1010",
                "0001 | 0000 | 0010",
                "0101 | 0100 | 0110"
            ]
        else:
            info = [
                "Liang-Barsky Algorithm:",
                "• Menggunakan parametric line equation",
                "• x = x1 + t*dx, y = y1 + t*dy",
                "• Menghitung parameter t untuk intersection",
                "• Lebih efisien untuk multiple clipping"
            ]
        
        y_offset = 40
        for line in info:
            text_surface = self.font.render(line, True, YELLOW)
            self.screen.blit(text_surface, (info_x, y_offset))
            y_offset += 22
    
    def run(self):
        running = True
        while running:
            running = self.handle_events()
            
            # Clear screen
            self.screen.fill(BLACK)
            
            # Draw clipping rectangle
            pygame.draw.rect(self.screen, BLUE, self.clip_rect, 3)
            
            # Draw original lines (in light gray)
            for line in self.lines:
                self.draw_line(line, LIGHT_GRAY, 1)
            
            # Draw clipped lines
            for line in self.lines:
                if self.clipping_mode == "cohen_sutherland":
                    clipped = self.cohen_sutherland_clip(line)
                else:
                    clipped = self.liang_barsky_clip(line)
                
                if clipped:
                    self.draw_line(clipped, GREEN, 3)
                    # Draw endpoints
                    self.draw_point(clipped.p1, RED)
                    self.draw_point(clipped.p2, RED)
            
            # Draw temporary line while drawing
            if self.drawing_line and self.temp_line_start:
                mouse_pos = pygame.mouse.get_pos()
                pygame.draw.line(self.screen, WHITE, 
                               (int(self.temp_line_start.x), int(self.temp_line_start.y)),
                               mouse_pos, 1)
            
            # Draw interface
            self.draw_interface()
            
            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()

def main():
    app = ClippingApp()
    app.run()

if __name__ == "__main__":
    main()