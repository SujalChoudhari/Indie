from .colour import COLOUR
import pygame
from .transform import TRANSFORM
from . import app as e


class PANEL(TRANSFORM):
    """
    A UI panel/rectangle
    """
    def __init__(self, position, size, rotation,thick, colour) -> None:
        self.thick = thick
        self.colour = colour
        self.size = size
        super().__init__(position=position, size=size, rotation=rotation)


    def blit(self):
        """
        Draw the rectangle on the screen
        """
        rect = pygame.Rect(
            self.position[0], self.position[1], self.size[0], self.size[1])
        pygame.draw.rect(e.screen, self.colour, rect, self.thick)
        return super().blit()
