# coding: ascii
# indieEngine - Indie Engine Library, made with pygame
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the MIT
# License as published by the Free Software Foundation;
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the MIT
#  License for more details.
#
# You should have received a copy of the MIT
# License along with this library;

# Sujal Choudhari
# https://notsujal.github.io

"""INDIE Engine is a set of Python modules designed for writing games.
It is written on top of the excellent Pygame library. This allows you
to create basic games and multimedia programs in the python
language. The package is highly portable, with games running on
Windows, MacOS, OS X, BeOS, FreeBSD, IRIX, and Linux, as defined by pygame module"""

try:
    from .app  import *
    from .button import BUTTON as Button
    from .character_controller import CHARACTER_CONTROLLER as Character_Controller
    from .colour import COLOUR as Colour
    from .files import FILE as File
    from .font import FONT as Font
    from .gameobject import GAMEOBJECT as GameObject
    from .image import IMAGE as Image
    from .input_feild import INPUTFEILD as InputFeild
    from .inputs import KEY as Key
    from .inputs import EVENT as Event
    from .panel import PANEL as Panel
    from .physics import *
    from .physics import VECTOR as Vector
    from .physics import QUAD as Quad
    from .sound_manager import SOUND as Sound
    from .sound_manager import MUSIC as Music
    from .spritesheet import SPRITESHEET as Spritesheet
    from .spritestrip_animation import SPRITESTRIP_ANIMATION as Spritestrip_animation
    from .text import TEXT as Text
    from .tilemap import TILEMAP as Tilemap
    from .transform import TRANSFORM as Transform

    # editor 
    # from .editor_classes import WINDOW as Window
    # from .editor_classes import INSPECTOR as Inspector
    # from .editor_classes import NAVBAR as Navbar
    # from .editor_classes import DROPDOWN as Dropdown
    # from .editor_classes import NEWPROJECT as NewProject
except Exception as e:
    print(e)

print("\n\n\nThanks for using IndieEngine. https://github.com/NotSujal/Indie \n\n\n")

