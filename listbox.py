import pygame

from .utils import TerminalColors, print_colored, update_rect
from .constants import *
from .label import Label

class Listbox:
    def __init__(self, canvas, text, anchor, padding, width, height, name, color=LISTBOX_COLOR_SECONDARY, font_size=24, font_color=TEXT_COLOR, font_name='Segoe UI', objects=[], selected_object=None):
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
        self.objects = objects
        self.scrolled_distance = 0
        self.selected_object = selected_object
        self.namelabel = Label(self.canvas, self.text, self.anchor, self.padding, self.width, 40, f'listbox-{self.name}-name-label')
        
        if self.canvas != None:
            self.canvas.objects.append(self)
            print_colored(f'New object <{self.name}> on canvas <{self.canvas.name}>', TerminalColors.OKGREEN)

        update_rect(self)

    def draw(self):
        # Get the right positions and sizes of the listbox
        update_rect(self)

        # Draw the listbox
        pygame.draw.rect(self.canvas.screen, self.color, (self._x, self._y, self._width, self._height))

        # Draw the objects
        for object in self.objects:
            object.x = self._x
            object.width = self._width
            object.height = 40

            if self.text != '':
                object.y = self._y + object.height * self.objects.index(object) + 40 + self.scrolled_distance  
            else:
                object.y = self._y + object.height * self.objects.index(object) + self.scrolled_distance

            if object.y + 1 > self._y and object.y:
                object.draw()

        # Draw the text
        if self.text != '':
            self.namelabel.draw()
