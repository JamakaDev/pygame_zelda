import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, position, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('.//graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=position)
        self.hitbox = self.rect.inflate(0,-25)
        self.obstacle_sprites = obstacle_sprites
        self.direction = pygame.math.Vector2()
        self.velocity = 5

        

    def key_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN]: self.direction.y = 1
        elif keys[pygame.K_UP]: self.direction.y = -1
        else: self.direction.y = 0

        if keys[pygame.K_LEFT]:self.direction.x = -1
        elif keys[pygame.K_RIGHT]: self.direction.x = 1
        else: self.direction.x = 0


    def move(self, velocity):
        if self.direction.magnitude(): 
            self.direction = self.direction.normalize()
        
        self.hitbox.x += self.direction.x * velocity
        self.collision(HORIZONTAL)
        self.hitbox.y += self.direction.y * velocity
        self.collision(VERTICAL)
        self.rect.center = self.hitbox.center


    def collision(self, direction):
        if direction == 'HORIZONTAL':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: self.hitbox.right = sprite.hitbox.left # Moving RIGHT
                    if self.direction.x < 0: self.hitbox.left = sprite.hitbox.right # Moving LEFT

        if direction == 'VERTICAL':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: self.hitbox.bottom = sprite.hitbox.top # Moving DOWN
                    if self.direction.y < 0: self.hitbox.top = sprite.hitbox.bottom # Moving UP
                        

    def update(self):
        self.key_input()
        self.move(self.velocity)

    