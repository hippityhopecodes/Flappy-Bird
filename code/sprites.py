import pygame
from settings import *

class Background(pygame.sprite.Sprite):
    """ Class which builds the background of the game """
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load('graphics/environment/background.png').convert()
        self.rect = self.image.get_rect(topleft = (0, 0))