
def clamp(value,min,max):
    if value <min:
        return min
    elif value > max:
        return max
    else:
        return value

class COLOUR():
    """
    Make a colour using RGB values\n
    """
    def make(self,R,G,B) -> None:
        """
        Make a new Colour with the help of RGB values\n
        Parameters:\n
        R: Red(int) range(0,255)\n
        G: Green(int) range(0,255)\n
        B: BLUE(int) range(0,255)\n
        """
        return (clamp(R,0,255),clamp(G,0,255),clamp(B,0,255))

    #Standared colours
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