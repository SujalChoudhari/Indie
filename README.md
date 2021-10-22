# Indie Engine

##  Getting Started
Here is a quick-start guide to getting started with Indie Engine.

1. Download the files from [github](https://github.com/Notsujal/Indie).
or type in the terminal
```py
pip install indie-engine
```




2. Create a new python file outside the IndieEngine folder
In this case its `test.py`


3. Import IndieEngine into your file  
    `import IndieEngine as ie`


## Creating Screen
A Screen is a place where the game runs and is visible to player.
To create screen/window follow these steps.

1. Set the window constants
    ```py
        # Default Screen Constants
        background_colour = colour.COLOUR.White
        caption = "Indie Engine"
        fps = 60
        screen_size = QUAD(0,0,900,600) # a quad stores the corner points of a rectangle (x,y,width,height)

        scale_amount = 1 # zoom of the main screen (to increase the pixel size)
        icon_file = "" # path th the icon file goes here
        scalable = False # set if user can resize the window for their comfert.

    ```
    Lets change the caption and screensize
    ```py
    # the code should look like this
    import IndieEngine as ie  

    ie.app.init(caption="Indie Engine",fps= 30, scalable= True, screen_size=ie.Vector(500,400))
    # make sure you initiate the package before you run the game
    ```

2. Run the main loop using `ie.run()`. We now have a blank screen to work with.
    ```py
    import IndieEngine as ie  

    ie.app.init(caption="Indie Engine",fps= 30, scalable= True, screen_size=ie.Vector(500,400))

    ie.run()
    ```


## Update, Draw and Inputs


`update`: code inside the update is called every frame.

`draw` : draw mwthod is used to draw/blit objects on screen, it is called right after update method.

`inputs` : this methods gives events and mouse position to the sub-methods for easy handling.

Ideal way to start

```py
import IndieEngine as ie  

ie.app.init(caption="Indie Engine",fps= 30, scalable= True, screen_size=ie.Vector(500,400))


def game():
    def Update():
        pass

    def Draw():
        pass

    def Inputs(event,mouse): 
        pass

    ie.run(Update,Draw,Inputs) # run calls these methods when required
    # make sure u don't call the functions, and pass them as a object.

game() # with this you can have multiple screens
```

## Game Objects
Every Object in the game is a Game Object.
It holds the parent object, may be usefull for alingning the childs later on.

```py
# set parent 
obj1 = ie.GameObject()
obj2 = ie.GameObject()
obj1.parent = obj2
```

## Transform
Transform class allows access to position, size and rotation of the object.

`align`  - align the object with respect to any object easily

`stretch` - stretch a object to its parent size

```py
# create a parent object
parent = ie.Transform(ie.Quad(0,0,200,200),0)

#create a child
transform1 = ie.Transform(ie.Quad(0,0,100,100),0)
# assign clild to the parent
transform1.parent = parent
# modify values
transform1.size = ie.Vector(120,120)
transform1.rotation = 20
# align function of transform
transform1.align(transform1.parent,"top-left")
# arguments for anchor are:
    # top-left
    # top-center
    # top-right

    # middle-left
    # middle-center
    # middle-right

    # bottom-left
    # bottom-right
    # bottom-center

transform1.stretch("fill",transform1.parent)
# arguments for stretch
    # fill - fill the entire parent
    # horizontal - fill only horizontally
    # vertical - fill only vertically

```


## Colour
This class has a method to make new colours, with some predefined colours

```py
black = ie.Colour().make(0,0,0)

#Standared colours
ie.Colour.Black
ie.Colour.White	
ie.Colour.Red	    
ie.Colour.Lime	
ie.Colour.Blue	
ie.Colour.Yellow	
ie.Colour.Aqua	
ie.Colour.Fuchsia	
ie.Colour.Silver	
ie.Colour.Gray	
ie.Colour.Maroon	
ie.Colour.Olive	
ie.Colour.Green	
ie.Colour.Purple	
ie.Colour.Teal	
ie.Colour.Navy	
```



## Image
This class allows us to draw images on screen.


```py

def game():

    image = ie.Image(ie.Quad(100,100,520,220),45,"Resources/folder.png")

    def Draw():
        image.blit()


    ie.run(update=None,draw=Draw,inputs = None)

game()
```

## Panel
This allows us to draw Rectangles on the screen,
This is a backbone class for other classes.

```py
def game():

    panel = ie.Panel(ie.Quad(0,0,200,300),10,0,ie.Colour.Black)

    def Draw():
        panel.blit()

    ie.run(update=None,draw=Draw,inputs = None)


game()
```

## Font
Font class allows us to create font assets and use them on text when required

```py
font_14 = ie.Font("Resources\font_big.ttf",14)
```

## Text
Text class allows us to create and display one-liner texts

```py
def game():
    font_14 = ie.Font("Resources/font_big.ttf",14)
    text = ie.Text(ie.Quad(0,0,100,100),"Here is some text",font_14,ie.Colour.Fuchsia,ie.Colour.Navy)

    def Draw():
        text.blit()
   
   ie.run(update=None,draw=Draw,inputs = None)

game()
```

## Button
This is a faster way to create buttons and handle inputs.
Buttton has three variables, `ishovered`, `ispressed` and `isselected` which we can use to control stuff.

Here is a example of a button 

```py
font_14 = ie.Font("Resources/font_big.ttf",14)
def game():
    

    button = ie.Button(ie.Quad(10,20,30,40),"Button",font_14,ie.Colour.Fuchsia,ie.Colour.Lime)


    def Update():
        if button.ishovered:
            # do some stuff
            pass
        if button.ispressed:
            # do some stuff
            pass
        if button.isselected:
            # do some stuff
            pass

    def Draw():
        button.blit()
        pass

    def Inputs(event,mouse): 
        button.control(event,mouse)
        pass

    ie.run(Update,Draw,Inputs)

game()
```

## Tile Maps
Tile maps help us to create environments with few lines of code( collision included with character controller)
You can assign each tile-type a id, based on that you can make it collidable.
You can overlay tiles to create effects, or layers.

```py
import IndieEngine as ie

ie.app.init(caption="Indie Engine", fps=30, scalable=True,
            screen_size=ie.Vector(500, 400))


def game():
    level1 = ie.Tilemap(16, "Resources/map1.txt",
                        tiles={
                            "1": ie.Image(ie.Quad(0, 0, 16, 16), 0, "Resources/folder.png"),
                            "2": ie.Image(ie.Quad(0, 0, 16, 16), 0, "Resources/blank_screen.png"),
                        })

    # specify which tiles are acctually collidable from tiles array.
    level1.loadmap(collidable_tiles=["1"])  # tile with id 1 is collidable, rest are not.

    def Draw():
        level1.blit()
        pass
    ie.run(draw=Draw)

game()
```

/Resources/map1.txt
```
1111
222
1111
2
```

## Character Controller
This is 8 way character controller,
assign buttons and movements to get going.

```py
import IndieEngine as ie

ie.app.init(caption="Indie Engine", fps=30, scalable=True,scale_amount=5,
            screen_size=ie.Vector(900,600))

def game():
    level1 = ie.Tilemap(16, "Resources/map1.txt",
                        tiles={
                            "1": ie.Image(ie.Quad(0, 0, 16, 16), 0, "Resources/folder.png"),
                            "2": ie.Image(ie.Quad(0, 0, 16, 16), 0, "Resources/blank_screen.png"),
                        })

    player = ie.Character_Controller(ie.Quad(0,0,16,16),20,"Resources/folder.png",20)

    # specify which tiles are acctually collidable from tiles array.
    level1.loadmap(collidable_tiles=["1"])  # tile with id 1 is collidable, rest are not.

    def Update():
        player.move() # move the player as required


    def Draw():
        level1.blit()
        player.blit()

    def Inputs(event,mouse):
        player.control(event)

    ie.run(Update,Draw,Inputs)

game()
```

## Sprite Sheets
sprite sheets are performant way to add graphics to the game, it loads up a huge image instead of 1000 unique ones. And crops out the required part of it.

The classes are taken from [here](https://www.pygame.org/wiki/Spritesheet)

Explore the package files to know about more functions related to it.

```py
import IndieEngine as ie

ie.app.init(caption="Indie Engine", fps=30, scalable=True,scale_amount=5,
            screen_size=ie.Vector(900,600))

def game():
    spritesheet = ie.Spritesheet("Resources/folder.png")
    # individual sprites
    player = spritesheet.image_at((32,32,16,16),ie.Colour.White)

    #can be used to create tilemaps
    tilemap = ie.Tilemap(16,"demo.txt",tiles={
        "1": spritesheet.image_at((0,0 ,16,16),ie.Colour.White),
        "2": spritesheet.image_at((0,16,16,16),ie.Colour.White),
        "3": spritesheet.image_at((0,32,16,16),ie.Colour.White),
        "4": spritesheet.image_at((0,48,16,16),ie.Colour.White),
        
    })
    def Update():
        pass
    def Draw():
        player.blit()
        pass
    def Inputs(event,mouse):
        pass

    ie.run(Update,Draw,Inputs)

game()

```

## Sprite Strip Animations
This class derives from SpriteSheet and thus is taken from [here](https://www.pygame.org/wiki/Spritesheet).

Load a strip of images with this class and use it as a frame by frame animation sequence.

```py

from pygame import Color
import IndieEngine as ie

ie.app.init(caption="Indie Engine", fps=30, scalable=True,scale_amount=5,
            screen_size=ie.Vector(900,600))

def game():
    player = ie.Character_Controller(ie.Quad(0,0,16,16),20,"Resources/folder.png",20)

    player_anim = ie.Spritestrip_animation("Resources/folder.png",(0,16,16,16),3,ie.Colour.White,loop=True,frames=3)
    player_anim.iter() # iterate through the images once


    def Update():
        player.move()
        player.image = player_anim.next() # bring on the next frame

    def Draw():
        player.blit()

    def Inputs(event,mouse):
        player.control(event)


    ie.run(Update,Draw,Inputs)

game()
```

## Files
With this class You can store/get data in json files.

```py
file_manager = ie.File("settings")

file_manager.save("volume", 0.5)
file_manager.save("name", "Indie Engine")


print(file_manager.get("volume"))
print(file_manager.get("name"))

file_manager.delete("volume")
```


## Music
This is extended Pygame.Mixer Library
```py
bg_music = ie.Music("demo.mp3")

bg_music.play(loops=-1,start=0,fade_ms=10)
#      loops =-1 ---> play infinitely
#      start =0 ----> start at 0 sec
#      fade = 10 ---> fade 10 ms

bg_music.volume(0.4) 

bg_music.pause()

bg_music.unpause()

bg_music.fadeout()

bg_music.stop()

```

## Sounds
Sounds is a class which can play sounds when needed.
```py
death = ie.Sound(sounds={
    "death_1": "sounds/death/1.mp3",
    "death_2": "sounds/death/2.mp3",
    "death_3": "sounds/death/3.mp3",
    "death_4": "sounds/death/4.mp3"
})

death.add("death_boss","sounds/death/boss.wav")
death.remove("death_2")
death.play("death_1")
```

Thanks for using Indie Engine!