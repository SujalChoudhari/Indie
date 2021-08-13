from Engine.Components.gameobject import GAMEOBJECT

class TRANSFORM(GAMEOBJECT):
    position = [10, 10]
    size = [100, 100]
    rotation = 0

    def blit(self):
        return super().blit()

    def rotate(self):
        pass

    def scale(self):
        pass