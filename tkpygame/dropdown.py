import pygame

from .utils import TerminalColors, print_colored, update_canvas_rect
from .constants import *
from .variables import dropdowns as dropdowns

class Dropdown:
    def __init__(self, screen, text, x, y, parent_button, name, color=DROPDOWN_COLOR_SECONDARY, objects=[], on_cursor_leave_command=None, font_name='Segoe UI', font_size=16, text_color=TEXT_COLOR):
        self.screen = screen
        self.text = text
        self.x = x
        self.y = y

        self.width = 0
        self.height = 0

        self.color = color
        self.objects = objects
        self.parent_button = parent_button
        self.name = name

        self.font_name = font_name
        self.font_size = font_size
        self.font_color = text_color

        if on_cursor_leave_command == None:
            self.on_cursor_leave_command = lambda: print_colored(f'No command set for object <{self.name}>', TerminalColors.FAIL)
        else:
            self.on_cursor_leave_command = on_cursor_leave_command

        update_canvas_rect(self)

        for button in objects:
            button.canvas = self

        self.parent_button.forced_state = 2

        dropdowns.append(self)
        self.update_text_surface()
        self.destroyed = False

    def draw(self):
        if not self.destroyed:
            self.height = 0
            for button in self.objects:
                self.width = button._width if button._width > self.width else self.width
                self.height += button._height

            if self.x - 5 - 50 < pygame.mouse.get_pos()[0] < self.x + self.width + 5 + 50 and self.y - 5 - 50 < pygame.mouse.get_pos()[1] < self.y + self.height + 30 + 50:
                pygame.draw.rect(self.screen, self.color, (self.x-5, self.y-5, self.width+10, self.height+40))
                for button in self.objects:
                    button._x = self.x
                    button._y = self.y + button._height * self.objects.index(button) + 30
                    button.draw()
            else:
                self.parent_button.forced_state = -1
                self.on_cursor_leave_command()
                variables.dropdowns = []
                self.objects = []

            text_rect = self.text_surface.get_rect()
            text_rect.center = (self.x + self.text_surface.get_width() / 2 + 5, self.y + self.text_surface.get_height() / 2)
            self.screen.blit(self.text_surface, text_rect)

    def update_text_surface(self):
        if not hasattr(self, '_font') or self._font is None:
            self._font = pygame.font.SysFont(self.font_name, self.font_size)
            
        text_surface = self._font.render(str(self.text), True, self.font_color)
        self.text_surface = text_surface
   