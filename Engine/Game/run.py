import pygame
from Engine.Game.main import *
pygame.init()


game = Main()
def Screen(awake=None, update=None, late_update=None, input=None):
    """
    Create a new screen. \n
    `awake` : this is called once before a screen loop starts
    `update` : this takes a function and calls after refreshing the screen
    `late_update` : this is called after the update method is called
    """
    screen = pygame.display.set_mode((screen_size[0], screen_size[1]))
    pygame.display.set_caption(game.caption)
    Update = update
    LateUpdate = late_update
    Awake = awake
    if awake is not None:
        Awake()
    while True:
        screen.fill(game.background_colour)
        if update:
            Update()
        pygame.display.flip()
        fpsClock.tick(game.fps)
        if late_update:
            LateUpdate()

