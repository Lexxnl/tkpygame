from .constants import *
import base64
from PIL import Image
from io import BytesIO
import pygame

def print_colored(text, color=TerminalColors.WHITE, only_if_not_debugging=True):
    result = color + str(text) + TerminalColors.ENDC
    if "New canvas " in str(text):
        result = "\n\n" + result + "\n"
    print(result)

def get_main_canvas(obj):
    # If the object has no canvas attribute or it is None, return the object itself
    if not hasattr(obj, 'canvas') or obj.canvas is None:
        return obj
    # Otherwise, recursively call the function on the canvas
    return get_main_canvas(obj.canvas)

def absolute_position(element):
    # Check if element.size is callable (i.e., a lambda function)
    if callable(element.size):
        element_width, element_height = element.size()  # Call the lambda to get size
    else:
        element_width, element_height = element.size  # Use the tuple directly
    
    # Check if element.canvas.size is callable (it might be a method or property)
    
    if hasattr(element, 'canvas'):
        if callable(element.canvas.size):
            canvas_width, canvas_height = element.canvas.size()  # Call if it's a method
        else:
            canvas_width, canvas_height = element.canvas.size  # Otherwise, it's a tuple
        x, y = element.canvas.position
    else:
        print(f"Warning: element.canvas is None or not defined for <{element.name}>")
        canvas_width, canvas_height = element.screen.size
        x, y = 0, 0
    

    
    
    # Apply anchor-based positioning
    if element.anchor == Anchor.TOP_LEFT:
        x += element.padding[0]
        y += element.padding[1]
    elif element.anchor == Anchor.TOP_RIGHT:
        x += canvas_width - element_width - element.padding[0]
        y += element.padding[1]
    elif element.anchor == Anchor.BOTTOM_LEFT:
        x += element.padding[0]
        y += canvas_height - element_height - element.padding[1]
    elif element.anchor == Anchor.BOTTOM_RIGHT:
        x += canvas_width - element_width - element.padding[0]
        y += canvas_height - element_height - element.padding[1]
    elif element.anchor == Anchor.CENTER:
        x += (canvas_width - element_width) / 2 + element.padding[0]
        y += (canvas_height - element_height) / 2 + element.padding[1]
    elif element.anchor == Anchor.LEFT:
        x += element.padding[0]
        y += (canvas_height - element_height) / 2
    elif element.anchor == Anchor.RIGHT:
        x += canvas_width - element_width - element.padding[0]
        y += (canvas_height - element_height) / 2
    elif element.anchor == Anchor.TOP:
        x += (canvas_width - element_width) / 2 + element.padding[0]
        y += element.padding[1] 
    elif element.anchor == Anchor.BOTTOM:
        x += (canvas_width - element_width) / 2 + element.padding[0]
        y += canvas_height - element_height - element.padding[1]

    return x, y

def set_icon_from_base64(base64_string):
    icon_data = base64.b64decode(base64_string)
    image = Image.open(BytesIO(icon_data))
    image = image.convert('RGBA')  # Ensure image has an alpha channel
    mode = image.mode
    size = image.size
    data = image.tobytes()

    icon_surface = pygame.image.frombuffer(data, size, mode)
    pygame.display.set_icon(icon_surface)