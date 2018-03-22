from retro_games.setup_for_pygame import *
from retro_games.snake.play import *
from retro_games.snake.home_screen import *


def main():
    # Initialise pygame.
    initialise_pygame()

    screen = new_screen((800, 800), "Snake")
    clock = new_clock()

    next_screen = 'Home Screen'
    quit_status = False
    while not quit_status:
        # --- Main event loop
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                quit_status = True

        if next_screen == 'Home Screen':
            quit_status, next_screen = open_home_screen(screen, clock)
        # Add more screen checks here...

        if next_screen == 'PLAY':
            speed = 0.1
            quit_status, score, next_screen = play_snake(speed, screen, clock)

        if next_screen == 'RULES':  # TODO: create a rules page.
            quit_status = True

        if next_screen == 'HIGH SCORES' and quit_status is not True:  # TODO: create a high scores page.
            quit_status = True

    pygame.quit()


if __name__ == '__main__':
    main()
