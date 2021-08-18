import pygame
from .image import IMAGE

class CHARACTER_CONTROLLER(IMAGE):
    """
    8 directional player movement\n
    """
    horizontal = 0
    vertical = 0
    speed = 10

    def move(self,axis:str = "None", value:bool= False)->None:
        """
        Used by control() to move the player\n

        Parameters:\n
        :axis(str):\n
        :value(bool):\n
        """
        if "left" in axis and value:
            self.horizontal = -1
        elif "right" in axis and value:
            self.horizontal = 1

        elif "up" in axis and value:
            self.vertical = -1

        elif "down" in axis and value:
            self.vertical = 1



        if "left" in axis and not value:
            self.horizontal = 0
        elif "right" in axis and  not value:
            self.horizontal = 0

        elif "up" in axis and not value:
            self.vertical = 0

        elif "down" in axis and not value:
            self.vertical = 0

    def blit(self):
        """
        Draw the player on the screen\n
        """
        self.position = [self.position[0] + (self.horizontal)*self.speed,self.position[1] + (self.vertical)*self.speed]
        return super().blit()

    def control(self,event)-> None:
        """
        Control the player with thr help of ASDW key pressed\n
        
        Parameters:\n
        :event(pygame.event.get()): Event to handle\n
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.move("left", True)
            if event.key == pygame.K_d:
                self.move("right", True)
            if event.key == pygame.K_w:
                self.move("up", True)
            if event.key == pygame.K_s:
                self.move("down", True)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.move("left", False)
            if event.key == pygame.K_d:
                self.move("right", False)
            if event.key == pygame.K_w:
                self.move("up", False)
            if event.key == pygame.K_s:
                self.move("down", False)
        