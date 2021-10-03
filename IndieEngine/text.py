from .colour import COLOUR
from .transform import TRANSFORM
from .font import FONT
from . import app  as e
class TEXT(TRANSFORM):
    """
    Create Ready to use texts\n
    """
    def __init__(self, text:str, font: FONT, colour:COLOUR,background_colour:COLOUR):
        """
        Create Ready to use texts\n
        \n
        Parameters:\n
        :text(str): The text you want to show\n
        :font(FONT): The font the text  should have\n
        :colour(COLOUR): The colour of the text\n
        """
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
        e.screen.blit(self.font, (self.position[0], self.position[1]))
        width = self.font.get_width()
        height = self.font.get_height()
        self.size = [width,height]
        return super().blit()

