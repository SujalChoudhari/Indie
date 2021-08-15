import pygame
import math

class Main:
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)
    black = (0, 0, 0)
    background_colour = white
    caption = "Slice.py"
    fps = 30
    screen_size = [900, 600]
    scale_amount = 1
    fpsClock = pygame.time.Clock()
    window = pygame.display.set_mode((screen_size[0], screen_size[1]))
    screen = pygame.Surface((math.ceil(screen_size[0]/scale_amount),math.ceil(screen_size[1]/scale_amount)))
