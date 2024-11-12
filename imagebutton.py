import pygame
import base64
from io import BytesIO
from PIL import Image

from .utils import TerminalColors, print_colored, update_rect
from .constants import *

class ImageButton:
    def __init__(self, canvas, anchor, padding, width: int, height: int, name: str, command, base64_image=None, color=BUTTON_COLOR_PRIMARY, hover_color=BUTTON_COLOR_HOVER_PRIMARY, pressed_color=BUTTON_COLOR_PRESSED_PRIMARY, visible=True):
        self.canvas = canvas
        self.anchor = anchor
        self.padding = padding
        self.width = width
        self.height = height
        self.color = color
        self.hover_color = hover_color
        self.pressed_color = pressed_color
        self.command = command
        self.name = name

        self.base64_image = base64_image
        self.image_surface = None
        
        self.visible = visible

        # Decode the base64 image if provided
        if self.base64_image:
            self.image_surface = self.decode_image(self.base64_image)
            if self.image_surface:
                # Now the size is determined by the user-specified width and height
                self.width, self.height = self.image_surface.get_size()

        if self.canvas is not None:
            self.canvas.objects.append(self)
            print_colored(f'New object <{self.name}> on canvas <{self.canvas.name}> initiated', TerminalColors.OKGREEN)

            update_rect(self)

        self.previous_frame_mouse_down = True

    def decode_image(self, base64_str):
        """Decodes base64 string into a Pygame surface and resizes it to the button's width and height"""
        image_data = base64.b64decode(base64_str)
        image = Image.open(BytesIO(image_data))
        image = image.convert('RGBA')  # Convert to a format Pygame understands

        # Resize the image to match the button's width and height
        image = image.resize((self.width, self.height), Image.Resampling.LANCZOS)  # Use LANCZOS for high-quality resizing

        # Convert the resized image to a Pygame surface
        mode = image.mode
        size = image.size
        data = image.tobytes()

        return pygame.image.fromstring(data, size, mode)

    def draw(self):
        if self.visible:
            """Handles drawing the button, including hover and pressed states"""
            if self._x < pygame.mouse.get_pos()[0] < self._x + self._width and self._y < pygame.mouse.get_pos()[1] < self._y + self._height:
                if pygame.mouse.get_pressed()[0]:
                    # Button is being pressed
                    pygame.draw.rect(self.canvas.screen, self.pressed_color, (self._x, self._y, self._width, self._height))

                    if not self.previous_frame_mouse_down:
                        self.command()  # Trigger command on click
                else:
                    # Hover effect
                    pygame.draw.rect(self.canvas.screen, self.hover_color, (self._x, self._y, self._width, self._height))
            else:
                # Default state
                pygame.draw.rect(self.canvas.screen, self.color, (self._x, self._y, self._width, self._height))

            # Draw the image on the button (if available)
            if self.image_surface:
                self.canvas.screen.blit(self.image_surface, (self._x, self._y))

            self.previous_frame_mouse_down = pygame.mouse.get_pressed()[0]  # Update state
