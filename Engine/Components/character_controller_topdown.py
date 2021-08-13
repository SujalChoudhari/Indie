import pygame
from Engine.Components.image import IMAGE

class CHARACTER_CONTROLLER_TOPDOWN(IMAGE):
    horizontal = 0
    vertical = 0
    speed = 10

    def move(self,axis:str = "None", value:bool= False):
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
        self.position = [self.position[0] + (self.horizontal)*self.speed,self.position[1] + (self.vertical)*self.speed]
        return super().blit()

    def controlls(self,event):
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
        