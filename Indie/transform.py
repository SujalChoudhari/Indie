from .gameobject import GAMEOBJECT

class TRANSFORM(GAMEOBJECT):
    """
    TRANSFORM\n
    This holds the physical location of a gameObject\n
    position: [x,y]\n
    size: [x,y]\n
    rotation:[n:degrees]\n
    """
    position = [10, 10]
    size = [100, 100]
    rotation = 0

    def blit(self):
        return super().blit()

    def rotate(self):
        pass

    def scale(self):
        pass