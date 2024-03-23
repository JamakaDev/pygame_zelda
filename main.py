import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self):
          
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
        pygame.display.set_caption('Here\'s your fucking Zelda game Bryan')
        self.clock = pygame.time.Clock()

        self.level = Level()
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type in [pygame.QUIT, pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit('You closed the program!')

            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    # game.run()