from retro_games.Display.display_manager import *


def draw_buttons(mouse_position, screen, _button_font, text, button_midpoints):
    for i in range(len(button_midpoints)):
        button = get_rectangle(text[i], _button_font, white, button_midpoints[i])
        if button.collidepoint(mouse_position):
            draw_new_text(text[i], _button_font, red, screen, button_midpoints[i])
        else:
            draw_new_text(text[i], _button_font, green, screen, button_midpoints[i])


def check_buttons_clicked(mouse_position, _button_font, text, button_midpoints):
    for i in range(len(button_midpoints)):
        button = get_rectangle(text[i], _button_font, white, button_midpoints[i])
        if button.collidepoint(mouse_position):
            return text[i]


def open_home_screen(_screen, clock):
    button_height = 50
    title_font = get_font('Comic Sans', 150)
    button_font = get_font('Lucida Console', button_height)

    screen = _screen[0]
    screen_size = _screen[1]

    # Image variables
    segment_size = 40
    apple_size = 40
    snake = [[(screen_size[0] / 2), (screen_size[1] / 2) - 10],
             [(screen_size[0] / 2) - segment_size, (screen_size[1] / 2) - 10],
             [(screen_size[0] / 2) - segment_size*2, (screen_size[1] / 2) - 10],
             [(screen_size[0] / 2) - segment_size*3, (screen_size[1] / 2) - 10],
             [(screen_size[0] / 2) - segment_size*4, (screen_size[1] / 2) - 10],
             [(screen_size[0] / 2) - segment_size*5, (screen_size[1] / 2) - 10]]
    apple_pos = [(screen_size[0] / 2) + 4*segment_size, (screen_size[1] / 2) - 10]

    title_midpoint = [screen_size[0] / 2, screen_size[1] / 4]
    button_names = ['PLAY', 'RULES', 'HIGH SCORES', 'SETTINGS']
    button_midpoints = []
    for i in range(len(button_names)):
        button_midpoints.append([screen_size[0]/2, screen_size[1] * (2/3) + button_height*i])

    quit_status = False
    done = False
    next_screen = None

    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                quit_status = True
                done = True  # Flag that we are done so we exit this loop
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_position = pygame.mouse.get_pos()
                next_screen = check_buttons_clicked(mouse_position, button_font, button_names, button_midpoints)
                if next_screen is not None:
                    done = True

        # --- Game logic should go here
        mouse_position = pygame.mouse.get_pos()

        # --- Screen-clearing code goes here
        screen.fill(black)
        draw_new_text("SNAKE", title_font, green, screen, title_midpoint)
        draw_buttons(mouse_position, screen, button_font, button_names, button_midpoints)

        # --- Drawing code should go here
        for i in range(len(snake)):
            pygame.draw.rect(screen, green, [snake[i][0], snake[i][1], segment_size-1, segment_size-1])
        pygame.draw.rect(screen, red, [apple_pos[0], apple_pos[1], apple_size-1, apple_size-1])

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

    return quit_status, next_screen
