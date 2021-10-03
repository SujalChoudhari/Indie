# Imports
from . import colour
import math
import pygame
import sys



# Screen Constants
background_colour = colour.COLOUR.White
caption = "indiedev"

fps = 30
screen_size = [900, 600]
scale_amount = 1
icon_file = ""

window = None
screen = None
def init():
    """
    Initiate the indiedev Module
    """
    global window,screen
    
    pygame.init()

    window = pygame.display.set_mode((screen_size[0], screen_size[1]))

    screen = pygame.Surface(
        (math.ceil(screen_size[0]/scale_amount), math.ceil(screen_size[1]/scale_amount)))


# Main RUN function
def run(awake=None, update=None, inputs=None) -> None:
    """
    Create a new screen. \n
    `Parameters:` \n
    :awake(function name): this is called once before a screen loop starts \n
    :update (function name): this takes a function and calls after refreshing the screen\n
    :input(function name) : this is called before the update\n
    \n
    """
    try:
        pygame.display.set_icon(pygame.image.load(icon_file))
    except:
        print("[MISSING] Ignoring the missing files, icon set to default")

    pygame.display.set_caption(caption)  # Set the title of the scene
    if awake:
        awake()

    while 1:
        screen.fill(background_colour)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if inputs:
                inputs(event,mouse)

        if update:
            update()

        window.blit(pygame.transform.scale(screen, (screen.get_width(
        )*scale_amount, screen.get_height() * scale_amount)), (0, 0))
        #Strech the screen over the window for a pixelated look

        #fix the framerate and update the screen
        pygame.display.update()
        pygame.time.Clock().tick(fps)
