import pygame
import base64
from io import BytesIO

from .canvas import Canvas
from .label import Label
from .constants import *
from .utils import print_colored, absolute_position, get_main_canvas

class Button:
    def __init__(self, canvas: Canvas, text: str, anchor: Anchor = Anchor.TOP_LEFT, size: tuple = (200, 50), font: str = FONT_NAME_PRIMARY, font_size: int = FONT_SIZE_PRIMARY, color: str = BUTTON_COLOR_PRIMARY, hover_color: str = BUTTON_COLOR_HOVER_PRIMARY, pressed_color: str = BUTTON_COLOR_PRESSED_PRIMARY, name: str = 'button', visible: bool = True, padding: tuple = (0, 0), font_color: str = FONT_COLOR_PRIMARY, command='N/A', icon: str = '', icon_width: int = 32, icon_height: int = 34):
        self.canvas = canvas
        self.anchor = anchor
        self.padding = padding

        self.size = size

        self.text = text    
        self.font = font
        self.font_size = font_size
        self.font_color = font_color
        self.color = color
        self.hover_color = hover_color
        self.pressed_color = pressed_color
        self.name = name
        self.visible = visible

        self.icon = icon  # Base64 string of the icon
        self.icon_width = icon_width
        self.icon_height = icon_height

        self.command = command
        if self.command == 'N/A':
            self.command = lambda: print_colored(f'Button element <{self.name}> clicked', TerminalColors.INFO)

        if not self in canvas.objects:
            canvas.objects.append(self)

        self.position = absolute_position(self)
        self.label = Label(canvas=self, text=self.text, anchor=Anchor.CENTER, font_size=self.font_size, font_color=self.font_color, name=f'{self.name}-label')

        self.rect = pygame.Rect(self.position, self.size)

        # Load and scale the icon if provided
        self.icon_surface = None
        if self.icon:
            self.icon_surface = self.load_icon(self.icon)

        self.previous_frame_mouse_down = pygame.mouse.get_pressed()[0]

        print_colored(f'New button element <{self.name}> initiated', TerminalColors.SUCCESS)

    def load_icon(self, base64_string: str):
        """Load and scale an image from a base64 string."""
        try:
            # Decode the base64 string and load the image
            icon_data = base64.b64decode(base64_string)
            icon_image = pygame.image.load(BytesIO(icon_data))

            # Resize the icon to the specified width and height
            icon_image = pygame.transform.scale(icon_image, (self.icon_width, self.icon_height))

            return icon_image
        except Exception as e:
            print_colored(f"Error loading icon: {e}", TerminalColors.ERROR)
            return None

    def draw(self):
        # Draw the button background based on mouse position and click state
        if self.position[0] < pygame.mouse.get_pos()[0] < self.position[0] + self.size[0] and self.position[1] < pygame.mouse.get_pos()[1] < self.position[1] + self.size[1]:
            if pygame.mouse.get_pressed()[0]:
                pygame.draw.rect(pygame.display.get_surface(), self.pressed_color, (self.position, self.size))
                if not self.previous_frame_mouse_down:
                    self.command()
            else:
                pygame.draw.rect(pygame.display.get_surface(), self.hover_color, (self.position, self.size))
        else:
            pygame.draw.rect(pygame.display.get_surface(), self.color, (self.position, self.size))

        # If an icon exists, draw it before the text
        if self.icon_surface:
            icon_width, icon_height = self.icon_surface.get_size()
            icon_x_padding = (self.size[1] - icon_height) / 2
            icon_x = self.position[0] + icon_x_padding
            icon_y = self.position[1] + (self.size[1] - icon_height) // 2  # Vertically center the icon

            pygame.display.get_surface().blit(self.icon_surface, (icon_x, icon_y))

            self.label.anchor = Anchor.LEFT
            self.label.padding = (icon_width + icon_x_padding * 2, self.label.padding[1])
        self.label.position = absolute_position(self.label)
            
        self.label.draw()

        self.previous_frame_mouse_down = pygame.mouse.get_pressed()[0]
