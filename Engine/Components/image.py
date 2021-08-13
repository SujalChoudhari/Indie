import pygame
from Engine.Components.transform import TRANSFORM
import Engine.Game.defaults as e

class IMAGE(TRANSFORM):
    image = pygame.image.load("Assets/images/pygame_logo.png")
    def blit(self):
        e.screen.blit(self.image, (self.position[0], self.position[1]))

        return super().blit()

    def scale(self, x, y):
        self.size[0] = x
        self.size[1] = y
        self.image = pygame.transform.scale(
            self.image, (self.size[0], self.size[1]))
        return super().scale()

    def rotate(self, angle):
        self.rotation = angle
        self.image = pygame.transform.rotate(self.image, self.rotation)
        return super().rotate()
