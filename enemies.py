import pygame
from map import TILESIZE

class Ganon():
    def __init__(self, level, Ganon_pos = [800, 300]):
        self.Ganon = pygame.image.load('sprites/ganon.png')
        self.Health = 250
        self.rect = pygame.Rect(Ganon_pos[0], Ganon_pos[1], 100, 100)
        self.level = level

class Beast():
    def __init__(self, level, Beast_pos = []):
        self.Beast = pygame.transform.scale(pygame.image.load('sprites/beast.png'), (TILESIZE, TILESIZE))
        self.Beast_pos = Beast_pos
        self.Health = 100
        self.rect = pygame.Rect(Beast_pos[0], Beast_pos[1], 50, 50)
        self.level = level