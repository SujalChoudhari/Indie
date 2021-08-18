from .image import IMAGE
import pygame
from . import app  as e

class TILEMAP(IMAGE):
    """
    Create custom tilemaps for levels
    """
    map_size = [20, 20]
    tile_size = 64
    map_location = ""
    game_map = []
    tiles = {}
    # Tiles {} example
    # {
    # "1":image(IMAGE),
    # "2":image(IMAGE),
    # "3":image(IMAGE),
    # "4":image(IMAGE),
    # "5":image(IMAGE),
    # }


    tile_rects = []

    def loadmap(self):
        """
        Load a map from a file
        Example content:
        /level.txt
            1111
            1001
            1111

        """
        with open(self.map_location) as f:
            level = f.read()
        string1 = level.split("\n")
        self.game_map = list(map(list, string1))

    def blit(self):
        """
        Draw the entire the map 
        """
        y = 0
        for row in self.game_map:
            x = 0
            for tile in row:
                if tile in self.tiles:
                    e.screen.blit(
                        self.tiles[tile].image, (x * self.tile_size, y * self.tile_size))
                if tile != 0 or tile != "":
                    self.tile_rects.append(pygame.Rect(
                        x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size))

                x += 1
            y += 1
        return

    def collision_test(self, player):
        """
        Detects collision for the tilemaps
        """
        hit_list = []
        for tile in self.tile_rects:
            if player.colliderect(tile):
                hit_list.append(tile)
        return hit_list
