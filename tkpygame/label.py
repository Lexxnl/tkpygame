import pygame

from .canvas import Canvas
from .constants import *
from .utils import print_colored, absolute_position, get_main_canvas

class Label:
    def __init__(self, canvas: Canvas, text: str, anchor: Anchor = Anchor.TOP_LEFT, font: str = FONT_NAME_PRIMARY, font_size: int = FONT_SIZE_PRIMARY, color: str = FONT_COLOR_PRIMARY, name: str = 'label', visible: bool = True, padding: tuple = (0, 0), font_color: str = FONT_COLOR_PRIMARY):
        self.canvas = canvas
        self.anchor = anchor
        self.padding = padding

        self.text = text
        self.font = font
        self.font_size = font_size
        self.font_color = font_color
        self.color = color
        self.name = name
        self.visible = visible


        self.update_text_surface()
        self.position = absolute_position(self)

        if hasattr(self.canvas, 'objects') and not self in self.canvas.objects:
            self.canvas.objects.append(self)

        print_colored(f'New label element <{self.name}> initiated', TerminalColors.SUCCESS)

    def draw(self):
        if not self.visible:
            return

        if self.text_surface is None:
            self.update_text_surface()
        if self.position is None:
            self.position = absolute_position(self)
        
        pygame.display.get_surface().blit(self.text_surface, self.position)

    def update_text_surface(self):
        if not hasattr(self, '_font') or self._font is None:
            self._font = pygame.font.SysFont(self.font, self.font_size)
        text_surface = self._font.render(str(self.text), True, self.font_color)
        self.size = (text_surface.get_width(), text_surface.get_height())
        
        self.text_surface = text_surface
