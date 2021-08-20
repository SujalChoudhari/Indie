from .gameobject import GAMEOBJECT


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
