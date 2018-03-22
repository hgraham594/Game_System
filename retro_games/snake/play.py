import random
import time
from retro_games.Display.display_manager import *


def new_apple_position(screen_size, apple_size, snake):
    """
    Calculates and returns random co-ordinates for a new apple on the screen (avoiding the snake's body).
    :param screen_size: [screen_width, screen_height] in pixels.
    :param apple_size: a positive integer representing the length and width of the square apple.
    :param snake: a list of sub-lists of length 3, where a sub-list is [x_position, y_position, direction].
    :return: x, y: co-ordinates for the new apple.
    """
    empty_space = True
    x = random.randrange(0, screen_size[0], apple_size)
    y = random.randrange(0, screen_size[1], apple_size)
    for i in range(len(snake)):
        if x == snake[i][0] and y == snake[i][1]:
            empty_space = False
    if empty_space is False:
        [x, y] = new_apple_position(screen_size, apple_size, snake)
    return [x, y]


def update_segment_position(segment, segment_size, screen_size):
    """
    Takes a segment of the retro_games, and returns an updated copy of the segment.
    :param segment: a list of length 3.
    :param segment_size: a positive integer.
    :param screen_size: [screen_width, screen_height] in pixels.
    :return: a list of length 3: [x_position, y_position, direction].
    """
    if segment[2] == 'U':
        segment[1] -= segment_size
        if segment[1] <= -segment_size:
            segment[1] = screen_size[1] - segment_size
    elif segment[2] == 'D':
        segment[1] += segment_size
        if segment[1] >= screen_size[1]:
            segment[1] = 0
    elif segment[2] == 'L':
        segment[0] -= segment_size
        if segment[0] <= -segment_size:
            segment[0] = screen_size[0] - segment_size
    else:  # (in which case direction == 'R')
        segment[0] += segment_size
        if segment[0] >= screen_size[0]:
            segment[0] = 0
    return segment


def update_snake_position(snake, segment_size, screen_size):
    """
    Updates the position of the snake based on each segment's current direction.
    :param snake: a list of sub-lists of length 3, where a sub-list is [x_position, y_position, direction].
    :param segment_size: a positive integer.
    :param screen_size: the width and height of the screen, as a list.
    :return: a copy of the updated snake.
    """
    for i in range(len(snake)):
        snake[i] = update_segment_position(snake[i], segment_size, screen_size)
    return snake


def update_snake_directions(snake, input_direction):
    """
    Updates the direction of the each segment of the snake.
    :param snake: a list of sub-lists of length 3, where a sub-list is [x_position, y_position, direction].
    :param input_direction: the new direction to be completed by the head of the snake.
    :return: the updated copy of the snake.
    """
    for i in range(len(snake) - 1, 0, -1):
        snake[i][2] = snake[i - 1][2]
    snake[0][2] = input_direction
    return snake


def add_new_segment(snake, segment_size, screen_size):
    """
    Adds a new segment to the retro_games.
    :param snake: a list of sub-lists of length 3.
    :param segment_size: a positive integer.
    :param screen_size: [screen_width, screen_height] in pixels.
    :return: snake with a sub-list of length 3 appended to its end.
    """
    _direction = snake[-1][2]
    # Make a copy of the tail of the snake.
    new_segment = []
    for j in range(3):
        new_segment.append(snake[-1][j])
    if _direction == 'U':
        new_segment[2] = 'D'
    elif _direction == 'D':
        new_segment[2] = 'U'
    elif _direction == 'L':
        new_segment[2] = 'R'
    else:  # in which case _direction == 'R'
        new_segment[2] = 'L'
    new_segment = update_segment_position(new_segment, segment_size, screen_size)
    new_segment[2] = _direction
    snake.append(new_segment)
    return snake


def check_for_body_crash(snake):
    """
    Checks whether or not the head of the snake has crashed into part of its body.
    :param snake: a list of sub-lists of length 3 representing segments of its body: [x_pos, y_pos, direction].
    :return: True or False.
    """
    for i in range(1, len(snake)):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            return True
    return False


