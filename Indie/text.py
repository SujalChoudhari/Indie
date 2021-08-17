from .transform import TRANSFORM
from .font import FONT
from . import app  as e
class TEXT(TRANSFORM):
    def __init__(self, text, font: FONT, colour):
        self.text = text
        self.font = font
        self.colour = colour
        self.font = self.font.font.render(
            self.text, True, self.colour, self.font.background)

    def blit(self):
        e.screen.blit(self.font, (self.position[0], self.position[1]))
        return super().blit()
