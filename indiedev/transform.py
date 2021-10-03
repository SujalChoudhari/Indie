from .gameobject import GAMEOBJECT
from .app import *
from indiedev import app

class TRANSFORM(GAMEOBJECT):
    """
    TRANSFORM\n
    This holds the physical location of a gameObject\n
    position: [x,y]\n
    size: [x,y]\n
    rotation:[n:degrees]\n
    """

    def __init__(self, position=[0, 0], size=[10, 10], rotation=0) -> None:
        self.position = position
        self.size = size
        self.rotation = rotation
        super().__init__()

    def blit(self):
        return super().blit()

    def rotate(self):
        pass

    def scale(self):
        pass

    def align(self,position:str="x",type:str = "center"):
        """
        Align a transform object\n
        :position:(str) This can be a "x" or a "y", the axis of which the align is to be used.\n
        :type:(str) this have values of "center", "start", "end". \n
                x, start means left,\n
                y, start means top,\n
                y,end means bottom,\n
                x,end means right\n
        """
        if position == "x":
            i = 0
        elif position =="y":
            i = 1
        else:
            print("[WRONG ARGUMENT] position argument is wrong")
            
        try:
            if type== "center":
                self.position[i] = (screen_size[i]/2) - (self.size[i]/2)
            elif type== "start":
                self.position[i] = 0
            elif type =="end":
                self.position[i] = screen_size[i] - self.size[i]

        except Exception as e:
            print(e)
            pass