def game_over(screen, screen_size):
    game_over_font = get_font('Comic Sans', 80)
    screen_centre = [screen_size[0] / 2, screen_size[1] / 2]
    draw_new_text("GAME OVER", game_over_font, red, screen, screen_centre)
    pygame.display.flip()
    time.sleep(2)


def play_snake(speed, screen_tuple, clock):
    """
    Runs a play-through of the retro_games game, and returns the final score when game over occurs.
    :param speed: a float representing how long in seconds it takes the retro_games to move forward one unit.
    :param screen_tuple: (screen, (screen_width, screen_height)), where width and height are in pixels.
    :param clock: a pygame clock object used to control the speed the game runs at.
    :return: score: a non-negative integer.
    """
    score_font = get_font('Calibri', 30)

    # The width and length of each segment and the apples are the same, as they will be square.
    segment_size = 40
    apple_size = segment_size
    starting_position = [400, 400]
    # The body of the snake. Each segment of its body: [x_position, y_position].
    snake = [[starting_position[0], starting_position[1], 'R'],
             [starting_position[0] - segment_size, starting_position[1], 'R'],
             [starting_position[0] - segment_size*2, starting_position[1], 'R'],
             [starting_position[0] - segment_size*3, starting_position[1], 'R'],
             [starting_position[0] - segment_size*4, starting_position[1], 'R'],
             [starting_position[0] - segment_size*5, starting_position[1], 'R']]
    input_direction = 'R'
    score = 0
    screen_size = screen_tuple[1]
    screen = screen_tuple[0]
    apple_position = new_apple_position(screen_size, apple_size, snake)  # Location of the apple.

    next_screen = None
    quit_status = False
    done = False
    while not done:
        # -----------------------
        # --- Main Event Loop ---
        # -----------------------
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                quit_status = True
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if input_direction != 'D':
                        input_direction = 'U'
                elif event.key == pygame.K_DOWN:
                    if input_direction != 'U':
                        input_direction = 'D'
                elif event.key == pygame.K_LEFT:
                    if input_direction != 'R':
                        input_direction = 'L'
                elif event.key == pygame.K_RIGHT:
                    if input_direction != 'L':
                        input_direction = 'R'

        # ---------------------------------
        # --- Game logic should go here ---
        # ---------------------------------
        snake = update_snake_directions(snake, input_direction)
        snake = update_snake_position(snake, segment_size, screen_size)
        # Check if the snake ate the apple.
        if snake[0][0] == apple_position[0] and snake[0][1] == apple_position[1]:
            apple_position = new_apple_position(screen_size, apple_size, snake)
            score += 1
            snake = add_new_segment(snake, segment_size, screen_size)
        if check_for_body_crash(snake):
            game_over(screen, screen_size)
            next_screen = 'Home Screen'
            done = True

        # Set the speed of the snake.
        time.sleep(speed)

        # ------------------
        # --- Background ---
        # ------------------
        screen.fill(black)
        score_text = score_font.render("Score: " + str(score), True, green)
        screen.blit(score_text, [0, 0])

        # -----------------------------------
        # --- Drawing code should go here ---
        # -----------------------------------
        # Draw the snake.
        for i in range(len(snake)):
            pygame.draw.rect(screen, green, [snake[i][0], snake[i][1], segment_size-1, segment_size-1])

        # Draw the apple.
        pygame.draw.rect(screen, red, [apple_position[0], apple_position[1], apple_size-1, apple_size-1])

        # ------------------------------------------------------------
        # --- Go ahead and update the screen with what we've drawn ---
        # ------------------------------------------------------------
        pygame.display.flip()

        # -------------------------------------
        # --- Limit to 60 frames per second ---
        # -------------------------------------
        clock.tick(60)

    if quit_status is True:
        pygame.quit()

    return quit_status, score, next_screen
