import pygame, sys, time
from settings import *
from sprites import Background, Ground, Plane, Obstacle

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

        # scale factor for sprites
        bg_height = pygame.image.load('graphics/environment/background.png').get_height()
        self.scale_factor = WINDOW_HEIGHT / bg_height

        # sprite setup
        Background(self.all_sprites, self.scale_factor)
        Ground([self.all_sprites, self.collision_sprites], self.scale_factor)
        self.plane = Plane(self.all_sprites, self.scale_factor / 1.8)

        # timer for the game
        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer, 1400)

    def collisions(self):
        if pygame.sprite.spritecollide(self.plane, self.collision_sprites, False, pygame.sprite.collide_mask)\
            or self.plane.rect.top <= 0:
            pygame.quit()
            sys.exit()

    def run(self):
        last_time = time.time()
        while True:

            # delta time, accounts for differing framerates
            dt = time.time() - last_time
            last_time = time.time()
            
            #event loop, handles quit logic, mouse clicks, and obstacle spawning
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.plane.jump()
                
                if event.type == self.obstacle_timer:
                    Obstacle([self.all_sprites, self.collision_sprites], self.scale_factor * 1.1)

            # game logic, updates pygame and calls the frame rate
            self.display_surface.fill('black')
            self.all_sprites.update(dt) 
            self.collisions()
            self.all_sprites.draw(self.display_surface)

            pygame.display.update()
            self.clock.tick(FRAMERATE)

    
# If the current file is the main file, run the game
if __name__ == '__main__':
    game = Game()
    game.run()