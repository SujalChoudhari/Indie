from Engine.Components.colour import COLOUR
import pygame

class FONT:
    """
    FONT
    create a pygame font asset to use if for text
    """
    def __init__(self, path, size, background:COLOUR):
        """
        Parameters:
        path : String path to the .ttf file(or other pygame supported formats)
        size : the size of the font
        bakground: background colour
        """
        self.path = path
        self.size = size
        self.background = background
        self.font = pygame.font.Font(self.path, self.size)



