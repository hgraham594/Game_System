import pygame
import os

# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)


def get_font_dir_location():
    s = os.path.dirname(os.path.abspath(__file__))
    s2 = s.partition("Display")
    return ''.join([s2[0], "resources\\fonts\\"])


def get_font(font_name, size):
    font_dir_location = get_font_dir_location()
    if font_name == 'Comic Sans':
        return pygame.font.Font(''.join([font_dir_location, 'comic.ttf']), size)
    if font_name == 'Calibri':
        return pygame.font.Font(''.join([font_dir_location, 'calibri.ttf']), size)
    if font_name == 'Lucida Console':
        return pygame.font.Font(''.join([font_dir_location, 'lucon.ttf']), size)
    return pygame.font.SysFont('Calibri', size, True, False)


def draw_new_text(text, font, colour, screen, center_point):
    text_surface = font.render(text, True, colour)  # create a surface object containing the desired text
    text_rect = text_surface.get_rect()  # create a rectangle of the text_surface area, with position 0,0
    text_rect.center = (center_point[0], center_point[1])  # move the rectangle to the desired position (not on screen)
    screen.blit(text_surface, text_rect)  # blit the text onto the rectangle's position onto the screen


def get_rectangle(text, font, colour, center_point):
    text_surface = font.render(text, True, colour)  # create a surface object containing the desired text
    text_rect = text_surface.get_rect()  # create a rectangle of the text_surface area, with position 0,0
    text_rect.center = (center_point[0], center_point[1])  # move the rectangle to the desired position (not on screen)
    return text_rect
