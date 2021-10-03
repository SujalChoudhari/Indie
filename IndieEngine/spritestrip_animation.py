from .image import IMAGE
from . import spritesheet


class SPRITESTRIP_ANIMATION(IMAGE):
    """sprite strip animator\n
    
    This class provides an iterator (iter() and next() methods), and a\n
    __add__() method for joining strips which comes in handy when a\n
    strip wraps to the next row.\n
    """
    def __init__(self, filename, rect, count, colorkey=None, loop=False, frames=1):
        """construct a SpriteStripAnim\n
        \n
        filename, rect, count, and colorkey are the same arguments used\n
        by spritesheet.load_strip.\n
        \n
        loop is a boolean that, when True, causes the next() method to\n
        loop. If False, the terminal case raises StopIteration.\n
        \n
        frames is the number of ticks to return the same image before\n
        the iterator advances to the next image.\n
        """
        self.filename = filename
        ss = spritesheet.SPRITESHEET(filename)
        self.images = ss.load_strip(rect,count,colorkey)
        self.i = 0
        self.loop = loop
        self.frames = frames
        self.f = frames


    def iter(self):
        """
        Iterate through the animation once\n
        """
        self.i = 0
        self.f = self.frames
        return self


    def next(self):
        """
        Bring up the next frame of the animation\n
        """
        if self.i >= len(self.images):
            if not self.loop:
                raise StopIteration
            else:
                self.i = 0
        image = self.images[self.i]
        self.f -= 1
        if self.f == 0:
            self.i += 1
            self.f = self.frames
        return image

    def __add__(self, ss):
        """
        Join a animation with another animation\n
        \n
        Parameters:\n
        ss(SPRITESHEET):\n
        """
        self.images.extend(ss.images)
        return self