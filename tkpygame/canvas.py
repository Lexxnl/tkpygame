import pygame

from .screen import Screen
from .constants import *
from .utils import print_colored, absolute_position

class Canvas:
    def __init__(self, screen: Screen, size: tuple, anchor: Anchor = Anchor.TOP_LEFT, padding: tuple = (0, 0), color: str = CANVAS_COLOR_PRIMARY, objects: list = [], name: str = 'canvas', visible: bool = True):
        self.screen = screen
        self.anchor = anchor
        self.padding = padding
        self.size = size
        self.color = color
        self.name = name
        self.visible = visible
        self.objects = objects

        self.position = absolute_position(self)

        if not self in self.screen.objects:
            self.screen.objects.append(self)

        print_colored(f'New canvas element <{self.name}> initiated', TerminalColors.SUCCESS)

    def draw(self):
        
        
        # Ensure self.position and self.size are tuples or call them if they are methods
        position = self.position() if callable(self.position) else self.position
        size = self.size() if callable(self.size) else self.size
        

        # Now, unpack the position and size tuples
        pygame.draw.rect(self.screen.screen, self.color, (*position, *size))

        for object in self.objects:
            object.draw()

