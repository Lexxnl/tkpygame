from tkpygame import *  # Import all modules and functions from tkpygame library for GUI and event handling

# Function to toggle the visibility of a label when called
def change_label_visible_on_click(label):
    label.visible = not label.visible  # Switch the label's visibility state

# Main function to initialize and run the GUI application
def main():
    # Initialize the main screen with specified width and height
    screen, clock = init(screen_width=800, screen_height=600)
    
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
