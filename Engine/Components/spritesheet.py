import pygame
from Engine.Components.image import IMAGE
class SPRITESHEET(IMAGE):
    def __init__(self, filename):
        "Give a filename to select a spritesheet"
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error:
            print ('Unable to load spritesheet image:', filename)
            raise SystemExit


    # Load a specific image from a specific rectangle
    def image_at(self, rectangle, colorkey = None):
        "Loads image from x,y,x+offset,y+offset"
        image_object = IMAGE()
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        image_object.image = image
        return image_object


    # Load a whole bunch of images and return them as a list
    def images_at(self, rects, colorkey = None):
        "Loads multiple images, supply a list of coordinates" 
        images = []
        for rect in rects:
            images.append(self.image_at(rect,colorkey))
        return images


    def load_set(self,x,y,grid_size, colorkey = None):
        "Loads a set of given size and amount"
        rects = []
        for j in range(0,y):
            for i in range(0,x):
                rects.append((i*grid_size,j*grid_size,grid_size,grid_size))
        return self.images_at(rects,colorkey)

        