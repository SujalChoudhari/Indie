# Imports
from . import colour
import math
import pygame
pygame.init()


# Screen Constants
background_colour = colour.COLOUR.Gray
caption = "Indie"
fps = 30
screen_size = [900, 600]
scale_amount = 1
fps_clock = pygame.time.Clock()

# Window is the display on which :screen: is blited on
# It is used for zooming the screen, i.e. to make pixels bigger(for a pixel art game)
# Recomended to blit text on window for crisp look (not by default)
window = pygame.display.set_mode((screen_size[0], screen_size[1]))

# All the images,geometry is drawn on the screen and 
# then screen is streched to fit the widow according to scale_amount 
screen = pygame.Surface(
    (math.ceil(screen_size[0]/scale_amount), math.ceil(screen_size[1]/scale_amount)))


# Main RUN function
def run(awake=None, update=None, late_update=None) -> None:
    """
    Create a new screen. \n
    Parameters: \n
    :awake(function name): this is called once before a screen loop starts \n
    :update (function name): this takes a function and calls after refreshing the screen\n
    :late_update(function name) : this is called after the update method is called\n
    """
    pygame.display.set_caption(caption)

    if awake:
        awake()

    while 1:
        window.fill(background_colour)
        if update:
            update()

        window.blit(pygame.transform.scale(screen, (screen.get_width(
        )*scale_amount, screen.get_height() * scale_amount)), (0, 0))

        pygame.display.update()
        fps_clock.tick(fps)

        if late_update:
            late_update()
