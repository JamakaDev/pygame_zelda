import pygame
from settings import *

class Rock(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load('.//graphics/test/rock.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=position)
        self.hitbox = self.rect.inflate(0,-10)


class Grass(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load('.//graphics/grass/grass_1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=position)
        self.hitbox = self.rect.inflate(0,-10)


class Sand(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.sprite_sheet = pygame.image.load('.//graphics/tilemap/Floor.png').convert_alpha()
        self.images = [self.sprite_sheet.subsurface(((x, y), (TILESIZE, TILESIZE))) for y in range(1600) for x in range(1408) if (not x % TILESIZE and not y % TILESIZE)]
        self.image = self.images[23]
        self.rect = self.image.get_rect(topleft=position)
        

    

    
    
