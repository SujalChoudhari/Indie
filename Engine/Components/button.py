import pygame
from Engine.Components.text import TEXT
from Engine.Components.panel import PANEL
import Engine.Game.defaults as e

class BUTTON(TEXT, PANEL):



    padding = 0.2
    ispressed = False

    def blit(self, color):
        width = self.font.get_width()
        height = self.font.get_height()
        b_rect = (self.position[0]-self.padding*width/2, self.position[1]-self.padding*height/2,
                  width+self.padding*width, height+self.padding*height)
        pygame.draw.rect(e.screen, self.colour, b_rect, self.thick)
        self.colour = color
        e.screen.blit(self.font, self.position)
        self.rect = pygame.Rect((b_rect))


    def controlls(self,event,mouse):
        self.ispressed = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint((mouse)):
                self.ispressed = True
