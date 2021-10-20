# Imports
from . import colour
import math
import pygame
import sys, threading


# Screen Constants
background_colour = colour.COLOUR.White
caption = "indiedev"

fps = 60
screen_size = [900, 600]
scale_amount = 1
icon_file = ""
scalable = False
window = None
screen = None
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.Font("Resources/font_small.ttf",18)
 
 
def update_fps():
	fps = str(int(clock.get_fps()))
	fps_text = font.render(fps, 1, pygame.Color("coral"))
	return fps_text

def init():
    """
    Initiate the indiedev Module
    """
    global window,screen
    
    pygame.init()

    window = pygame.display.set_mode((screen_size[0], screen_size[1]),pygame.RESIZABLE)

    screen = pygame.Surface(
        (math.ceil(screen_size[0]/scale_amount), math.ceil(screen_size[1]/scale_amount)))


# Main RUN function
def run(awake=None, update=None,draw=None, inputs=None) -> None:
    global window, screen, screen_size
    """
    Create a new screen. \n
    `Parameters:` \n
    :awake(function name): this is called once before a screen loop starts \n
    :update (function name): this takes a function and calls after refreshing the screen\n
    :input(function name) : this is called before the update\n
    \n
    """
    pygame.display.set_caption(caption)  # Set the title of the scene
    awake_thread = threading.Thread(target=awake)

    try:
        pygame.display.set_icon(pygame.image.load(icon_file))
    except:
        print("[MISSING] Ignoring the missing files, icon set to default")

    if awake:
        awake_thread.start()

    awake_thread.join()

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

        screen.blit(update_fps(), (screen_size[0]-30,0))
        window.blit(pygame.transform.scale(screen, (screen.get_width(
        )*scale_amount, screen.get_height() * scale_amount)), (0, 0))
        #Strech the screen over the window for a pixelated look

        #fix the framerate and update the screen
        pygame.display.update()
        clock.tick(fps)