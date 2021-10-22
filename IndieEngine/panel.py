import pygame
from .transform import TRANSFORM
from .physics import QUAD
from . import app as e


class PANEL(TRANSFORM):
    """
    A UI panel/rectangle
    """
    def __init__(self, rect:QUAD, rotation, thick, colour) -> None:
        super().__init__(rect=rect, rotation=rotation)
        self.thick = thick
        self.colour = colour
        self.size = rect.size
        self.position = rect.position
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        


    def blit(self):
        """
        Draw the rectangle on the screen
        """
        self.rect = pygame.Rect(
            self.position.x,
            self.position.y,
            self.size.x,
            self.size.y)

        pygame.draw.rect(e.screen, self.colour, self.rect, self.thick)
        return super().blit()

    def collidepoint(self,points:tuple=()) -> bool:
        return self.rect.collidepoint(points[0],points[1])
        
 
