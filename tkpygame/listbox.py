import pygame

from .canvas import Canvas
from .label import Label
from .screen import Screen
from .constants import *
from .utils import print_colored, absolute_position

class ListBox():
    def __init__(self, canvas: Canvas, title: str = 'ListBox', anchor=Anchor.TOP_LEFT, padding: tuple = (0, 0), 
                 size: tuple = (300, 200), objects: list = [], name: str = 'listbox', color: str = LISTBOX_COLOR_PRIMARY, 
                 font: str = FONT_NAME_PRIMARY, font_size: int = FONT_SIZE_PRIMARY, font_color: str = FONT_COLOR_PRIMARY, 
                 visible: bool = True, grid_columns: int = 2, grid_spacing: tuple = (10, 10)):
        self.canvas = canvas
        self.title = title
        self.anchor = anchor
        self.padding = padding
        self.size = size
        self.objects = objects
        self.name = name
        self.color = color
        self.font = font
        self.font_size = font_size
        self.font_color = font_color
        self.visible = visible
        self.grid_columns = grid_columns  # Number of columns in the grid
        self.grid_spacing = grid_spacing  # Spacing between grid items (horizontal, vertical)

        if self not in canvas.objects:
            canvas.objects.append(self)

        self.position = absolute_position(self)
        self.label = Label(canvas=self, text=self.title, anchor=Anchor.TOP_LEFT, font_size=self.font_size, 
                           font_color=self.font_color, name=f'{self.name}-label', padding=(10, 10))

        print_colored(f'New listbox element <{self.name}> initiated', TerminalColors.SUCCESS)

    def draw(self):
        if self.visible:
            # Draw the listbox background
            pygame.draw.rect(pygame.display.get_surface(), self.color, (*self.position, *self.size))
            
            # Draw the title label
            self.label.draw()

            if len(self.objects) > 1:
                # Start by calculating the maximum number of columns that can fit
                grid = []


                num_columns = 0
                current_total_width = 0
                max_total_width = self.size[0]

                column = []
                for object in self.objects:
                    if object != self.label:
                        if current_total_width + object.size[0] + object.padding[0] * 2 < max_total_width:
                            num_columns += 1
                            current_total_width += object.size[0] + object.padding[0] * 2
                            column.append(object)
                        else:
                            # Object doesnt fit anymore in the column
                            grid.append(column)

                            # New column
                            column = []

                            num_columns = 0
                            current_total_width = 0
                            max_total_width = self.size[0]

                            num_columns += 1
                            current_total_width += object.size[0] + object.padding[0] * 2
                            column.append(object)
                            
                            

                if column not in grid:
                    grid.append(column)
                    

                self.position = absolute_position(self)

                biggest_y_padding = 0
                for object in grid[0]:
                    if object.padding[1] > biggest_y_padding:
                        biggest_y_padding = object.padding[1]

                current_y = self.position[1] + biggest_y_padding
                
                for column in grid:
                    current_x = self.position[0]
                    
                    
                    for object in column:
                        object_index = column.index(object)

                        # Calculate the position of the object
                        current_x += object.padding[0]

                        object.position = (current_x, current_y)
                        object.draw()

                        current_x += object.size[0]
                        current_x += object.padding[0]
                    
                    current_y += biggest_y_padding

                    biggest_y_padding = 0
                    for object in column:
                        if object.padding[1] > biggest_y_padding:
                            biggest_y_padding = object.padding[1]
                    
                    biggest_y = 0
                    for object in column:
                        if object.size[1] > biggest_y:
                            biggest_y = object.size[1]

                    current_y += biggest_y_padding + biggest_y

