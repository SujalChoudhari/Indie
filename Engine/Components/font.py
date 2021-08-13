import pygame

class FONT:
    def __init__(self, path, size, background):
        self.path = path
        self.size = size
        self.background = background
        self.font = pygame.font.Font(self.path, self.size)



