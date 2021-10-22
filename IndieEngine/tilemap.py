import pygame
from .gameobject import GAMEOBJECT
from . import app  as e
from . import physics
class TILEMAP(GAMEOBJECT):
    """
    Create custom tilemaps for levels

    Tiles {} example
    {
    "1":image(IMAGE),
    "2":image(IMAGE),
    "3":image(IMAGE),
    "4":image(IMAGE),
    "5":image(IMAGE),
    }
    """

    def __init__(self,tile_size=16,map_location = "",tiles={}) -> None:
        
        self.tile_size =tile_size
        self.map_location = map_location
        self.tiles = tiles
   
    
    

    blitable_rect_list = []
    game_map = []
    tile_rects = []

    def loadmap(self,collidable_tiles = ["","0"]):
        """
        Load a map from a file\n
        Example content:\n
        /level.txt\n
            1111\n
            1001\n
            1111\n
        \n
        """
        with open(self.map_location) as f:
            level = f.read()
        string1 = level.split("\n")
        self.game_map = list(map(list, string1))

        y = 0
        for row in self.game_map:
            x = 0
            for tile in row:
                if tile in self.tiles:
                    self.blitable_rect_list.append((
                        self.tiles[tile].image, (x * self.tile_size, y * self.tile_size)))
                if tile in collidable_tiles:
                    self.tile_rects.append(pygame.Rect(
                        x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size))
                    physics.collidable_tile_rects += self.tile_rects
                x += 1
            y += 1

    def blit(self):
        """
        Draw the entire the map 
        """
        for tile in self.blitable_rect_list:
            e.screen.blit(tile[0],tile[1])
        
        return

    
