import pygame

from .utils import TerminalColors, print_colored, update_rect
from .constants import *


class Label:
    def __init__(self, canvas, text, anchor, padding, width, height, name, text_offset_x=0, text_offset_y=0, color=None, font_size=24, font_color='#ffffff', font_name='Segoe UI', visible = True, canvas_x=None, canvas_y=None):
        self.canvas = canvas
        self.text = text
        self.anchor = anchor
        self.padding = padding
        self.width = width
        self.height = height
        self.color = color
        self.font_size = font_size
        self.font_color = font_color
        self.font_name = font_name
        self.name = name
        self.text_offset_x = text_offset_x
        self.text_offset_y = text_offset_y
        self.visible = visible
        self.text_surface = None

        self.canvas_x = canvas_x
        self.canvas_y = canvas_y
        update_rect(self)
        
        if self.canvas != None:
            self.canvas.objects.append(self)
            print_colored(f'New object <{self.name}> on canvas <{self.canvas.name}> initiated with text <{self.text}>', TerminalColors.OKGREEN)
        
        self.update_text_surface()

    def draw(self):
        if callable(self.visible):
            self._visible = self.visible()
        else:
            self._visible = self.visible
        
        if self._visible:
            if self._width != None and self._height != None and self.color != None:
                pygame.draw.rect(self.canvas.screen, self.color, (self._x, self._y, self._width, self._height))

            if self.text_surface != None:
                text_rect = self.text_surface.get_rect()
                text_rect.center = (self._x + self.text_surface.get_width() / 2 + self.text_offset_x, self._y + self.text_surface.get_height() / 2 + self.text_offset_y)
                self.canvas.screen.blit(self.text_surface, text_rect)
            else:
                self.update_text_surface()

    def update_text_surface(self):
        if not hasattr(self, '_font') or self._font is None:
            self._font = pygame.font.SysFont(self.font_name, self.font_size)
        text_surface = self._font.render(str(self.text), True, self.font_color)
        self.width, self.height = text_surface.get_width(), text_surface.get_height()
        
        update_rect(self)
        self.text_surface = text_surface