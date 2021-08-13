from Engine.Components.image import IMAGE
import pygame
import Engine.Game.defaults as e


class TILEMAP(IMAGE):
    map_size = [20, 20]
    tile_size = 64
    map_location = ""
    game_map = []
    tiles = {}

    tile_rects = []

    def loadmap(self):
        with open(self.map_location) as f:
            level = f.read()
        string1 = level.split("\n")
        self.game_map = list(map(list, string1))

    def blit(self):
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
        hit_list = []
        for tile in self.tile_rects:
            if player.colliderect(tile):
                hit_list.append(tile)
        return hit_list
