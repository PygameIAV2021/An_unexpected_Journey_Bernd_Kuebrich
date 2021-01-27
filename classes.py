import pygame
from map import Map, TILESIZE, MAPHEIGHT, MAPWIDTH, DISPLAYSURFACE, Tiles

class Player():
    def __init__(self, name, pos, look, map: Map, speed=10, spritecounter=0, health=100, inventory = []):
        self.name = name
        self.map = map
        self.speed = speed
        self.look = look
        self.rect = pygame.Rect(pos[0], pos[1], TILESIZE, TILESIZE)
        self.spritecounter = spritecounter
        self.link_go_up = [pygame.image.load("sprites/link/link_b0.png"), pygame.image.load("sprites/link/link_b1.png"), pygame.image.load("sprites/link/link_b2.png"), pygame.image.load("sprites/link/link_b3.png"), pygame.image.load("sprites/link/link_b4.png"), pygame.image.load("sprites/link/link_b5.png"), pygame.image.load("sprites/link/link_b6.png"), pygame.image.load("sprites/link/link_b7.png")]
        self.link_go_down = [pygame.image.load("sprites/link/link_f0.png"), pygame.image.load("sprites/link/link_f1.png"), pygame.image.load("sprites/link/link_f2.png"), pygame.image.load("sprites/link/link_f3.png"), pygame.image.load("sprites/link/link_f4.png"), pygame.image.load("sprites/link/link_f5.png"), pygame.image.load("sprites/link/link_f6.png"), pygame.image.load("sprites/link/link_f4.png")]
        self.link_go_left = [pygame.image.load("sprites/link/link_l3.png"), pygame.image.load("sprites/link/link_l1.png"), pygame.image.load("sprites/link/link_l2.png"), pygame.image.load("sprites/link/link_l0.png"), pygame.image.load("sprites/link/link_l4.png"), pygame.image.load("sprites/link/link_l5.png"), pygame.image.load("sprites/link/link_l6.png"), pygame.image.load("sprites/link/link_l7.png")]
        self.link_go_right = [pygame.image.load("sprites/link/link_r0.png"), pygame.image.load("sprites/link/link_r1.png"), pygame.image.load("sprites/link/link_r2.png"), pygame.image.load("sprites/link/link_r3.png"), pygame.image.load("sprites/link/link_r4.png"), pygame.image.load("sprites/link/link_r5.png"), pygame.image.load("sprites/link/link_r6.png"), pygame.image.load("sprites/link/link_r7.png")]
        self.health = health
        self.inventory = inventory

    def tryToMove(self, direction):

        moveX, moveY = (0, 0)

        if direction == "down":
            self.look = "down"
            if self.rect.top < ( MAPHEIGHT * TILESIZE) - TILESIZE:  # if Bedingung damit die figur nicht über den unteren rand hinausgeht
                moveX, moveY = (0, self.speed)
        elif direction == "up":
            self.look = "up"
            if self.rect.top >= self.speed:
                moveX, moveY = (0, -1*self.speed)
        elif direction == "right":
            self.look = "right"
            if self.rect.left< (MAPWIDTH * TILESIZE) - TILESIZE:  # if Bedingung damit die figur nicht über den rechten rand hinausgeht
                moveX, moveY = (self.speed, 0)
        elif direction == "left":
            self.look = "left"
            if self.rect.left > 0:  # if Bedingung damit die figur nicht über den linken rand hinausgeht
                moveX, moveY = (-1*self.speed, 0)

        self.rect.move_ip(moveX, moveY) #verändere deine Position um diffx und diffy

        rectList = self.map.returnRectList()
        result = self.rect.collidelistall(rectList) #liefert index (aus collisionList) von allen rects mit kollisionen

        for index in result:
            if rectList[index].type in [Tiles.WATER, Tiles.WALL, Tiles.TREE1, Tiles.TREE2]:
                self.rect.move_ip(-1*moveX, -1*moveY)
                return

        self.spritecounter += 1
        if self.spritecounter > 7:
            self.spritecounter = 0
            
    def draw(self):
        if self.look == "up":
            DISPLAYSURFACE.blit(self.link_go_up[self.spritecounter],
                                (self.rect.left, self.rect.top))

        elif self.look == "down":
            DISPLAYSURFACE.blit(self.link_go_down[self.spritecounter],
                                (self.rect.left, self.rect.top))

        elif self.look == "left":
            DISPLAYSURFACE.blit(self.link_go_left[self.spritecounter],
                                (self.rect.left, self.rect.top))

        elif self.look == "right":
            DISPLAYSURFACE.blit(self.link_go_right[self.spritecounter],
                                (self.rect.left, self.rect.top))

    def changeLevel(self, position, map):
        self.rect.left = position[0]
        self.rect.top = position[1]
        self.map = map

class Sword():
    def __init__(self):
        self.NAME = 'Sword'
        self.IMAGE = pygame.image.load('sprites/sword.png')
        self.IMAGE_ARMED = pygame.transform.scale(self.IMAGE, (35, 35))
        self.POS = [500, 500]
        self.PLACED = True


class Shield():
    def __init__(self):
        self.NAME = 'SHIELD'
        self.IMAGE = pygame.image.load('./sprites/shield.png')
        self.POS = [250, 250]
        self.PLACED = True

class Ganon():
    def __init__(self, Ganon_pos = [300, 800]):
        self.Ganon = pygame.image.load('./sprites/ganon.png')
        self.Ganon_pos = Ganon_pos
        self.Health = 250
        self.rect = pygame.Rect(Ganon_pos[0], Ganon_pos[1], 100, 100)

class Bow():
    def __init__(self):
        self.NAME = 'BOW'
        self.IMAGE = pygame.transform.scale(pygame.image.load('./sprites/bow.png'), (50, 50))
        self.POS = [400, 400]
        self.PLACED = True
