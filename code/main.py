import pygame
import sys
import time
from settings import *
from sprites import Background

class Game:
    """ Class which builds the actual Flappy Bird Game	"""

    def __init__(self):
        # sets up the game's display, caption, and clock
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Flappy Bird')
        self.clock = pygame.time.Clock()

        # sprite groups for all sprites and collision sprites
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        # sprite setup
        Background(self.all_sprites)

    def run(self):
        last_time = time.time()
        while True:

            # delta time, accounts for differing framerates
            dt = time.time() - last_time
            last_time = time.time()
            
            #event loop, handles quit logic
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit

            # game logic, updates pygame and calls the frame rate
            self.all_sprites.draw(self.display_surface)

            pygame.display.update
            self.clock.tick(FRAMERATE)
    
# If the current fil is the main file, run the game
if __name__ == '__main__':
    game = Game()
    game.run()