import pygame

from .constants import *
from .utils import print_colored, TerminalColors
from .variables import popups


class Popup:
    def __init__(self, screen: pygame.display, title: str, width: int, height: int, objects: list, name: str, color: str = CANVAS_COLOR_PRIMARY, progress_bar_color=BLUEISH_COLOR, progress_bar_color_background: str = CANVAS_COLOR_SECONDARY, font_name='Segoe UI', title_font_size=28, text_font_size=16, text='', progress=0, title_text_offset_x : int = 0, title_text_offset_y : int = 20):
        self.title = title
        self.objects = objects
        self.name = name
        self.screen = screen
    
        self.width = width
        self.height = height

        self.font_name = font_name
        self.text_font_size = text_font_size
        self.title_font_size = title_font_size
        self.font_color = TEXT_COLOR
        self.text = text
        self.progress = progress

        self.title_text_offset_x = title_text_offset_x
        self.title_text_offset_y = title_text_offset_y

        self.x = screen.get_width()/2 - self.width/2
        self.y = screen.get_height()/2 - self.height/2

        self.color = color
        self.progress_bar_color = progress_bar_color
        self.progress_bar_color_background = progress_bar_color_background

        self.update_title_surface()
        self.update_text_surface()

        popups.append(self)

        print_colored(f'New object <{self.name}> on canvas <{self.screen}> initiated', TerminalColors.OKGREEN)

    def draw(self):
        # Draw the background
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

        # progress bar
        pygame.draw.rect(self.screen, self.progress_bar_color_background, (self.x+25, self.y+100, self.width-50, 45))

        pygame.draw.rect(self.screen, self.progress_bar_color, (self.x+25, self.y+100, self.progress * (self.width - 50), 45))
        
        for button in self.objects:
            button._x = (self.x + self.width - button.width) - (button.width + 25) * self.objects.index(button) - 15
            button._y = self.y + self.height - button.height - 15
            button.draw()
        
        # Draw the text

        if self.title_surface != None:
            text_rect = self.title_surface.get_rect()
            text_rect.center = (self.x + self.width/2 + self.title_text_offset_x, self.y + self.title_text_offset_y + text_rect.height/2)
            self.screen.blit(self.title_surface, text_rect)
        else:
            self.update_title_surface()
        
        

    def update_title_surface(self):
        if not hasattr(self, '_font') or self._font is None:
            self._font = pygame.font.SysFont(self.font_name, self.title_font_size)
        title_surface = self._font.render(str(self.title), True, self.font_color)

        self.title_surface = title_surface
    
    def update_text_surface(self):
        if not hasattr(self, '_font') or self._font is None:
            self._font = pygame.font.SysFont(self.font_name, self.text_font_size)
        text_surface = self._font.render(str(self.text), True, self.font_color)

        self.text_surface = text_surface
