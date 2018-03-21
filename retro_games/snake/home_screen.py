from Display.display_manager import *


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
    title_font = get_font('Comic Sans', 100)
    button_font = get_font('Lucida Console', 30)

    screen = _screen[0]
    screen_size = _screen[1]

    snake = [[(screen_size[0] / 2), (screen_size[1] / 2) - 10],
             [(screen_size[0] / 2) - 20, (screen_size[1] / 2) - 10],
             [(screen_size[0] / 2) - 40, (screen_size[1] / 2) - 10],
             [(screen_size[0] / 2) - 60, (screen_size[1] / 2) - 10],
             [(screen_size[0] / 2) - 80, (screen_size[1] / 2) - 10],
             [(screen_size[0] / 2) - 100, (screen_size[1] / 2) - 10]]
    apple_x, apple_y = [(screen_size[0] / 2) + 80, (screen_size[1] / 2) - 10]  # Location of the apple

    title_midpoint = [screen_size[0] / 2, screen_size[1] / 4]
    play_midpoint = [screen_size[0] / 2, screen_size[1] * (2 / 3)]
    rule_midpoint = [screen_size[0] / 2, screen_size[1] * (2 / 3) + 35]
    high_score_midpoint = [screen_size[0] / 2, screen_size[1] * (2 / 3) + 70]
    button_midpoints = [play_midpoint, rule_midpoint, high_score_midpoint]
    button_names = ['PLAY', 'RULES', 'HIGH SCORES']

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
            pygame.draw.rect(screen, green, [snake[i][0], snake[i][1], 19, 19])
        pygame.draw.rect(screen, red, [apple_x, apple_y, 19, 19])

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

    return quit_status, next_screen
