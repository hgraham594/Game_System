import pygame


def initialise_pygame():
    """
    Initialises pygame.
    :return: None
    """
    pygame.init()


def new_clock():
    """
    Create a new pygame clock object.
    :return: a pygame clock object.
    """
    return pygame.time.Clock()


def new_screen(screen_size, screen_name):
    """
    Creates a new pygame screen of the given name and dimensions.
    :param screen_size: [screen_width, screen_height] in pixels.
    :param screen_name: a string.
    :return: (screen, screen_size), where screen is a new pygame screen object.
    """
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption(screen_name)
    return screen, screen_size
