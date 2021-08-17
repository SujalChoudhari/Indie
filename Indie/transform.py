from .gameobject import GAMEOBJECT

class TRANSFORM(GAMEOBJECT):
    """
    TRANSFORM
    This holds the physical location of a gameObject
    `position: [x,y]`
    `size: [x,y]`
    `rotation:[n:degrees]`
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