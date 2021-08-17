import pygame
pygame.init()

import math

background_colour = (21,21,21)
caption = "Slice.py"
fps = 30
screen_size = [900, 600]
scale_amount = 1
fpsClock = pygame.time.Clock()
window = pygame.display.set_mode((screen_size[0], screen_size[1]))
screen = pygame.Surface((math.ceil(screen_size[0]/scale_amount),math.ceil(screen_size[1]/scale_amount)))


def run(update=None):
    """
    Create a new screen. \n
    `awake` : this is called once before a screen loop starts
    `update` : this takes a function and calls after refreshing the screen
    `late_update` : this is called after the update method is called
    """
    pygame.display.set_caption(caption)
    Update = update
    while 1:
        window.fill(background_colour)
        if update:
            Update()
        window.blit(pygame.transform.scale(screen, (screen.get_width()*scale_amount, screen.get_height()* scale_amount)), (0, 0))
        pygame.display.update()
        fpsClock.tick(fps)

       

