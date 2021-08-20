import pygame
from pygame import image
from .transform import TRANSFORM
from . import app  as e
class IMAGE(TRANSFORM):
    """
    Add images on the screen\n
    """
    path = "./images/logo.png"
    image = pygame.image.load(path)

        
    def blit(self):
        """
        Draw the images on the screen\n
        """
        e.screen.blit(self.image, (self.position[0], self.position[1]))

        return super().blit()

    def scale(self, x:int, y:int):
        """
        Scales up the image as per parameters\n

        Parameters:\n
        :x(int): scale amount on x axis\n
        :y(int): scale amount on y axis\n
        """
        self.size[0] = x
        self.size[1] = y
        self.image = pygame.transform.scale(
            self.image, (self.size[0], self.size[1]))
        return super().scale()

    def rotate(self, angle:int):
        """
        Rotate the image as per parameters\n

        Parameters:\n
        :angle(int): Angle in degrees(0-360)\n
        """
        self.rotation = angle
        self.image = pygame.transform.rotate(self.image, self.rotation)
        return super().rotate()
