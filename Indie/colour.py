
def clamp(value,min,max):
    if value <min:
        return min
    elif value > max:
        return max
    else:
        return value

class COLOUR():
    """
    COLOUR
    Make a colour using RGB values
    """
    def __init__(self,R,G,B):
        """
        Parameters:
        `R: Red` range(0,255)
        `G: Green` range(0,255)
        `B: BLUE` range(0,255)
        """
        self.R = R
        self.G = G
        self.B = B
    
    def colour(self):
         return (clamp(self.R,0,255),clamp(self.G,0,255),clamp(self.B,0,255))

    
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