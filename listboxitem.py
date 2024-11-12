import pygame

from .utils import TerminalColors, print_colored
from .constants import *
from .variables import popups, dropdowns


class ListboxItem:
    def __init__(self, canvas, text, x, y, width, height, command=None, right_click_command=None, name=None, color=LISTBOXITEM_COLOR_PRIMARY, hover_color=LISTBOXITEM_COLOR_HOVER_PRIMARY, pressed_color=LISTBOXITEM_COLOR_PRESSED_PRIMARY, selected_color=LISTBOXITEM_COLOR_SELECTED_PRIMARY, hover_selected_color=LISTBOXITEM_COLOR_SELECTED_HOVER_PRIMARY, font_size=24, font_color=TEXT_COLOR, font_name='Segoe UI', forced_state=-1):
        self.canvas = canvas

        self.text = text
        
        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.color = color
        self.hover_color = hover_color
        self.pressed_color = pressed_color
        self.selected_color = selected_color
        self.hover_selected_color = hover_selected_color

        self.font_size = font_size
        self.font_color = font_color
        self.font_name = font_name
        
        if command == None:
            self.command = lambda: print_colored(f'No command set for object <{self.name}>', TerminalColors.FAIL)
        else:
            self.command = command
        
        if right_click_command == None:
            self.right_click_command = lambda: print_colored(f'No right click command set for object <{self.name}>', TerminalColors.FAIL)
        else:
            self.right_click_command = right_click_command

        if name == None:
            self.name = text
        else:
            self.name = name

        self.previous_frame_mouse_down = True
        self.previous_frame_right_mouse_down = True

        if self not in self.canvas.objects:
            self.canvas.objects.append(self)
        
        self.objects = []
        self.text_surface = None

        self.forced_state = forced_state # -1 means the button is free to do whatever it wants, 0 means the button is forced to be in the idle state, 1 means the button is forced to be in the hovering state, and 2 means the button is forced to be in the pressed down state.
    
    def draw(self):
        if len(dropdowns) > 0 or len(popups) > 0:
            if self.forced_state < 0:
                self.forced_state = 0 
        else:
            self.forced_state = -1


        try:
            if self.forced_state == -1:
                if self.canvas.selected_object == self:
                    if self.x < pygame.mouse.get_pos()[0] < self.x + self.width and self.y < pygame.mouse.get_pos()[1] < self.y + self.height:
                        pygame.draw.rect(self.canvas.canvas.screen, self.hover_selected_color, (self.x, self.y, self.width, self.height)) # Selected and hovering
                    else:
                        pygame.draw.rect(self.canvas.canvas.screen, self.selected_color, (self.x, self.y, self.width, self.height)) # Selected
                else:
                    if self.x < pygame.mouse.get_pos()[0] < self.x + self.width and self.y < pygame.mouse.get_pos()[1] < self.y + self.height:
                        if pygame.mouse.get_pressed()[0]:
                            pygame.draw.rect(self.canvas.canvas.screen, self.pressed_color, (self.x, self.y, self.width, self.height)) # Pressed
                            if not self.previous_frame_mouse_down:
                                self.canvas.selected_object = self
                                self.command()
                        else:
                            pygame.draw.rect(self.canvas.canvas.screen, self.hover_color, (self.x, self.y, self.width, self.height)) # Hovering
                    else:
                        pygame.draw.rect(self.canvas.canvas.screen, self.color, (self.x, self.y, self.width, self.height)) # Not hovering

                if self.x < pygame.mouse.get_pos()[0] < self.x + self.width and self.y < pygame.mouse.get_pos()[1] < self.y + self.height and pygame.mouse.get_pressed()[2]:
                    pygame.draw.rect(self.canvas.canvas.screen, self.pressed_color, (self.x, self.y, self.width, self.height))
                    if not self.previous_frame_mouse_down and not self.previous_frame_right_mouse_down:
                        self.canvas.selected_object = self
                        self.right_click_command()
                        
                
            elif self.forced_state == 0:
                pygame.draw.rect(self.canvas.canvas.screen, self.color, (self.x, self.y, self.width, self.height))
            elif self.forced_state == 1:
                pygame.draw.rect(self.canvas.canvas.screen, self.hover_color, (self.x, self.y, self.width, self.height))
            else:
                pygame.draw.rect(self.canvas.canvas.screen, self.selected_color, (self.x, self.y, self.width, self.height))
            
            self.previous_frame_mouse_down = pygame.mouse.get_pressed()[0]
            self.previous_frame_right_mouse_down = pygame.mouse.get_pressed()[2]

            # Draw the text
            self.update_text_surface()
            text_rect = self.text_surface.get_rect()
            text_rect.center = (self.x + self.text_surface.get_width() / 2, self.y + self.text_surface.get_height() / 2)
            self.canvas.canvas.screen.blit(self.text_surface, text_rect)
        except Exception as e:
            print_colored(f'Error in ListboxItem.draw(): {e}', TerminalColors.FAIL)
        

    def update_text_surface(self):
        if not hasattr(self, '_font') or self._font is None:
            self._font = pygame.font.SysFont(self.font_name, self.font_size)
        removed_characters = 0

        text_surface = self._font.render(str(self.text), True, self.font_color)
        text_rect = text_surface.get_rect()


        while text_rect.width +5 > self.width:
            removed_characters += 1
            text_surface = self._font.render(str(self.text)[:-removed_characters]+"...", True, self.font_color)
            text_rect = text_surface.get_rect()

        self.text_surface = text_surface

"""
def update_text_surface(self):
    if not hasattr(self, '_font') or self._font is None:
        self._font = pygame.font.SysFont(self.font_name, self.font_size)
    text_surface = self._font.render(str(self.text), True, self.font_color)
    self.width, self.height = text_surface.get_width(), text_surface.get_height()

    self.text_surface = text_surface

"""