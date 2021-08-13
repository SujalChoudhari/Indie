from Engine.Components import BUTTON, FONT, IMAGE, PANEL, TEXT
import Engine.Game.main
import pygame
import sys
import math
import easygui


pygame.init()
Engine.Setup.screen_size = [900, 600]

#setup
spritesheet = IMAGE()
spritesheet.position = [0, 0]
w, h = 0, 0

grid = 16

#set multiplier
multiplier = [1, 1]
font = FONT("Assets/fonts/pacifico/Pacifico.ttf", 17, None)

#highlight box
rect = PANEL()
rect_free = PANEL()
rect_free.size = [0,0]

#buttons
open_spritesheet = BUTTON("Open New Spritesheet", font, (0, 0, 0))
open_spritesheet.position = [700, 560]


def closestmultiplier(initial, round):
    return math.ceil(initial/round) * round

    # if x > n:
    #     return x
    # z = (int)(x / 2)
    # n = n + z
    # n = n - (n % x)
    # return n


def Update():
    global multiplier
    spritesheet.blit()

    #co-ordinates
    mouse_pos = pygame.mouse.get_pos()
    rect_pos_text_end = TEXT(
        f"{math.ceil((rect.position[0] + rect.size[0] )/multiplier[0])},{math.ceil((rect.position[1]+ rect.size[1])/multiplier[1])}", font, (0, 0, 0))
    rect_pos_text_end.position = (mouse_pos[0] + 10, mouse_pos[1]+50)

    #highlighted box
    rect.position = [closestmultiplier(mouse_pos[0], grid * multiplier[0]) - grid * multiplier[0],
                     closestmultiplier(mouse_pos[1], grid * multiplier[1]) - grid * multiplier[0]]
    rect_pos_text = TEXT(
        f"{math.ceil(rect.position[0]/multiplier[0])},{math.ceil(rect.position[1]/multiplier[1])}", font, (0, 0, 0))
    rect_pos_text.position = (mouse_pos[0] + 10, mouse_pos[1]+20)
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            rect_free.position = [mouse_pos[0], mouse_pos[1]]
            rect_free.size = [0, 0]
        open_spritesheet.controlls(event, mouse_pos)
    #open_spritesheet button check
    if open_spritesheet.ispressed:
        file = easygui.fileopenbox()

        spritesheet.image = pygame.image.load(file).convert()
        spritesheet.image.set_colorkey((255, 255, 255))
        w, h = spritesheet.image.get_height(), spritesheet.image.get_height()
        spritesheet.image = pygame.transform.scale(
            spritesheet.image, (500, 500))

        multiplier = spritesheet.image.get_height()/w, spritesheet.image.get_height()/h
        rect.size = [grid * multiplier[0], grid * multiplier[1]]

    #draw


    rect.blit()
       

    rect_pos_text.blit()
    rect_pos_text_end.blit()
    rect_free.blit()
    open_spritesheet.blit((0, 0, 0))


Engine.Game.run.Screen(update=Update)
