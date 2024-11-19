from tkpygame import *

def main():
    import pygame

    screen, clock = init(screen_width=800, screen_height=600)
    variables.clock = clock
    canvas = Canvas(screen, 0, 0, 800, 600, 'mycanvasname')
    label = Label(canvas, 'Hello, world!', 'center', (0, 0), 100, 50, 'mylabelname')
    label2 = Label(canvas, 'This is a test to test the performance of tkpygame!', 'center', (0, 70), 100, 50, 'mylabelname')
    fps_label = Label(canvas, 'FPS: ', 'NW', (0, 0), 0, 0, 'myfpslabel')

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        fps_label.text = "FPS: " + str(clock.get_fps()) 
        fps_label.update_text_surface()

        flip(clock)

if __name__ == '__main__':
    main()
