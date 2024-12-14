import pygame
from .constants import *
from .utils import print_colored, set_icon_from_base64

class Screen:
    def __init__(self, title: str, size: tuple, objects: list = [], color: str = SCREEN_COLOR_PRIMARY, resizeable: bool = False, fps_limit: int = -1):
        self.title = title
        self.size = size
        self.objects = objects
        self.color = color  
        self.resizeable = resizeable
        self.fps_limit = fps_limit

        self.screen = pygame.display.set_mode(size, pygame.RESIZABLE if resizeable else 0)
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        set_icon_from_base64(TKPYGAME_LOGO_BASE64)

        print_colored(f'New screen element <{self.title}> initiated', TerminalColors.SUCCESS)

    def draw(self):
        self.screen.fill(self.color)

        for object in self.objects:
            object.draw()

    def update(self):
        self.draw()

        self.clock.tick(self.fps_limit)
        pygame.display.update()
