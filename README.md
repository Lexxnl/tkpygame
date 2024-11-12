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
from tkpygame import *  # Import all modules and functions from tkpygame library for GUI and event handling

# Function to toggle the visibility of a label when called
def change_label_visible_on_click(label):
    label.visible = not label.visible  # Switch the label's visibility state

# Main function to initialize and run the GUI application
def main():
    # Initialize the main screen with specified width and height
    screen = init(screen_width=800, screen_height=600)
    
    # Create a canvas that covers the entire screen area for holding GUI elements
    canvas = Canvas(screen, 0, 0, 800, 600, 'mycanvasname')
    
    # Add a label to the canvas; initially hidden
    # - Positioned 60 pixels below the center (0, 60)
    # - Size is 100x50 pixels
    label = Label(canvas, 'Hello, world!', 'center', (0, 60), 100, 50, 'mylabelname', visible=False)
    
    # Add a button to the canvas; when clicked, it toggles the label visibility
    # - Positioned at the center of the canvas (0, 0)
    # - Size is 100x50 pixels
    button = Button(canvas, 'Click me!', 'center', (0, 0), 100, 50, 'mybuttonname', 
                    lambda: change_label_visible_on_click(label))

    # Main event loop to keep the application running
    running = True
    while running:
        # Process each event in the event queue
        for event in pygame.event.get():
            # Check if the close button on the window is clicked
            if event.type == pygame.QUIT:
                running = False  # End the loop to close the application

        # Update the display to render any changes on the screen
        flip()

# Entry point of the program
if __name__ == '__main__':
    main()

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
