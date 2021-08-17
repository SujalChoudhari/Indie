from .colour import COLOUR
import pygame
from .transform import TRANSFORM
from . import app  as e

class PANEL(TRANSFORM):
    thick = 1
    colour = COLOUR.Gray
    rect = pygame.Rect(0, 0, 100, 100)

    def blit(self):
        rect = pygame.Rect(
            self.position[0], self.position[1], self.size[0], self.size[1])
        pygame.draw.rect(e.screen, self.colour, rect, self.thick)
        return super().blit()