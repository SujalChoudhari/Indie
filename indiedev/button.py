from .colour import COLOUR
import pygame
from .text import TEXT
from .panel import PANEL
from . import app  as e

class BUTTON(TEXT, PANEL):
    """
    Create a interactable button a Surface\n
    """
    padding = 0.2
    ispressed = False

    def blit(self, color:COLOUR) -> None:
        """
        Draw the Button on the Screen\n
        Parameters:\n
        :color(COLOUR): the colour of the button(not text)\n
        """
        width = self.font.get_width()
        height = self.font.get_height()
        b_rect = (self.position[0]-self.padding*width/2, self.position[1]-self.padding*height/2,
                  width+self.padding*width, height+self.padding*height)
        pygame.draw.rect(e.screen, self.colour, b_rect, self.thick)
        self.colour = color
        e.screen.blit(self.font, self.position)
        self.rect = pygame.Rect((b_rect))


    def control(self,event,mouse)->None:
        """
        Handle Events of a Button\n
        Parameters:\n
        :event(event.pygame.get()): The event to handle\n
        :mouse(x,y): Position of mouse\n
        """
        self.ispressed = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint((mouse)):
                self.ispressed = True
