import pygame
import math

# Inisialisasi pygame
pygame.init()

# Konstanta
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)
LIGHT_GRAY = (200, 200, 200)

class ViewingTransformation:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Viewing Transformation - Window to Viewport")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 24)
        self.small_font = pygame.font.Font(None, 18)
        
        # World coordinate system (Window)
        self.world_xmin = -10
        self.world_xmax = 10
        self.world_ymin = -8
        self.world_ymax = 8
        
        # Device coordinate system (Viewport)
        self.viewport_x = 550
        self.viewport_y = 100
        self.viewport_width = 400
        self.viewport_height = 300
        
        # Sample objects in world coordinates
        self.world_objects = [
            # Triangle
            [(-3, 2), (0, 6), (3, 2), (-3, 2)],
            # Mountain-like shape
            [(-8, -2), (-5, 3), (-2, 1), (2, 4), (5, 0), (8, -2)],
            # Rectangle
            [(-6, -6), (6, -6), (6, -4), (-6, -4), (-6, -6)]
        ]
    
    def world_to_window_coords(self, world_x, world_y, window_rect):
        """Convert world coordinates to window display coordinates"""
        wx_min, wy_min, w_width, w_height = window_rect
        
        # Normalize to [0,1]
        norm_x = (world_x - self.world_xmin) / (self.world_xmax - self.world_xmin)
        norm_y = (world_y - self.world_ymin) / (self.world_ymax - self.world_ymin)
        
        # Map to window coordinates (flip Y axis for screen coordinates)
        window_x = wx_min + norm_x * w_width
        window_y = wy_min + (1 - norm_y) * w_height
        
        return int(window_x), int(window_y)
    
    def world_to_viewport_coords(self, world_x, world_y):
        """Convert world coordinates directly to viewport coordinates"""
        # Normalize to [0,1]
        norm_x = (world_x - self.world_xmin) / (self.world_xmax - self.world_xmin)
        norm_y = (world_y - self.world_ymin) / (self.world_ymax - self.world_ymin)
        
        # Map to viewport coordinates (flip Y axis for screen coordinates)
        viewport_x = self.viewport_x + norm_x * self.viewport_width
        viewport_y = self.viewport_y + (1 - norm_y) * self.viewport_height
        
        return int(viewport_x), int(viewport_y)
    
    def draw_coordinate_system(self, rect, title, is_world=True):
        """Draw coordinate system with axes and labels"""
        x, y, width, height = rect
        
        # Draw border
        pygame.draw.rect(self.screen, BLACK, (x-2, y-2, width+4, height+4), 2)
        pygame.draw.rect(self.screen, WHITE, (x, y, width, height))
        
        # Draw title
        title_text = self.font.render(title, True, BLACK)
        title_rect = title_text.get_rect(centerx=x + width//2, y=y - 30)
        self.screen.blit(title_text, title_rect)
        
        if is_world:
            # Draw world coordinate axes
            center_x = x + width // 2
            center_y = y + height // 2
            
            # X axis
            pygame.draw.line(self.screen, GRAY, (x + 20, center_y), (x + width - 20, center_y), 1)
            # Y axis  
            pygame.draw.line(self.screen, GRAY, (center_x, y + 20), (center_x, y + height - 20), 1)
            
            # Labels for world coordinates
            labels = [
                (f"X{chr(8331)}ᵢₙ", x + 10, center_y + 15),
                (f"X{chr(8331)}ₐₓ", x + width - 30, center_y + 15),
                (f"Y{chr(8331)}ᵢₙ", center_x - 25, y + height - 10),
                (f"Y{chr(8331)}ₐₓ", center_x - 25, y + 10)
            ]
        else:
            # Labels for device coordinates
            labels = [
                (f"X{chr(7515)}ᵢₙ", x + 10, y + height + 15),
                (f"X{chr(7515)}ₐₓ", x + width - 30, y + height + 15),
                (f"Y{chr(7515)}ᵢₙ", x - 30, y + height - 10),
                (f"Y{chr(7515)}ₐₓ", x - 30, y + 20)
            ]
        
        for label, lx, ly in labels:
            text = self.small_font.render(label, True, BLACK)
            self.screen.blit(text, (lx, ly))
    
    def draw_objects_in_window(self, window_rect):
        """Draw objects in the window coordinate system"""
        for obj in self.world_objects:
            points = []
            for world_x, world_y in obj:
                win_x, win_y = self.world_to_window_coords(world_x, world_y, window_rect)
                points.append((win_x, win_y))
            
            if len(points) > 2:
                pygame.draw.lines(self.screen, BLUE, False, points, 2)
    
    def draw_objects_in_viewport(self):
        """Draw objects in the viewport coordinate system"""
        for obj in self.world_objects:
            points = []
            for world_x, world_y in obj:
                vp_x, vp_y = self.world_to_viewport_coords(world_x, world_y)
                points.append((vp_x, vp_y))
            
            if len(points) > 2:
                pygame.draw.lines(self.screen, RED, False, points, 2)
    
    def draw_transformation_arrow(self):
        """Draw arrow showing transformation from window to viewport"""
        start_x = 300
        start_y = 250
        end_x = 520
        end_y = 250
        
        
    def draw_info_panel(self):
        """Draw information panel"""
        info_y = 450
        info_texts = [
            "Window (World Coordinate):",
            f"  Range: X[{self.world_xmin}, {self.world_xmax}], Y[{self.world_ymin}, {self.world_ymax}]",
            "Viewport (Device Coordinate):",
            f"  Position: ({self.viewport_x}, {self.viewport_y})",
            f"  Size: {self.viewport_width} x {self.viewport_height}",
            "",
            "Objek biru: tampilan di Window",
            "Objek merah: hasil transformasi di Viewport"
        ]
        
        for i, text in enumerate(info_texts):
            if text.startswith("Objek biru"):
                color = BLUE
            elif text.startswith("Objek merah"):
                color = RED
            else:
                color = BLACK
                
            rendered_text = self.small_font.render(text, True, color)
            self.screen.blit(rendered_text, (50, info_y + i * 20))
    
    def run(self):
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            # Clear screen
            self.screen.fill(WHITE)
            
            # Define window rectangle (left side)
            window_rect = (50, 100, 300, 240)
            
            # Draw coordinate systems
            self.draw_coordinate_system(window_rect, "Window", True)
            self.draw_coordinate_system((self.viewport_x, self.viewport_y, 
                                       self.viewport_width, self.viewport_height), 
                                     "ViewPort", False)
            
            # Draw objects
            self.draw_objects_in_window(window_rect)
            self.draw_objects_in_viewport()
            
            # Draw transformation arrow
            self.draw_transformation_arrow()
            
            # Draw info panel
            self.draw_info_panel()
            
            # Add coordinate system labels
            world_label = self.small_font.render("World Co-ordinate", True, BLACK)
            self.screen.blit(world_label, (120, 350))
            
            device_label = self.small_font.render("Device Co-ordinate", True, BLACK)
            self.screen.blit(device_label, (650, 420))
            
            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()

if __name__ == "__main__":
    viewer = ViewingTransformation()
    viewer.run()