import pygame

from .utils import TerminalColors, print_colored, update_rect
from .constants import *
from .variables import selected_input_field

class InputField:
    def __init__(self, canvas, anchor, padding, width, height, name, command=None, on_clicked_command=None, text_offset_x=0, text_offset_y=0, color=INPUTFIELD_COLOR_PRIMARY, hover_color=INPUTFIELD_COLOR_HOVER_PRIMARY, typing_color=INPUTFIELD_COLOR_TYPING_PRIMARY, text_color=TEXT_COLOR, font_size=24, font_name='Segoe UI', text='', set_width_to_text_rect_width=False, visible=True, selected=False):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.color = color
        self.text_color = text_color
        self.font_size = font_size
        self.font_name = font_name
        self.name = name
        self.hover_color = hover_color
        self.typing_color = typing_color
        self.text = text
        self.anchor = anchor
        self.padding = padding
        self.text_offset_x = text_offset_x
        self.text_offset_y = text_offset_y
        self.set_width_to_text_rect_width = set_width_to_text_rect_width

        self.canvas.objects.append(self)

        if command == None:
            self.command = lambda: print_colored(f'No command set for object <{self.name}>', TerminalColors.FAIL)
        else:
            self.command = command
        
        if on_clicked_command == None:
            self.on_clicked_command = lambda: print_colored(f'No on_clicked command set for object <{self.name}>', TerminalColors.FAIL)
        else:
            self.on_clicked_command = on_clicked_command

        self.visible = visible
        self.selected = selected

        if self.canvas != None:
            if self not in self.canvas.objects:
                self.canvas.objects.append(self)
            print_colored(f'New object <{self.name}> on canvas <{self.canvas.name}> initiated', TerminalColors.OKGREEN)

            update_rect(self)

        self.previous_frame_mouse_down = True
        self.update_text_surface()

    def draw(self):
        self.selected = selected_input_field == self
        if callable(self.visible):
            self._visible = self.visible()
        else:
            self._visible = self.visible
        
        if self._visible:
            # Draw the input field
            if self.selected:
                pygame.draw.rect(self.canvas.screen, self.typing_color, (self._x, self._y, self._width, self._height))
                if pygame.mouse.get_pressed()[0] and self.previous_frame_mouse_down == False and not(self._x < pygame.mouse.get_pos()[0] < self._x + self._width and self._y < pygame.mouse.get_pos()[1] < self._y + self._height):
                    self.command()
                    self.selected = False
            else: 
                if self._x < pygame.mouse.get_pos()[0] < self._x + self._width and self._y < pygame.mouse.get_pos()[1] < self._y + self._height:
                    if pygame.mouse.get_pressed()[0]:
                        pygame.draw.rect(self.canvas.screen, self.typing_color, (self._x, self._y, self._width, self._height))
                        self.on_clicked_command() # Set this inputfield to selected, change the previous selected inputfield to unselected
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
        text_surface = self._font.render(str(self.text), True, self.text_color)
        self.text_rect = text_surface.get_rect()
        
        self.text_rect.center = (self._x + text_surface.get_width() / 2 + self.text_offset_x, self._y + text_surface.get_height() / 2 + self.text_offset_y)
        self.canvas.screen.blit(text_surface, self.text_rect)

        if self.set_width_to_text_rect_width:
            self.width = text_surface.get_width()
            update_rect(self)
