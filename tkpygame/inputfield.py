import pygame

from .canvas import Canvas
from .label import Label
from .constants import *
from .utils import print_colored, absolute_position, get_main_canvas
class InputField:
    def __init__(self, canvas: Canvas, placeholder: str = 'Start Typing...', text: str = '', anchor: Anchor = Anchor.TOP_LEFT, size: tuple = (200, 50), font: str = FONT_NAME_PRIMARY, font_size: int = -1, color: str = INPUTFIELD_COLOR_PRIMARY, hover_color: str = INPUTFIELD_COLOR_HOVER_PRIMARY, pressed_color: str = INPUTFIELD_COLOR_TYPING_PRIMARY, name: str = 'input_field', visible=True, padding: tuple = (0, 0), font_color: str = FONT_COLOR_PRIMARY, placeholder_font_color: str = PLACEHOLDER_FONT_COLOR, command='N/A', selected: bool = False):
        self.canvas = canvas
        self.anchor = anchor
        self.padding = padding
        self.size = size
        self.placeholder = placeholder
        self.text = text
        self.font = font
        self.font_size = font_size
        self.font_color = font_color
        self.placeholder_font_color = placeholder_font_color
        self.color = color
        self.hover_color = hover_color
        self.pressed_color = pressed_color
        self.name = name
        self.visible = visible
        self.command = command

        self.selected = selected
        self.text_offset = 0  # Offset for scrolling text
        
        if self.command == 'N/A':
            self.command = lambda: print_colored(f'Input field element <{self.name}> clicked', TerminalColors.INFO)

        if self not in canvas.objects:
            canvas.objects.append(self)

        self.position = absolute_position(self)
        self.previous_frame_mouse_down = pygame.mouse.get_pressed()[0]

        self.font_obj = pygame.font.SysFont(self.font, self.font_size)

        print_colored(f'New input field element <{self.name}> initiated', TerminalColors.SUCCESS)



    def draw(self):
        # Draw the input field rectangle
        rect_color = self.pressed_color if self.selected else (self.hover_color if self.is_hovered() else self.color)
        pygame.draw.rect(pygame.display.get_surface(), rect_color, (self.position, self.size))

        if pygame.mouse.get_pressed()[0]:
            self.selected = self.is_hovered()

        # Determine the text to render (placeholder or actual text)
        display_text = self.text if self.text else self.placeholder
        text_color = self.font_color if self.text else self.placeholder_font_color
        text_surface = self.font_obj.render(display_text, True, text_color)

        # Handle text overflow and scrolling
        text_width = text_surface.get_width()
        if text_width > self.size[0]:  # If text overflows
            self.text_offset = max(0, text_width - self.size[0]) if self.selected else 0
        else:
            self.text_offset = 0

        # Create a surface to clip the text
        clip_surface = pygame.Surface(self.size)
        clip_surface.fill(rect_color)
        clip_surface.blit(text_surface, (-self.text_offset, 0))

        # Blit the clipped text surface to the main screen
        pygame.display.get_surface().blit(clip_surface, self.position)

    def is_hovered(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        return self.position[0] <= mouse_x <= self.position[0] + self.size[0] and self.position[1] <= mouse_y <= self.position[1] + self.size[1]
