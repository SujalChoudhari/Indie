# Imports
from IndieEngine.physics import VECTOR
from . import colour
import math
import pygame
import sys


global background_colour, caption, fps, screen_size, scalable, scale_amount, icon_file,window,screen

# Screen Constants
background_colour = colour.COLOUR.White
caption = "Indie Engine"
fps = 60
screen_size = VECTOR(900,600)
scale_amount = 1
icon_file = ""
scalable = False


window = None
screen = None
clock = pygame.time.Clock()
pygame.font.init()
 


def init(caption:str="Indie Engine",fps:int=30,screen_size:VECTOR = VECTOR(900,600),scale_amount:int=1,icon_file:str="",scalable:bool=False):
    """
    Initiate module/ window with given parameters(screen constants)
    """
    global window, screen
    
    pygame.init()
    caption = caption
    fps = fps
    screen_size = screen_size
    scale_amount = scale_amount
    icon_file = icon_file
    scalable = scalable



    window = pygame.display.set_mode((screen_size.x, screen_size.y),pygame.RESIZABLE)
    screen = pygame.Surface(
        (math.ceil(screen_size.x/scale_amount), math.ceil(screen_size.y/scale_amount)))


# Main RUN function
def run(update=None,draw=None, inputs=None) -> None:
    """
    Game loop
    """
    global window, screen, screen_size
    pygame.display.set_caption(caption)  # Set the title of the scene


    try:
        pygame.display.set_icon(pygame.image.load(icon_file))
    except:
        print("[MISSING] Ignoring the missing files, icon set to default")

    while 1:
        screen.fill(background_colour)
        
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE and scalable:
                window = pygame.display.set_mode((event.w,event.h),pygame.RESIZABLE)
                screen = pygame.transform.scale(screen, (event.w, event.h))
                screen_size = [event.w,event.h]
            if inputs:
                inputs(event,mouse)

        if update:
            update()

        if draw:
            draw()


        window.blit(pygame.transform.scale
        (screen, 
        (screen_size.x * scale_amount, 
        screen_size.y  * scale_amount)), (0, 0))
        #Strech the screen over the window for a pixelated look

        #fix the framerate and update the screen
        pygame.display.update()
        clock.tick(fps)