
import pygame

from IndieEngine import inputs
from . import app as e
from .colour import COLOUR
from .font import *
from .inputs import EVENT
from .button import BUTTON
from .text import TEXT
from .input_feild import INPUTFEILD
from .panel import PANEL
from IndieEngine import app


class WINDOW(PANEL):
    dragged = False
    is_active = True;
    is_minimised = False
    def __init__(self, position, size, rotation, thick,name,button_colour=COLOUR.White) -> None:
        super().__init__(position, size, rotation, thick, COLOUR().make(22,22,22))
        self.name = name
        self.name = TEXT(name,FONT("Resources/font_big.ttf",20),COLOUR.White,None)
        self.name.blit()
        
        self.hide = BUTTON("x",FONT("Resources/font_small.ttf",16),button_colour,None)
        self.hide.thick = -1

        self.minimise = BUTTON("v",FONT("Resources/font_small.ttf",16),button_colour,None)
        self.minimise.thick = -1
        self.minimise.blit()

    rect =None
    def blit(self): 
        if not self.is_active:
            return

        if self.is_minimised:
            self.size[1] = self.name.rect.width

        self.name.position[0] = self.position[0] + (self.size[0]/2) - self.name.size[0]/2
        self.name.position[1] = self.position[1] + self.name.size[1]/3
        self.name.blit()

        self.hide.position[0] = self.position[0] + (self.size[0]) - 10 - self.hide.size[0]/2
        self.hide.position[1] = self.position[1] + self.hide.size[1]
        self.hide.blit()

        self.minimise.position[0] = self.position[0] + (self.size[0] - 10 -self.minimise.rect.width) - self.minimise.size[0]/2
        self.minimise.position[1] = self.position[1] + self.minimise.size[1]
        self.minimise.blit()
        
        return super().blit()


    mouse_offset = [0,0]
    streched = False
    def controls(self,event,mouse):
        self.hide.control(event,mouse)
        self.minimise.control(event,mouse)
        # close the window 
        if self.hide.ispressed:
            self.is_active = not self.is_active

        if not self.is_active:
            return
        
        if self.minimise.ispressed:
            self.is_minimised = not self.is_minimised
            if not self.is_minimised:
                self.size[1] = 35+(40 * len(self.input_list))


        if event.type == EVENT.mouse_button_down:
            if mouse[0] > self.position[0] +self.size[0] - 10 and mouse[0] < self.position[0] +self.size[0] + 10:
                if mouse[1] > self.position[1] +self.size[1] - 10 and mouse[1] < self.position[1] +self.size[1] + 10:
                    pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_SIZENWSE)
                    self.streched = True
                    

        if event.type == EVENT.mouse_button_down and self.name.rect.collidepoint(mouse):
            self.mouse_offset = [mouse[0] - self.position[0],mouse[1]-self.position[1]]
            self.dragged = True
            

        if event.type == EVENT.mouse_button_up :
            self.dragged = False
            self.streched = False
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)
        
        if self.dragged:
            self.position = [mouse[0]-self.mouse_offset[0],mouse[1]-self.mouse_offset[1]] 

        if self.streched:
            width  = max(200,mouse[0] - self.position[0])
            height = max(35+(40 * len(self.input_list)),mouse[1] - self.position[1])
            self.size = [width,height]
           


