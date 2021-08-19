# INDIE 

pygame framework

## Introduction
---
Indie is a pygame framework made by [@NotSujal.](https://github.com/NotSujal)
It has pre-written classes required for developing games.



## Installation
---
```py
pip install Indie
```

(not yet uploaded to pypi)  
*Download from the [Github](https://github.com/NotSujal/Indie)

## How to use
---
Brief information of each submodules of Indie
### Setting up (app)
---

There are various constants to start setting up the window.

```py
background_colour = (0,0,0)
caption = "Indie"
icon_file = 'Assets/images/logo.png'
fps = 30
screen_size = [900, 600]
scale_amount = 1
```

To set each one of it, what you can do is
```py
import Indie

Indie.app.background_colour = (255,255,255)

Indie.app.caption = "My new Project"
#applicable for all the screen constants
```

### Screens
---
A Screen is just a infinite while loop, with multiple screens(loops) you can create multiple scenes, i.e. Start Screen, Game Screen, etc.

```py
Indie.app.run(awake=None, update=None, inputs=None)
# This Creates a screen

```
#### Parameters

`run()` takes 3 function names as parameters.

`awake` : awake is called only once before the while loop to load the necessary data.

`update` : update is called every frame, usefull for drawing GUI/Images on Screen.

`inputs` : inputs is called whenever an input is generated

#### Example
```py
#so your code may look like this

def Update():
    # logic/ physics/ drawing goes here
    pass

def Inputs(event,mouse): 
    #NOTE: the Input function needs a pygame.event parameter
    #and mouse position tuple (x,y)

    # close/quit event is already handled by the app.run
    # handle events here
    pass

def Awake():
    # load the data from the files, load the images, sounds, etc.
    pass

Indie.app.run(awake=Awake, update=Update, inputs=Inputs)
```


##  Classes
---
Premade classes helps to build the project in cleaner pattern

### GAMEOBJECT
---
Every object on the screen is a game object, from texts to images, all of them.
It has a basic function  `blit` which is overritten by other classes.

### TRANSFORM
----
Transform is responsible for the `position`, `scale` and the `rotation` of the object, and holds basics manipulations which are overitten by other classes.
```py
#properties of transform

position = [x,y]
scale = [x,y]
rotation = deg(int in degrees)
```

### FONT
---
Font helps in creating font assets for text.
Font takes `path`( location of only pygame supported font assets(.ttf,etc)) and `size`(in int)
```py
#creating font asset
huge_font = Indie.font.FONT(path = "Assets/fonts/germania_one/germania_regular_one.ttf", size = 128)
```

### COLOUR
---

An Easy way to make colours using RGB values, It has some built in colours

```py
# make a new colour
Indie.colour.COLOUR.make(255,0,0) # R=255, G=0, B=0
# this will return (255,0,0)
# it clamps values between 0 and 255, so,
# Indie.colour.COLOUR.make(300,400,500) will return (255,255,255)
```

Using Standared Colours
```py

Indie.app.background_colour = Indie.colour.COLOUR.White

# List of standared colours
Black	= (0,0,0)
White	= (255,255,255)
Red	    = (255,0,0)
Lime	= (0,255,0)
Blue	= (0,0,255)
Yellow	= (255,255,0)
Aqua	= (0,255,255)
Fuchsia	= (255,0,255)
Silver	= (192,192,192)
Gray	= (128,128,128)
Maroon	= (128,0,0)
Olive	= (128,128,0)
Green	= (0,128,0)
Purple	= (128,0,128)
Teal	= (0,128,128)
Navy	= (0,0,128)
```

### TEXT
---
Text uses the FONT class to make a nice looking text.
It has constants such as `text`,`colour`,`font`,`background_colour`
This overrites the blit from the GameObject class

```py
some_text = Indie.text.TEXT(text ="Hello, World!", font =huge_font, colour = Indie.colour.COLOUR.Black, background_colour= None)


def Update():
    # this will draw the text at position([x,y])
    some_text.position = [100,50]
    some_text.blit() 
```


### PANEL
---
Panel is a way to draw rectangles on the screen
It uses `thick` the thickness of rectangle, `colour` the colour of rectangle,


```py
square = Indie.panel.PANEL(1,Indie.colour.COLOUR.Grey)
```

### IMAGE
---

Image class allows us to draw images on the screen
It takes a extra `path`(str) of the image.
It also overrites the `scale` and `rotate` functions of Transform.

```py
image = Indie.image.Image(path = "img.png") # can also set position,size and rotation here.

def Update():
    image.blit()
    image.scale(10,10) # the position shows the topleft corner, while size shows the width and height
    image.rotate(90) #in degrees

```


### BUTTON
---
Button Component helps to create descent looking buttons.
it draws a box around a centered text.
It has a extra `padding` parameter which gives space between text and box.

```py
button1 = Indie.button.BUTTON(text="Press Me", font=huge_font, colour: (0,0,0), background_colour: (21,21,21))
# note the above parameters are for the text of buttons, customize the box in blit()

button1.padding = 0.5
def Update():
    button1.blit(color=COLOUR.Red) # this is the box colour
```

To interact with the button,
```py

def Inputs(event,mouse):
    
    button1.control(self,event,mouse)
```

### CHARATER_CONTROLLER
---
Character controller component is just an image component but movable with key inputs.
You can set the inputs by
```py
#initiate the controller
player = Indie.character_controller.CHARACTER_CONTROLLER()
#speed of controller
player.speed = 2
player.scale(16, 16) # player.size = [16,16] wont work cause the image is already loaded
player.position = [100, 100]

#change the inputs of controller (these are default values)
player.up_key = pygame.K_w
player.down_key = pygame.K_s
player.left_key = pygame.K_a
player.right_key = pygame.K_d

```
Then we can draw the player as normal
```py
player.blit()
```

For the movement you have `moving_left`,`moving_right`, `moving_up`, `moving_down` bools
Thus for a 8 directional movement
```py

def Inputs(event,mouse):
    player.control(event)

def Update():
    if player.moving_left:
        player.relative_movement[0] -= player.speed
    if player.moving_right:
        player.relative_movement[0] += player.speed


    if player.moving_up:
        player.relative_movement[1] -= player.speed
    if player.moving_down:
        player.relative_movement[1] += player.speed
    # note the relative_movement is the position relative to the current position which will be set on next frame

    #finally move the object to the new position
    player.move()
    # then drawing it
    plyer.blit()
```

### SPRITESHEETS
---
This allows you to use spritesheets for project for performance and maintainance reasons,
This sprite sheet component is taken from [here](https://www.pygame.org/wiki/Spritesheet) and modified.

```py

images = []
sprite_sheet = Indie.spritesheet.SPRITESHEET("Assets\images\spritesheet.png")
# this will populate the images[] with IMAGE objects.

# by using load_set
    #this allows you to choose a desired grid from the spritesheet.png
images = sprite_sheet.load_set(x=4, y=2, grid_size=16, colorkey=Indie.colour.COLOUR.White)

# you can use load_set, image_at, load_strip, images_at as per criteria
```

### SPRITESTRIP_ANIMATION
---
This allows use to use animations very efficiently, again tis spritestrip component is taken from [here](https://www.pygame.org/wiki/Spritesheet).
It uses the load_strip from Spritesheet class.

```py

player_walk_cycle = Indie.spritestrip_animation.SPRITESTRIP_ANIMATION(
    filename="player_animation.png", rect=(0,0,16,16), count=5, colorkey=None, loop=False, frames=10)
    # select the first image from the strip by rect parameter
    # count is used to specify how many images from that strip will be used

#start itirating the animation
player_walk_cycle.iter()

def Update():
    # set the player image to the image of next frame of the animation cycle.
    player.image = player_walk_cycle.next().image
```

### TILEMAP
---
Tilemap is the best way to design levels
These tilemaps can stack on top of each other and can be collided with.
This uses the physics.py library for that.

```py
level1 = Indie.tilemap.TILEMAP()
level1.map_location = "map.txt"
level1.tile_size = 16 # size of a tile f the tilemap
```

/map.txt (each character represents a tile)
```txt
11111
1  31
12  1
11111
```

setting up tiles{}
```py
level1.tiles = {
    # here images is the array returned by the spritesheet.load_set()
    "1": images[0], # the first image in the array has id=1
    "2": images[1], #id = 2
    "3": images[2], # ..
    "4": images[4], #..
    "5": images[7], # id=5
}

# setting up physics
Indie.physics.collidable_tile_rects = level1.tile_rects 
# tile_rects is a list of all the tiles in the tilemap.

def Awake():
    level1.loadmap(["3","1"]) # load the data from map.txt into game
    #Note: ["3","1"] specifies the tiles with ids which are acctually collidable

def Update():
    level1.blit()

Indie.app.run(awake=Awake,update=Update,inputs=Inputs)
```

### SOUND_MANAGER
---
Sound manager is a combination of classes, MUSIC and SOUND
This allows us to create sound libraries and play music

```py
# background music
background_music = Indie.sound_manager.MUSIC("Assets/sounds/background.mp3")
background_music.play() # there are various methods to change volume, fade, etc..
```

```py
# for sound libraries
soundcard_lvl1 = Indie.sound_manager.SOUND()
soundcard_lvl1.add("die","Assets/sounds/die.wav")
soundcard_lvl1.add("shoot","Assets/sounds/shoot.wav")

# to play the sound 
soundcard_lvl1.play("die")
```