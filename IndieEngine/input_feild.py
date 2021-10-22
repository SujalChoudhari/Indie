from IndieEngine.inputs import EVENT, KEY
from IndieEngine.physics import QUAD, VECTOR
from .transform import TRANSFORM
from .colour import COLOUR
from .font import font_16
from . import app  as e
import pygame
pygame.init()


class INPUTFEILD(TRANSFORM):
    """
    Customisable Input feilds
    """
    save_status = False
    COLOR_INACTIVE = COLOUR().make(0,0,0)
    COLOR_ACTIVE =COLOUR().make(20,80,80)

    def __init__(self,rect:QUAD, text='',colour_inactive=COLOUR().make(0,0,0),colour_active=COLOUR().make(20,80,80)):
        self.position = rect.position
        self.size = rect.size
        self.rect = pygame.Rect(rect.x,rect.y,rect.w,rect.h)
        self.color = colour_inactive
        self.COLOR_INACTIVE = colour_inactive
        self.COLOR_ACTIVE = colour_active
        self.text = text
        self.active = False
        self.save_status = True
        self.save()
        self.txt_surface = font_16.render(self.text, True, COLOUR().make(150,150,150))

    def controls(self, event):
        if event.type == EVENT.mouse_button_down:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                if self.true_value:
                    self.text = self.true_value
                self.update()
                # Toggle the active variable.
                self.active = not self.active
            else:
                if self.active:
                    self.active = False
                    if not "..." in self.text:
                        self.save()
                    
            # Change the current color of the input box.
            if self.active:
                self.color = self.COLOR_ACTIVE
            else:
                self.color = self.COLOR_INACTIVE
            # Re-render the text.
            self.txt_surface = font_16.render(self.text, True, COLOUR().make(150,150,150))
            

        if event.type == EVENT.key_down:
            if self.active:
                self.update()
                if event.key == KEY.return_:
                    self.save_status = True
                    self.save()
                    self.active = False
                elif event.key == KEY.backspace:
                    self.text = self.text[:-1]
                else:
                    self.save_status = False
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = font_16.render(self.text, True, COLOUR().make(150,150,150))



    def update(self):
        # Resize the box if the text is too long.
        width = max(50, self.txt_surface.get_width()+ 20)
        self.rect.width = width

    def blit(self):
        # Blit the rect.
        pygame.draw.rect(e.screen, self.color, self.rect, 0)
        # Blit the text.
        self.rect = pygame.Rect(self.position.x,self.position.y,self.size.x,self.size.y)
        e.screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+10))
        
    true_value = None
    def save(self):
        self.true_value = self.text
        self.text = f"{self.text[:int(self.size.x/10)]}..."
        

