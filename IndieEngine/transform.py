from IndieEngine.physics import QUAD, VECTOR
from .gameobject import GAMEOBJECT

from .app import *


class TRANSFORM(GAMEOBJECT):

    def __init__(self, rect:QUAD, rotation=0) -> None:
        """
        Transform class allows access to position, size and rotation of the object
        """
        self.x = rect.x
        self.y = rect.y
        self.width = rect.width
        self.height = rect.height

        self.position = rect.position
        self.size = rect.size

        self.rotation = rotation
        super().__init__()

    def blit(self):
        return super().blit()

    def align(self,parent:QUAD, anchor="mid-center") -> VECTOR:
        if anchor == "top-left":
            return parent.position
        elif anchor == "top-center":
            return VECTOR(parent.width/2-self.width/2,parent.y)
        elif anchor == "top-right":
            return VECTOR(parent.width-self.width,parent.y)
        elif anchor == "mid-left":
            return VECTOR(parent.x,parent.height/2-self.height/2)
        elif anchor == "mid-center":
            return VECTOR(parent.width/2 - self.width/2, parent.height/2 - self.height/2)
        elif anchor == "mid-right":
            return VECTOR(parent.width - self.width,parent.height/2 - self.height/2)
        elif anchor == "bottom-left":
            return VECTOR(parent.x,parent.height-self.height)
        elif anchor == "bottom-center":
            return VECTOR(parent.width/2-self.width/2,parent.height-self.height)
        elif anchor == "bottom-right":
            return VECTOR(parent.width-self.width,parent.width-self.width)
        else:
            return self.position

    def stretch(self,mode="fill",parent:QUAD=screen_size) -> QUAD:
        if mode == "fill":
            return QUAD(parent.x,parent.y,parent.width,parent.height)
        elif mode == "horizontal":
            return QUAD(parent.x,self.y,parent.width,self.height)
        elif mode == "vertical":
            return QUAD(self.x,parent.y,self.width,parent.height)




      