class INSPECTOR(WINDOW):
    def __init__(self, position, size, rotation, thick, name) -> None:
        super().__init__(position, size, rotation, thick, name)

    input_list:INPUTFEILD = []
    name_list:TEXT = []
    def listen(self,*variables:list,text_colour=COLOUR().make(35,105,105)):
        i = 1
        for variable in variables:
            if type(variable[0]) is str or type(variable[0]) is int:
                self.input_list.append(INPUTFEILD(self.position[0] + self.size[1] * 0.1, (self.position[1]+ 30 * i+10) ,100,20,str(variable[0])))


                text = TEXT(variable[1],FONT("Resources/font_small.ttf",9),text_colour)
                text.position = [self.position[0] + self.size[1] * 0.1, (self.position[1]+ 30 * i+5)]
                self.name_list.append(text)

            if type(variable[0]) is list:
                self.input_list.append(INPUTFEILD(self.position[0] + self.size[1] * 0.1, (self.position[1]+ 30 * i+10) ,100,20,str(variable[0][0])))

                text = TEXT(f"{variable[1]}.x",FONT("Resources/font_small.ttf",9),text_colour)
                text.position = [self.position[0] + self.size[1] * 0.1, (self.position[1]+ 30 * i+5)]
                self.name_list.append(text)

                self.input_list.append(INPUTFEILD(self.position[0] + self.size[1] * 0.1, (self.position[1]+ 30 * i+10) ,100,20,str(variable[0][1])))

                text = TEXT(f"{variable[1]}.y",FONT("Resources/font_small.ttf",9),text_colour)
                text.position = [self.position[0] + self.size[1] * 0.1, (self.position[1]+ 30 * i+5)]
                self.name_list.append(text)
            i +=1
        pass
    def blit(self):
        if  self.is_active and not self.is_minimised:
            
            self.rect = pygame.Rect(self.position[0],self.position[1],self.size[0],self.size[1])
            pygame.draw.rect(e.screen, self.colour, self.rect, 0)
            i = 1
            for inputs in self.input_list:
                inputs.size [0] = 0.9 * self.size[0]
                inputs.position = [self.position[0] + (self.size[0]/2) - inputs.size[0]/2, self.position[1]+ 30 * i+10 +i*5]
                inputs.blit()
                i += 1

            j = 1
            for name in self.name_list:
                name.position = [self.position[0] + (self.size[0]/2) - name.size[0]/2, self.position[1]+ 30 * j+10 + j*5]
                name.blit()
                j+=1
        return super().blit()

    def controls(self, event, mouse):
        super().controls(event, mouse)
        value_array =[]
        for inputs in self.input_list:
            value_array.append(inputs.true_value)
            inputs.controls(event)
        return value_array
        
    
class NAVBAR(PANEL):
    def __init__(self, position, size, rotation, thick, colour) -> None:
        super().__init__(position, size, rotation, thick, colour)
    buttons = []

    def add_button(self,buttons:list[BUTTON]):
        self.buttons.extend(buttons)
        for button in self.buttons:
            button.blit()

    def blit(self):
        i = 0
        self.size = [app.screen_size[0],20]
        super().blit()
        for button in self.buttons:
            button.position = [i * self.buttons[i-1].rect.width +10 ,5]
            button.blit()
            i +=1

    def controls(self,event,mouse):
        for button in self.buttons:
            button.control(event,mouse)

    
class DROPDOWN(PANEL):
    def __init__(self, position, size, rotation, thick, colour) -> None:
        self.rect = pygame.Rect(self.position[0],self.position[1],self.size[0],self.size[1])
        super().__init__(position, size, rotation, thick, colour)
    buttons = []
    isfocused = False
    def add_button(self,buttons:list[BUTTON]):
        self.buttons.extend(buttons)
        for button in self.buttons:
            button.blit()

    def blit(self):
        if self.isfocused:
            i = 0
            # self.size = [app.screen_size[0],20]
            self.rect = pygame.Rect(self.position[0],self.position[1],self.size[0],self.size[1])
            pygame.draw.rect(e.screen, self.colour, self.rect, 0)
            super().blit()
            for button in self.buttons:
                button.position = [self.position[0] + 10 ,self.position[1] + i * self.buttons[i-1].rect.height +10]
                button.blit()
                i +=1

    def controls(self,event,mouse):
        if self.rect.collidepoint((mouse)) and event.type == inputs.EVENT.mouse_button_down:
            self.isfocused = True
            for button in self.buttons:
                button.control(event,mouse)
        else:
            self.isfocused = False
            for button in self.buttons:
                button.ispressed = False


        
