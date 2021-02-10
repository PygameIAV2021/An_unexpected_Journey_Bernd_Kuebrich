import pygame
from map import TILESIZE

#Klasse für Ganon
class Ganon():
    def __init__(self, level, Ganon_pos = [800, 300]):
        self.Ganon = pygame.image.load('sprites/ganon.png')
        self.Health = 250
        self.rect = pygame.Rect(Ganon_pos[0], Ganon_pos[1], 100, 100)
        self.level = level
        self.alive = True

#Klasse für Beast
class Beast():
    def __init__(self, level, Beast_pos = []):
        self.Beast = pygame.transform.scale(pygame.image.load('sprites/beast.png'), (TILESIZE, TILESIZE))
        self.Beast_pos = Beast_pos
        self.Health = 100
        self.rect = pygame.Rect(Beast_pos[0], Beast_pos[1], 50, 50)
        self.level = level
        self.move_x = -9
        self.move_y = 0
        self.changeDirectionCounter = 10
        self.moveCounter = 0
        self.alive = True
        self.direction = "Left"

    #Methode für Beastbewegung
    def move(self):
        self.rect.move_ip(self.move_x, self.move_y)
        self.moveCounter += 1
        if self.moveCounter > self.changeDirectionCounter:
            self.move_x *= -1
            self.move_y *= -1
            self.moveCounter = 0
            self.Beast = pygame.transform.flip(self.Beast, True, False)
            if self.direction == "Left":
                self.direction = "Right"
            else:
                self.direction = "Left"