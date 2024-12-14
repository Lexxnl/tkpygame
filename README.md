# tkpygame

`tkpygame` is a Python package that combines Tkinter and Pygame functionality to enable enhanced GUI components and graphics rendering within Python applications. The package provides pre-built components, utilities, and color formatting options to facilitate a streamlined development experience.

## Features

- **Custom GUI Components**: Easily use components like buttons, dropdowns, input fields, and more with additional customization.
- **Base64 Icon Handling**: Set application icons from base64-encoded images.
- **Pygame Integration**: Allows for creating, rendering, and managing Pygame components within a Tkinter environment.
- **Utilities**: Provides utilities for layout management, color formatting, and canvas updates.

## Installation

You can install `tkpygame` via pip:

```bash
pip install tkpygame
```

Make sure you have Python 3.6 or later.

## Dependencies

`tkpygame` requires the following external libraries, which are installed automatically with `pip`:

- `pygame`: Used for graphics rendering.
- `Pillow`: Used for handling images, especially for loading and converting images in base64 format.

## Usage

Here's a quick example to get you started. This assumes you have installed `tkpygame`.

### Example

```python
from tkpygame import *
from tkpygame.button import Button

# Function to be executed when the button is clicked
def on_button_click():
    print("Button clicked!")

def get_screen_size():
    return my_screen.size

# Initialize the screen and canvas
my_screen = Screen(title='My Screen', size=(800, 600), resizeable=True)
my_canvas = Canvas(screen=my_screen, size=(lambda: get_screen_size()), name='my_canvas', visible=True)

# Initialize labels
top_left_label = Label(canvas=my_canvas, text='TOP LEFT', anchor=Anchor.TOP_LEFT, padding=(10, 10))
top_label = Label(canvas=my_canvas, text='TOP', anchor=Anchor.TOP, padding=(10, 10))
top_right_label = Label(canvas=my_canvas, text='TOP RIGHT', anchor=Anchor.TOP_RIGHT, padding=(10, 10))

center_right_label = Label(canvas=my_canvas, text='CENTER RIGHT', anchor=Anchor.RIGHT, padding=(10, 10))
bottom_right_label = Label(canvas=my_canvas, text='BOTTOM RIGHT', anchor=Anchor.BOTTOM_RIGHT, padding=(10, 10))
bottom_label = Label(canvas=my_canvas, text='BOTTOM', anchor=Anchor.BOTTOM, padding=(10, 10))

bottom_left_label = Label(canvas=my_canvas, text='BOTTOM LEFT', anchor=Anchor.BOTTOM_LEFT, padding=(10, 10))
center_left_label = Label(canvas=my_canvas, text='CENTER LEFT', anchor=Anchor.LEFT, padding=(10, 10))
center_label = Label(canvas=my_canvas, text='CENTER', anchor=Anchor.CENTER)

fps_label = Label(canvas=my_canvas, text='FPS: ', anchor=Anchor.TOP_LEFT, font='arial', font_size=18, font_color='green', name='fps_label')


# Create the button
my_button = Button(
    canvas=my_canvas, 
    text="Click Me", 
    padding=(200, 200)
)

fps_label = Label(canvas=my_canvas, text='FPS: ', anchor=Anchor.TOP_LEFT, font='arial', font_size=18, font_color='green', name='fps_label')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE:
            my_canvas.size = (event.w, event.h)
            for object in my_canvas.objects:
                object.position = absolute_position(object)
                
    fps_label.text = f'FPS: {my_screen.clock.get_fps()}'
    fps_label.update_text_surface()


    my_screen.update()

pygame.quit()

```

### Components Overview

- **Canvas**: A Tkinter canvas with added methods for positioning and rendering Pygame visuals.
- **Button**: A customizable button component with text and styling options.
- **Dropdown**: A dropdown selection component.
- **InputField**: A text input field with a placeholder.
- **Label**: A label component with color and font styling.
- **Listbox** and **ListboxItem**: Components for displaying lists of items.
- **Popup**: A modal popup component for displaying messages or custom content.
- **ImageButton**: A button component that uses an image as its icon.

### Utility Functions

- `set_icon_from_base64(base64_string)`: Sets the application icon using a base64-encoded image string.
- `print_colored(text, color)`: Prints text to the terminal with ANSI color codes.

### Layout Utilities

- `update_canvas_rect(canvas)`: Updates canvas dimensions based on dynamic size attributes.
- `update_rect(obj)`: Updates an object’s dimensions and position based on its parent canvas properties.

## Terminal Colors

The package provides the `TerminalColors` class with predefined color codes to enable colorful terminal output. Here’s an example:

```python
from tkpygame import TerminalColors, print_colored

print_colored("This is a warning message", TerminalColors.WARNING)
print_colored("This is an error message", TerminalColors.FAIL)
```

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
