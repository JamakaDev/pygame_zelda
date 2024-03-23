import pygame
from settings import *
from tile import Rock, Grass, Sand
from player import Player
from debug import debug


class Level():
    def __init__(self):
        
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        # Setting up the sprites
        self.create_map()


    def create_map(self):
        for row_idx, row in enumerate(LEVEL_1):
            for col_idx, col in enumerate(row):
                x, y = col_idx * TILESIZE, row_idx * TILESIZE
                if col == 'R': Rock((x,y),[self.visible_sprites, self.obstacle_sprites])
                if col == 'P': self.player = Player((x,y),[self.visible_sprites], self.obstacle_sprites)
                if col == ' ': Sand((x,y), [self.visible_sprites])
                


# debug(self.player.direction)
    def run(self):
        # Update and draw the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()



class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()
    

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_position = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_position)