from IndieEngine.physics import QUAD, VECTOR
from .colour import COLOUR
from .transform import TRANSFORM
from .font import FONT
from . import app  as e
import pygame
class TEXT(TRANSFORM):
    """
    Create Ready to use texts\n
    """
    rect = None
    def __init__(self,rect:QUAD, text:str, font: FONT, colour:COLOUR,background_colour:COLOUR=None):
        """
        Create Ready to use texts\n
        \n
        Parameters:\n
        :rect(Quad): The position and suggested dimentions.
        :text(str): The text you want to show\n
        :font(FONT): The font the text  should have\n
        :colour(COLOUR): The colour of the text\n
        """
        self.rect = rect
        self.position = rect.position
        self.text = text
        self.font = font
        self.colour = colour
        self.background_colour = background_colour
        self.font = self.font.font.render(
            self.text, True, self.colour, self.background_colour)
            


    def blit(self):
        """
        Draw the text on to the screen\n
        """
        super().blit()
        width = self.font.get_width()
        height = self.font.get_height()
        self.size = VECTOR(width,height)
        self.rect = pygame.Rect(self.position.x,self.position.y,self.size.x,self.size.y)
        e.screen.blit(self.font, (self.rect.x, self.rect.y))
        
        

