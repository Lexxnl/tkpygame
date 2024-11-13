import pygame

from .utils import TerminalColors, print_colored, update_canvas_rect
from .constants import *
from .variables import canvases

class Canvas:
    def __init__(self, screen, x, y, width, height, name, visible=True, buffer=None, color=CANVAS_COLOR_PRIMARY, buffer_width=1080, buffer_height=1920, auto_draw_objects=True):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.name = name
        self.objects = []
        self.visible = visible

        self.buffer_width = buffer_width
        self.buffer_height = buffer_height
        self.auto_draw_objects = auto_draw_objects

        if buffer is not None:
            self.buffer = pygame.Surface((buffer_width, buffer_height))
        else:
            self.buffer = None

        self.resizeable = update_canvas_rect(self)
        canvases.append(self)
        print_colored(f'New canvas object <{self.name}> initiated', TerminalColors.OKBLUE)

    def draw(self, draw_buffer_to_screen=True):
        if self.visible:
            if self.buffer is None:
                if self.resizeable:
                    update_canvas_rect(self)
                pygame.draw.rect(self.screen, self.color, (self._x, self._y, self._width, self._height))

                for obj in self.objects:
                    obj.draw()
            else:
                if self.auto_draw_objects:
                    self.buffer.fill(self.color)

                    for obj in self.objects:
                        obj.draw()

                if draw_buffer_to_screen:
                    self.screen.blit(pygame.transform.scale(self.buffer, (self._width, self._height)), (self._x, self._y))
