import pygame
from map import *

spielfeld = [[0 for y in range(MAPWIDTH)] for x in range(MAPHEIGHT)]

class Spielfiguren:
    def __init__(self, name, pos_x, pos_y, look, speed=10, spritecounter=0):
        self.name = name
        self.speed = speed
        self.look = look
        self.rect = pygame.Rect(pos_x, pos_y, TILESIZE, TILESIZE)
        self.spritecounter = spritecounter
        self.link_go_up = [pygame.image.load("sprites/link/link_b0.png"), pygame.image.load("sprites/link/link_b1.png"), pygame.image.load("sprites/link/link_b2.png"), pygame.image.load("sprites/link/link_b3.png"), pygame.image.load("sprites/link/link_b4.png"), pygame.image.load("sprites/link/link_b5.png"), pygame.image.load("sprites/link/link_b6.png"), pygame.image.load("sprites/link/link_b7.png")]
        self.link_go_down = [pygame.image.load("sprites/link/link_f0.png"), pygame.image.load("sprites/link/link_f1.png"), pygame.image.load("sprites/link/link_f2.png"), pygame.image.load("sprites/link/link_f3.png"), pygame.image.load("sprites/link/link_f4.png"), pygame.image.load("sprites/link/link_f5.png"), pygame.image.load("sprites/link/link_f6.png"), pygame.image.load("sprites/link/link_f4.png")]
        self.link_go_left = [pygame.image.load("sprites/link/link_l3.png"), pygame.image.load("sprites/link/link_l1.png"), pygame.image.load("sprites/link/link_l2.png"), pygame.image.load("sprites/link/link_l0.png"), pygame.image.load("sprites/link/link_l4.png"), pygame.image.load("sprites/link/link_l5.png"), pygame.image.load("sprites/link/link_l6.png"), pygame.image.load("sprites/link/link_l7.png")]
        self.link_go_right = [pygame.image.load("sprites/link/link_r0.png"), pygame.image.load("sprites/link/link_r1.png"), pygame.image.load("sprites/link/link_r2.png"), pygame.image.load("sprites/link/link_r3.png"), pygame.image.load("sprites/link/link_r4.png"), pygame.image.load("sprites/link/link_r5.png"), pygame.image.load("sprites/link/link_r6.png"), pygame.image.load("sprites/link/link_r7.png")]

    def tryToMove(self, direction):

        moveX, moveY = (0, 0)

        if direction == "down":
            self.look = "down"
            #DISPLAYSURFACE.blit(self.link_go_down[self.spritecounter], (self.rect.left, self.rect.top))
            if self.rect.top < ( MAPHEIGHT * TILESIZE) - TILESIZE:  # if Bedingung damit die figur nicht über den unteren rand hinausgeht
                moveX, moveY = (0, self.speed)
        elif direction == "up":
            self.look = "up"
            #DISPLAYSURFACE.blit(self.link_go_up[self.spritecounter], (self.rect.left, self.rect.top))
            if self.rect.top >= self.speed:
                moveX, moveY = (0, -1*self.speed)
        elif direction == "right":
            self.look = "right"
            #DISPLAYSURFACE.blit(self.link_go_right[self.spritecounter], (self.rect.left, self.rect.top))
            if self.rect.left < (MAPWIDTH * TILESIZE) - TILESIZE:  # if Bedingung damit die figur nicht über den rechten rand hinausgeht
                moveX, moveY = (self.speed, 0)
        elif direction ==  "left":
            self.look = "left"
            #DISPLAYSURFACE.blit(self.link_go_left[self.spritecounter], (self.rect.left, self.rect.top))
            if self.rect.left > 0:  # if Bedingung damit die figur nicht über den linken rand hinausgeht
                moveX, moveY = (-1*self.speed, 0)

        collisionList = [0 for x in range(MAPWIDTH*MAPHEIGHT)]
        i = 0
        for x in range(MAPHEIGHT):
            for y in range(MAPWIDTH):
                collisionList[i] = spielfeld[x][y]
                i += 1

        self.rect.move_ip(moveX, moveY) #verändere deine Position um diffx und diffy

        result = self.rect.collidelistall(collisionList) #liefert index (aus collisionList) von allen rects mit kollisionen

        print("collision with: ")
        for index in result:
            print(collisionList[index].type)
            if collisionList[index].type in [Tiles.WATER, Tiles.WALL]:
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

class Spielkachel(pygame.Rect):
    def __init__(self, typ, x, y):
        super().__init__(x, y, TILESIZE, TILESIZE)
        self.type = typ

#Bodenkachelerkennung
for x in range(MAPHEIGHT):
    for y in range(MAPWIDTH):
        spielfeld[x][y] = Spielkachel(MAP1[x][y], y*TILESIZE, x*TILESIZE)