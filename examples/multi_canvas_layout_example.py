from tkpygame import *
import pygame

def get_left_canvas_width(screen: pygame.Surface):
    return screen.get_width() // 3

def get_right_canvas_x_position(screen: pygame.Surface):
    return 2 * (screen.get_width() // 3)

def get_canvas_height(screen: pygame.Surface):
    return screen.get_height()

def main():
    screen = init(screen_width=800, screen_height=600)

    leftcanvas = Canvas(screen, 0, 0, lambda: get_left_canvas_width(screen), lambda: get_canvas_height(screen), 'mycanvasname', color=CANVAS_COLOR_SECONDARY)
    middlecanvas = Canvas(screen, lambda: get_left_canvas_width(screen), 0, lambda: get_left_canvas_width(screen), lambda: get_canvas_height(screen), 'mycanvasname1', color=BLUEISH_COLOR)
    rightcanvas = Canvas(screen, lambda: get_right_canvas_x_position(screen), 0, lambda: get_left_canvas_width(screen), lambda: get_canvas_height(screen), 'mycanvasname2', color=CANVAS_COLOR_SECONDARY)

    leftcanvas_label = Label(leftcanvas, 'LEFT', 'CENTER', (0, 0 ), 0, 0, 'leftcanvaslabel', color=CANVAS_COLOR_SECONDARY)
    middlecanvas_label = Label(middlecanvas, 'MIDDLE', 'CENTER', (0, 0 ), 0, 0, 'middlecanvaslabel', color=BLUEISH_COLOR)
    rightcanvas_label = Label(rightcanvas, 'RIGHT', 'CENTER', (0, 0 ), 0, 0, 'rightcanvaslabel', color=CANVAS_COLOR_SECONDARY)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running
        
        flip()


if __name__ == '__main__':
    main()