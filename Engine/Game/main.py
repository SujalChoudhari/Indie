from Engine.Components.colour import COLOUR
import pygame
import math

class Main:
    background_colour = COLOUR.White
    caption = "Slice.py"
    fps = 30
    screen_size = [900, 600]
    scale_amount = 1
    fpsClock = pygame.time.Clock()
    window = pygame.display.set_mode((screen_size[0], screen_size[1]))
    screen = pygame.Surface((math.ceil(screen_size[0]/scale_amount),math.ceil(screen_size[1]/scale_amount)))
