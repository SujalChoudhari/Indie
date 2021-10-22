import pygame

from IndieEngine.physics import QUAD
from .transform import TRANSFORM
from . import app  as e
class IMAGE(TRANSFORM):
    """
    Add images on the screen\n
    """
    def __init__(self,rect:QUAD,rotation,path=None) -> None:
        self.path = path
        super().__init__(rect,rotation)
        try:
            self.image = pygame.image.load(self.path).convert_alpha()
            self.scale(rect.width,rect.height)
            self.rotate(rotation)
        except:
            print("[MISSING]: missing the file path")

        self.size = rect.size

    def blit(self):
        """
        Draw the images on the screen\n
        """
        if self.position.x >= -self.size.x and self.position.y >= -self.size.y:
            if self.position.x <= e.screen_size.x and self.position.y <= e.screen_size.y:
                e.screen.blit(self.image, (self.position.x, self.position.y))

        return super().blit()

    def scale(self, x:int, y:int):
        """
        Scales up the image as per parameters\n

        Parameters:\n
        :x(int): scale amount on x axis\n
        :y(int): scale amount on y axis\n
        """
        self.size.x = x
        self.size.y = y
        self.image = pygame.transform.scale(self.image,(self.size.x,self.size.y))
       

    def rotate(self, angle:int):
        """
        Rotate the image as per parameters\n

        Parameters:\n
        :angle(int): Angle in degrees(0-360)\n
        """
        self.rotation = angle
        self.image = pygame.transform.rotate(self.image, self.rotation)
