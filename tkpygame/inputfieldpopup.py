import pygame

from constants import *
from button import Button
from inputfield import InputField
from utils import print_colored, TerminalColors
import variables


class InputfieldPopup:
    def __init__(self, screen: pygame.display, title: str, width: int, height: int, name: str, color: str = CANVAS_COLOR_PRIMARY, font_name='Segoe UI', title_font_size=28, text_font_size=16, text='', title_text_offset_x : int = 0, title_text_offset_y : int = 20, done_button_text : str = 'Done', end_command=None, inputfield_text=''):
        self.title = title
        self.name = name
        self.screen = screen

        self.objects = []

        self.width = width
        self.height = height
        self._width = width

        self.font_name = font_name
        self.text_font_size = text_font_size
        self.title_font_size = title_font_size
        self.font_color = TEXT_COLOR
        self.text = text

        self.title_text_offset_x = title_text_offset_x
        self.title_text_offset_y = title_text_offset_y

        self.x = screen.get_width()/2 - self.width/2
        self.y = screen.get_height()/2 - self.height/2

        self.color = color
        
        if end_command == None:
            self.end_command = lambda: print_colored(f'InputfieldPopup <{self.name}> has self.end_command set to None', TerminalColors.RED)
        else:
            self.end_command = end_command


        self.done_button = Button(self, done_button_text, 'SE', (10, 10), 0, 0, f'inputfield-popup-{name}-button', lambda: self.stop_taking_input(), set_height_to_text_rect_height=True, set_width_to_text_rect_width=True)
        self.inputfield = InputField(self, 'N', (0, 100), 250, 50, f'inputfield-popup-{name}-inputfield', command=lambda: self.stop_taking_input(), text=inputfield_text)
        self.inputfield.on_clicked_command = self.set_inputfield_clicked_command

        variables.selected_input_field = self.inputfield
        
        self.update_title_surface()
        self.update_text_surface()

        variables.popups.append(self)

        print_colored(f'New object <{self.name}> on canvas <{self.screen}> initiated', TerminalColors.OKGREEN)
    
    def set_inputfield_clicked_command(self):
        variables.selected_input_field = self.inputfield

    def draw(self):
        # Draw the background
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
        
        self.done_button.draw()
        
        self.inputfield.draw()
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

    def take_input(self):
        pass

    def stop_taking_input(self):
        variables.popups = []
        variables.selected_input_field = None
        self.end_command()

