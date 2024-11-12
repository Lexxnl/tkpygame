import pygame

from .utils import TerminalColors, print_colored, update_rect
from .constants import *

class Button:
    def __init__(self, canvas, text: str, anchor, padding, width: int, height: int, name: str, command, text_offset_x=0, text_offset_y=0, color=BUTTON_COLOR_PRIMARY, hover_color=BUTTON_COLOR_HOVER_PRIMARY, pressed_color=BUTTON_COLOR_PRESSED_PRIMARY, font_size=24, font_color=TEXT_COLOR, font_name='Segoe UI', set_width_to_text_rect_width=False, set_height_to_text_rect_height=False):
        self.canvas = canvas
        self.text = text
        self.anchor = anchor
        self.padding = padding
        self.width = width
        self.height = height
        self.color = color
        self.hover_color = hover_color
        self.pressed_color = pressed_color
        self.font_size = font_size
        self.font_color = font_color
        self.font_name = font_name
        self.command = command
        self.name = name

        self.text_offset_x = text_offset_x
        self.text_offset_y = text_offset_y

        self.set_width_to_text_rect_width = set_width_to_text_rect_width
        self.set_height_to_text_rect_height = set_height_to_text_rect_height

        if self.canvas is not None:
            self.canvas.objects.append(self)
            print_colored(f'New object <{self.name}> on canvas <{self.canvas.name}> initiated', TerminalColors.OKGREEN)

            update_rect(self)

        self.previous_frame_mouse_down = True
        
    def draw(self):
        if self._x < pygame.mouse.get_pos()[0] < self._x + self._width and self._y < pygame.mouse.get_pos()[1] < self._y + self._height:
            if pygame.mouse.get_pressed()[0]:
                pygame.draw.rect(self.canvas.screen, self.pressed_color, (self._x, self._y, self._width, self._height))

                if self.previous_frame_mouse_down == False:
                    self.command()
            else:
                pygame.draw.rect(self.canvas.screen, self.hover_color, (self._x, self._y, self._width, self._height))
        else:
            pygame.draw.rect(self.canvas.screen, self.color, (self._x, self._y, self._width, self._height))

        self.previous_frame_mouse_down = pygame.mouse.get_pressed()[0]  # Update the global variable
        
        # Draw the text
        self.update_text_surface()

    def update_text_surface(self):
        if not hasattr(self, '_font') or self._font is None:
            self._font = pygame.font.SysFont(self.font_name, self.font_size)
        text_surface = self._font.render(str(self.text), True, self.font_color)
        text_rect = text_surface.get_rect()

        if self.set_width_to_text_rect_width:
            self.width = text_rect.width + 40
        if self.set_height_to_text_rect_height:
            self.height = text_rect.height + 20
        
        if self.set_height_to_text_rect_height or self.set_width_to_text_rect_width:
            update_rect(self)

        

        text_rect.center = (self._x + (self._width / 2) + self.text_offset_x, self._y + (self._height / 2) + self.text_offset_y)
        self.canvas.screen.blit(text_surface, text_rect)