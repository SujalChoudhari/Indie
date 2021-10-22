from . import physics
import pygame
from .image import IMAGE


class CHARACTER_CONTROLLER(IMAGE):
    """
    Object movement\n
    """
    relative_movement = physics.VECTOR(0,0)
    moving_left = False
    moving_right = False
    moving_up = False
    moving_down = False
    speed = 10

    up_key = pygame.K_w
    down_key = pygame.K_s
    left_key = pygame.K_a
    right_key = pygame.K_d

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
