from Indie.colour import COLOUR
import pygame
from .image import IMAGE


class SPRITESHEET(IMAGE):
    """
    Use spritesheets to better performance.\n
    """

    def __init__(self, filename):
        """
        Parameters:\n
        :filename(str): Give a filename to select a spritesheet\n
        """
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error:
            print('Unable to load spritesheet image:', filename)
            raise SystemExit

    # Load a specific image from a specific rectangle
    def image_at(self, rectangle, colorkey: COLOUR = None) -> IMAGE:
        """
        Load image from the sheet\n
        Parameters:\n
        :rectangle(x,y,x+offset,y+offset): the dimentions of the image\n
        :colorkey(COLOUR):colourkey for that specific image\n
        \n
        Returns:\n
        An individual image\n
        """
        image_object = IMAGE()
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        image_object.image = image
        return image_object

    # Load a whole bunch of images and return them as a list
    def images_at(self, rects, colorkey: COLOUR = None):
        """
        Loads multiple images, supply a list of coordinates\n
        \n
        Parameters:\n
        :rects([rect1,rect2,...,rectN]): list of rects as per (x,y,x+offset,y+offset)\n
        :colorkey(COLOUR)\n
        \n
        Returns:\n
        List of images(IMAGE object)\n
        """
        images = []
        for rect in rects:
            images.append(self.image_at(rect, colorkey))
        return images

    def load_set(self, x: int, y: int, grid_size: int, colorkey: COLOUR = None):
        """
        Loads a set of given size and amount\n
        \n
        Parameters:\n
        :x(int): the starting position of the cropping grid(x)\n
        :y(int): the starting position of the cropping grid(y)\n
        :grid_size(int): size of an individual tile\n
        \n
        Returns:\n
        List of images(IMAGE object)\n
        """
        rects = []
        for j in range(0, y):
            for i in range(0, x):
                rects.append((i*grid_size, j*grid_size, grid_size, grid_size))
        return self.images_at(rects, colorkey)
