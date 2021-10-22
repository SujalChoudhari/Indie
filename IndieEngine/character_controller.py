from IndieEngine.inputs import KEY
from . import physics
import pygame
from .image import IMAGE


class CHARACTER_CONTROLLER(IMAGE):
    """
    Object movement\n
    """
    def __init__(self, rect:physics.QUAD, rotation, path, speed:int=10, up_key=KEY.w, down_key=KEY.s, 
    left_key=KEY.a, right_key=KEY.d) -> None:
        self.speed = speed
        self.up_key = up_key
        self.down_key = down_key
        self.left_key = left_key
        self.right_key = right_key
        super().__init__(rect, rotation, path)

        


    relative_movement = physics.VECTOR(0,0)
    moving_left = False
    moving_right = False
    moving_up = False
    moving_down = False


    

    def blit(self):
        """
        Draw the object on the screen\n
        """
        return super().blit()

    def control(self, event) -> None:
        """
        Get events of the object\n
        
        Parameters:\n
        :event(pygame.event.get()): Event to handle\n
        """

        if event.type == pygame.KEYDOWN:
            if event.key == self.left_key:
                self.moving_left = True
                

            if event.key == self.right_key:
                self.moving_right = True

            if event.key == self.up_key:
                self.moving_up = True
                

            if event.key == self.down_key:
                self.moving_down = True
                

        if event.type == pygame.KEYUP:
            if event.key == self.left_key:
                self.moving_left = False

            if event.key == self.right_key:
                self.moving_right = False

            if event.key == self.up_key:
                self.moving_up = False

            if event.key == self.down_key:
                self.moving_down = False

        if self.moving_up:
            self.relative_movement.y = -self.speed
        if self.moving_down:
            self.relative_movement.y = self.speed
        if self.moving_left:
            self.relative_movement.x = -self.speed
        if self.moving_right:
            self.relative_movement.x = self.speed
            

    def move(self):
        """Move the object with the help of relative position"""

        updated_location, collisions = physics.move(pygame.Rect(
            self.position.x, self.position.y, self.size.x, self.size.y), self.relative_movement)

        self.position.x = updated_location.x
        self.position.y = updated_location.y
        self.relative_movement = physics.VECTOR(0,0)
